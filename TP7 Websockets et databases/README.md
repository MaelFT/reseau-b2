# TP7 DEV : Websockets et databases

Dans ce sujet de TP, non pas une mais deuuuux nouvelles notions :

➜ **les Websockets**

- remplace notre connexion TCP brute
- est lui-même encapsulé dans du TCP
- une alternative à HTTP
- caractéristiques :
  - communication bi-directionnelle
  - gestion de session
  - compression

➜ **Gestion de base de données**

- c'est bien beau les variables globales mais ça va deux minutes...
  - si le programme crash, on perd tout !
  - si un jour l'application grossit et on a besoin de deux serveurs, comment ils se partagent la variable ?
- ici il ne s'agit pas de rentrer dans le détail de fonctionnement des bases : on survole pour être de simples consommateurs des bases de données !

![Websockets](./img/websocket.png)

## Sommaire

- [TP7 DEV : Websockets et databases](#tp7-dev--websockets-et-databases)
  - [Sommaire](#sommaire)
  - [I. Websockets](#i-websockets)
    - [1. First steps](#1-first-steps)
    - [2. Client JS](#2-client-js)
    - [3. Chatroom magueule](#3-chatroom-magueule)
  - [II. Base de données](#ii-base-de-données)
    - [1. Intro données](#1-intro-données)
    - [2. Redis](#2-redis)
    - [3. Bonus : MongoDB](#3-bonus--mongodb)

## I. Websockets

> Voir [la trace écrite du cours Websockets](../../../cours/dev/websockets/README.md) avant de vous attaquer au TP.

### 1. First steps

Comme d'hab on va commencer simple : un ptit client et un p'tit serveur, qui échangent des données.

> AUSSI POUR S'ASSURER QUE VOUS SAVEZ INSTALLER UNE LIB SUR VOTRE POSTE MAINTENANT GRRR 😇

🌞 **`ws_i_1_server.py` et `ws_i_1_client.py`**

- simple client/serveur qui utilisent la librairie Websocket pour communiquer
- tout doit être asynchrone
- la boucle d'utilisation de l'application :
  - l'utilisateur (client) peut saisir une string et l'envoyer au serveur
  - le serveur reçoit le message
    - affiche le message
    - le serveur renvoie au client `Hello client ! Received "<STRING>"` où `<STRING>` est la string saisie/envoyée par le client
  - le client reçoit le message
    - affiche la string retournée par le serveur

➜ **Lance Wireshark** pendant l'échange

- **si t'es un curieux, y'a des trucs cools à voir**
- tu devrais voir l'échange WebSocket
- c'est important de lancer Wireshark AVANT de commencer l'échange :
  - si Wireshark rate le début de la communication il ne sera pas en mesure de comprendre que c'est du trafic Websocket
  - c'est le début de la communication qui contient ce qu'il faut pour comprendre la suite
- admirez la compression à la volée !
  - votre message est illisible sur le réseau
  - il est pas chiffré, il est compressé
  - essayez d'envoyer une string très longue pour voir !

### 2. Client JS

Ouhloulou on va faire du JS en cours de réseau.

Je me sens obligé de me justifier, mais c'est -je trouve- vraiment à sa place :

- **c'est dans un contexte Web que brillent les Websockets** (alternative à HTTP)
  - donc manipuler avec JS c'est manipuler dans le contexte où il est le plus utilisé
- **ici pas de serveur HTTP** : on va exécuter du JS en local côté client
  - ça vous permet aussi de comprendre/vous rappeler qu'un serveur HTTP c'est juste un truc qui permet de télécharger des fichiers
  - si on a déjà le fichier, pas besoin de le télécharger avec HTTP : on peut juste l'exécuter en local !
- **pas de beau framework JS** côté client non plus !
  - on va faire à la main ce que les frameworks modernes embarquent sous le capot

Une fois de plus, je vais pas réinventer la roue quand elle est déjà bien ronde chez les autres.  
[Un lien donc vers la doc officielle de Mozilla](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API/Writing_WebSocket_client_applications) au sujet de l'API WebSocket dans les navigateur (dit autrement : comment ouvrir un websocket en JS, puis send/receive des données).

🌞 **`ws_i_2_client.js`**

- un `.js` donc oui ! Vous l'exécutez en local dans votre navigateur pour vos tests
- doit se comporter comme `ws_i_1_client.py`
- un input utilisateur, et il affiche la string reçue du serveur !

> Pour l'affichage, bah t'as javascript sous la main ! Libre à toi de faire un p'tit formulaire pour l'input, et de créer une div ou un élément de liste quand tu reçois un message ! Ou juste un `alert()`. Ou autre chose ! Démerde-toi, mais reste simple !

**Bah l'exemple est nul, mais ça c'est déjà impossible à faire avec juste du HTTP** : le serveur qui envoie une donnée au client, et le client qui agit en fonction (HTTP c'est toujours le client qui fait une requête, jamais le serveur qui envoie arbitrairement une donnée sans requête du client).

### 3. Chatroom magueule

🌞 **`ws_i_3_server.py` et `ws_i_3_client.{py,js}`**

- un seul fichier pour le client : JS ou Python, libre à toi !
- une chatroom fonctionnelle comme au TP6
  - au moins fonctionnalités minimales : plusieurs clients qui rejoignent et peuvent discuter
  - pas de sockets TCP bruts : que du Websocket !
- le mieux serait de récup le code du TP6 et juste l'adapter pour passer de sockets TCP bruts à des Websockets

➜ **Petit mot technique vitefé en passant**

- la chatroom du TP6 elle est fonctionnelle, opti si vous avez fait des trucs de ouf dans le dév
- bref ça marche bien, c'est pas déconnant, mais c'est pas vraiment pas intégrable dans un contexte Web (et aujourd'hui, tout est web)
- c'est une chatroom autonome, dans son coin
- faire ça en Websockets ça fait que c'est DIRECTEMENT intégrable à une app web (app mobile, site web, autres)
- genre là il manque quasi-rien pour avoir une app mobile fonctionnelle ou un discord-like dans un navigateur

## II. Base de données

### 1. Intro données

➜ Bon dans le cadre du chat, **les données** c'est :

- **la variable globale `clients`**
  - contient toutes les infos des clients connectés : les sessions
  - c'est une donnée très "chaude" qui change tout le temps
- **l'historique du chat**
  - *si t'as fait le bonus, sinon, tu fais genre*
  - une donnée plutôt "tiède" (personne ne dit ça) : accédée assez régulièrement mais ça va
  - on accède pas à tout en même temps :
    - soit on ajoute le dernier message à l'historique
    - soit on lit les N derniers messages pour les envoyer à un client qui se co
    - on modifie jamais une donnée existante

➜ L'idée c'est :

- on veut **pas garder les données dans notre application**, c'est trop fragile
  - donc *exit* la variable globale qui stocke tout
- on veut sortir les données pour les stocker à un endroit dédié
- on pourrait stocker ça sur le disque
  - certains ont fait ça pour le chat au TP6 (format JSON)
  - mais ça rame sa mère le disque, surtout quand le fichier va grossir
  - et on fait comment quand il faut deux serveurs pour soutenir la charge ? Un fichier partagé ? Woah le bordel. Et s'ils modifient à deux le même fichier ? Woah le bordel.
  - *exit* le stockage sur disque
- **le remède : stocker ça en base de données**
  - pour une base, les données sont essentiellement en RAM
  - c'est fast
  - on déporte la gestion des données vers une autre application
  - si cette base de données est sur une autre machine que notre application il faut utiliser... le réseau ! LA BOUCLE EST BOUCLÉE.

➜ **On va aussi stocker/interagir avec les données différemment suivant leur "température"**.

Ici on aimerait :

- **un stockage petit mais très performant pour stocker nos "sessions"**
  - équivalent de la variable globale `client`
  - on a même pas besoin de conserver ça entre les redémarrages limite
  - on va utiliser une base de données Redis
- **un stockage + orienté longue durée pour stocker l'historique**
  - on va utiliser une base de données MongoDB

> *Ouais donc, base de données, mais pas de SQL. La vie est belle.*

### 2. Redis

➜ **Pour installer Redis**

- soit vous gérez votre truc (Docker en local ?)
- soit vous popez une VM Rocky Linux et vous exécuter les commandes suivantes :
  - nécessaire d'avoir une connexion internet dans la VM
  - nécessaire de se co en SSH pour copy/paste mes commandes
  - les commandes :

```bash
# on installe docker vitefé
$ sudo yum install -y yum-utils
$ sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
$ sudo yum install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
$ sudo systemctl enable --now docker

# on lance un ptit conteneur qui tournera à l'infini avec redis dedans
$ sudo docker run -d -p 6379:6379 --restart=always redis
```

Une fois que c'est fait, y'a Redis disponible (depuis votre poste ou une autre VM) à l'adresse : `<IP_VM_REDIS>:6379`.

➜ **P'tit coup de pouce pour la syntaxe de la lib Python `redis` :**

```python
import asyncio
import redis.asyncio as redis # on utilise la version asynchrone de la lib

async def main():
    # connexion au serveur Redis
    client = redis.Redis(host="10.1.1.1", port=6379)
    
    # on définit la clé 'cat' à la valeur 'meo'
    await client.set('cat', 'meow')
    # on définit la clé 'dog' à la valeur 'waf'
    await client.set('dog', 'waf')

    # récupération de la valeur de 'cat'
    what_the_cat_says = await client.get('cat')

    # ça devrait print 'meow'
    print(what_the_cat_says)

    # on ferme la connexion proprement
    await client.aclose()

if __name__ == "__main__":
    asyncio.run(main())
```

🌞 **`ws_ii_2_server.py`**

- adaptez-votre code serveur précédent
- celui-ci n'utilise pas du tout de variable globale `client`
- à la place, il utilise une base de données Redis :
  - ajout d'une donnée quand un nouveau client arrive
  - suppression/modification d'une donnée quand un client s'en va
  - tous les appels à la base de données doivent être asynchrones

### 3. Bonus : MongoDB

🌞 **`ws_ii_3_server.py`**

- bonus-ception vu que l'historique était déjà un bonus
- le serveur stocke l'historique des messages dans une base MongoDB
- il faut donc setup un serveur MongoDB et avoir une lib Python adaptée

![t'as la réf ?](./img/talaref.png)
