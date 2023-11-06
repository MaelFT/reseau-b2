# TP3 DEV : Python et réseau

- [I. Ping](#i-ping)
- [II. DNS](#ii-dns)
- [III. Get your IP](#iii-get-your-ip)
- [IV. Mix](#iv-mix)
- [V. Deploy](#v-deploy)

# I. Ping

🌞 **`ping_simple.py`**

- importez la fonction `system` de la lib `os`
- utilisez-la pour effectuer un `ping 8.8.8.8`

[Lien vers le fichier "ping_simple.py"](./code/ping_simple.py)

---

🌞 **`ping_arg.py`**

- importez la liste `argv` de la lib `sys`
  - cette liste contient les arguments passés au script à l'exécution
- effectuez un `ping` vers l'IP fournie en argument quand on exécute le code

[Lien vers le fichier "ping_arg.py"](./code/ping_arg.py)

🌞 **`is_up.py`**

- même code que `ping_arg.py` mais il doit
  - soit juste afficher "UP !" si la machine répond au ping
  - soit juste afficher "DOWN !" si la machine ne répond pas

[Lien vers le fichier "is_up.py"](./code/is_up.py)

# II. DNS

🌞 **`lookup.py`**

- utilisez la fonction `gethostbyname()` de la lib `socket`
- permet de résoudre un nom de domaine passé en argument à la fonction

[Lien vers le fichier "lookup.py"](./code/lookup.py)

# III. Get your IP

🌞 **`get_ip.py`**

- utilisez la fonction `net_if_addrs()` de la librairie `psutil`
- votre code doit afficher l'adresse IP de votre carte WiFi

[Lien vers le fichier "get_ip.py"](./code/get_ip.py)

# IV. Mix

🌞 **`network.py`**

- doit contenir une fonction `lookup()` qui prend en argument un nom de domaine et retourne l'IP qui correspond
- doit contenir une fonction `ping()` qui prend en argument une IP et retourne "UP !" ou "DOWN !"
- doit contenir une fonction `ip()` qui prend rien en argument et retourne l'IP de la carte WiFi
- **ne doit contenir qu'un seul `print()`**

[Lien vers le fichier "network.py"](./code/network.py)

# V. Deploy

Déployez-moi ça dans une VM Rocky :

- git clone du dépôt git de code, dans la VM
- install/mise à jour de Python si nécessaire
- exécution du code, le code doit fonctionner normalement
