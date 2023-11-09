# I. Simple bs program


🌞 **Commandes...**

```shell
[mael@server code]$ sudo firewall-cmd --add-port=13337/tcp --permanent
success
[mael@server code]$ sudo firewall-cmd --reload
success
```

```shell
[mael@server code]$ python3 bs_server_I1.py
Connected by ('10.33.76.213', 47868)
Données reçues du client : b'Meooooo !'

[mael@client code]$ python3 bs_client_I1.py
Le serveur a répondu b'Hi mate !'
```

```shell
[mael@server code]$ ss -alnp | grep python3
tcp   LISTEN 0      1                                0.0.0.0:13337            0.0.0.0:*     users:(("python3",pid=1756,fd=3))
```