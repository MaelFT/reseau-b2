# TP6 : Chat room

Dans ce TP on continue toujours sur du dév réseau, c'est genre le thème un peu ! On progresse au fil des TPs en voyant de nouvelles notions au fur et à mesure.

Le but à la fin de ce TP : avoir **une petite application de chat à peu près stylée.** Plusieurs clients connectés qui discutent.

![Kittens](./img/kittens.jpg)

Pour ça, on va amener une nouvelle notion : **l'asynchrone.**

> Prenez connaissance du [cours sur le sujet](../../../cours/dev/async/README.md).

En Python ça commence à être bien intégré depuis récemment.
Pour quelque chose de basique comme ce qu'on va faire, la complexité reste sous contrôle.

➜ **Côté client :**

- se connecte au serveur, en indiquant son pseudo
- arrive dans la chatroom
- peut envoyer des messages, qui seront reçus par tous les autres clients connectés

➜ **Côté serveur :**

- attend la connexion de nouveaux clients
- quand un client se connecte, il l'ajoute à la liste des clients présents
- quand un client envoie un message, il le redistribue à tous les autres

## Quelques remarques

Vous allez commencer à produire **pas mal de lignes** de code au fur et à mesure.

Je ne serai pas trop regardant sur les TPs d'avant, mais à partir de maintenant, je serai très regardant sur **la clarté de votre code**. Ne sur-commentez pas chaque ligne, c'est pas ça, parce que c'est pire encore.

Quelques conseils donc :

- **nommez** judicieusement vos variables et fonction
- c'est souvent plus clair si vous **typez** les arguments des fonctions/retours de fonction
- **commentez** les lignes qui ne sont pas assez claires d'elles-mêmes
- éclatez votre code en **plusieurs feuilles** Python, je vous laisse libre pour l'organisation pour le moment

## Sommaire

- [TP6 : Chat room](#tp6--chat-room)
  - [Quelques remarques](#quelques-remarques)
  - [Sommaire](#sommaire)
  - [I. Débuts avec l'asynchrone](#i-débuts-avec-lasynchrone)
  - [II. Chat Room](#ii-chat-room)
  - [III. Bonus](#iii-bonus)

## I. Débuts avec l'asynchrone

Document dédié à la partie I. [Débuts avec l'asynchrone](./async_first_steps.md)

## II. Chat Room

Document dédié à la partie II. [Chat Room](./chat_room.md)

## III. Bonus

Document dédié à la partie III. [Bonus](./bonus.md)
