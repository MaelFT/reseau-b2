# TP1 : Maîtrise réseau du poste

- [I. Basics](#i-basics)
- [II. Go further](#ii-go-further)
- [III. Le requin](#iii-le-requin)

# I. Basics


☀️ **Carte réseau WiFi**

Déterminer...

- l'adresse MAC de votre carte WiFi
```bash
C:\Users\maelf>ipconfig /all
[...]
Wireless LAN adapter Wi-Fi:

   Link-local IPv6 Address . . . . . : fe80::24c:fd19:2865:f46e%6
```
- l'adresse IP de votre carte WiFi
```bash
C:\Users\maelf>ipconfig /all
[...]
Wireless LAN adapter Wi-Fi:

   IPv4 Address. . . . . . . . . . . : 10.33.76.231
```
- le masque de sous-réseau du réseau LAN auquel vous êtes connectés en WiFi
  - en notation CIDR, par exemple `/16`
  - ET en notation décimale, par exemple `255.255.0.0`

```bash
/20
```

```bash
C:\Users\maelf>ipconfig /all
[...]
Wireless LAN adapter Wi-Fi:

   Subnet Mask . . . . . . . . . . . : 255.255.240.0
```

---

☀️ **Déso pas déso**

Pas besoin d'un terminal là, juste une feuille, ou votre tête, ou un tool qui calcule tout hihi. Déterminer...

- l'adresse de réseau du LAN auquel vous êtes connectés en WiFi

```bash

```

- l'adresse de broadcast

```bash

```

- le nombre d'adresses IP disponibles dans ce réseau

```bash

```

---

☀️ **Hostname**

- déterminer le hostname de votre PC

```bash
C:\Users\maelf>hostname
M
```

---

☀️ **Passerelle du réseau**

Déterminer...

- l'adresse IP de la passerelle du réseau

```bash
C:\Users\maelf>ipconfig /all
[...]
Wireless LAN adapter Wi-Fi:

   Default Gateway . . . . . . . . . : 10.33.79.254
```

- l'adresse MAC de la passerelle du réseau

```bash
C:\Users\maelf>ipconfig /all
[...]
Wireless LAN adapter Wi-Fi:

   Physical Address. . . . . . . . . : 40-1A-58-4F-00-0A
```

---

☀️ **Serveur DHCP et DNS**

Déterminer...

- l'adresse IP du serveur DHCP qui vous a filé une IP

```bash
C:\Users\maelf>ipconfig /all
[...]
Wireless LAN adapter Wi-Fi:

   DHCP Server . . . . . . . . . . . : 10.33.79.254
```

- l'adresse IP du serveur DNS que vous utilisez quand vous allez sur internet

```bash
C:\Users\maelf>ipconfig /all
[...]
Wireless LAN adapter Wi-Fi:

   DNS Servers . . . . . . . . . . . : 8.8.8.8
                                       1.1.1.1
```

---

☀️ **Table de routage**

Déterminer...

- dans votre table de routage, laquelle est la route par défaut

```bash
C:\Users\maelf>netstat -r

IPv4 Route Table
===========================================================================
Active Routes:
Network Destination        Netmask          Gateway       Interface  Metric
          0.0.0.0          0.0.0.0     10.33.79.254     10.33.76.231     30
```

---

# II. Go further

☀️ **Hosts ?**

- faites en sorte que pour votre PC, le nom `b2.hello.vous` corresponde à l'IP `1.1.1.1`

```bash
C:\Windows\System32\drivers\etc>type hosts
[...]
1.1.1.1 b2.hello.vous
```

- prouvez avec un `ping b2.hello.vous` que ça ping bien `1.1.1.1`

```bash
C:\Users\maelf>ping b2.hello.vous

Pinging b2.hello.vous [1.1.1.1] with 32 bytes of data:
Reply from 1.1.1.1: bytes=32 time=37ms TTL=57
Reply from 1.1.1.1: bytes=32 time=43ms TTL=57
Reply from 1.1.1.1: bytes=32 time=11ms TTL=57
Reply from 1.1.1.1: bytes=32 time=11ms TTL=57

Ping statistics for 1.1.1.1:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 11ms, Maximum = 43ms, Average = 25ms
```

---

☀️ **Go mater une vidéo youtube et déterminer, pendant qu'elle tourne...**

- l'adresse IP du serveur auquel vous êtes connectés pour regarder la vidéo
- le port du serveur auquel vous êtes connectés
- le port que votre PC a ouvert en local pour se connecter au port du serveur distant

---

☀️ **Requêtes DNS**

Déterminer...

- à quelle adresse IP correspond le nom de domaine `www.ynov.com`

```bash
C:\Users\maelf>nslookup www.ynov.com
Server:  dns.google
Address:  8.8.8.8

Non-authoritative answer:
Name:    www.ynov.com
Addresses:  2606:4700:20::681a:be9
          2606:4700:20::ac43:4ae2
          2606:4700:20::681a:ae9
          104.26.10.233
          104.26.11.233
          172.67.74.226
```

- à quel nom de domaine correspond l'IP `174.43.238.89`

```bash
C:\Users\maelf>nslookup 174.43.238.89
Server:  dns.google
Address:  8.8.8.8

Name:    89.sub-174-43-238.myvzw.com
Address:  174.43.238.89
```

---

☀️ **Hop hop hop**

Déterminer...

- par combien de machines vos paquets passent quand vous essayez de joindre `www.ynov.com`

```bash
C:\Users\maelf>tracert www.ynov.com

Tracing route to www.ynov.com [104.26.10.233]
over a maximum of 30 hops:

  1     9 ms     1 ms     1 ms  10.33.79.254
  2     8 ms     3 ms     2 ms  145.117.7.195.rev.sfr.net [195.7.117.145]
  3     5 ms     3 ms     4 ms  237.195.79.86.rev.sfr.net [86.79.195.237]
  4     2 ms     5 ms     3 ms  196.224.65.86.rev.sfr.net [86.65.224.196]
  5    11 ms    11 ms    10 ms  12.148.6.194.rev.sfr.net [194.6.148.12]
  6    61 ms    11 ms    11 ms  12.148.6.194.rev.sfr.net [194.6.148.12]
  7    61 ms   182 ms    12 ms  141.101.67.48
  8    12 ms    13 ms     9 ms  141.101.67.54
  9    19 ms    17 ms    14 ms  104.26.10.233

Trace complete.
```

---

☀️ **IP publique**

Déterminer...

- l'adresse IP publique de la passerelle du réseau (le routeur d'YNOV donc si vous êtes dans les locaux d'YNOV quand vous faites le TP)

```bash
C:\Users\maelf>curl ifconfig.me
195.7.117.146
```

---

☀️ **Scan réseau**

Déterminer...

- combien il y a de machines dans le LAN auquel vous êtes connectés

```bash
C:\Users\maelf>arp -a

Interface: 10.33.76.231 --- 0x6
  Internet Address      Physical Address      Type
  10.33.76.233          f8-b5-4d-43-18-4a     dynamic
  10.33.79.254          7c-5a-1c-d3-d8-76     dynamic
  10.33.79.255          ff-ff-ff-ff-ff-ff     static
  224.0.0.2             01-00-5e-00-00-02     static
  224.0.0.22            01-00-5e-00-00-16     static
  224.0.0.251           01-00-5e-00-00-fb     static
  224.0.0.252           01-00-5e-00-00-fc     static
  224.0.1.60            01-00-5e-00-01-3c     static
  239.255.255.250       01-00-5e-7f-ff-fa     static
  255.255.255.255       ff-ff-ff-ff-ff-ff     static
```

# III. Le requin

Faites chauffer Wireshark. Pour chaque point, je veux que vous me livrez une capture Wireshark, format `.pcap` donc.

Faites *clean* 🧹, vous êtes des grands now :

- livrez moi des captures réseau avec uniquement ce que je demande et pas 40000 autres paquets autour
  - vous pouvez sélectionner seulement certains paquets quand vous enregistrez la capture dans Wireshark
- stockez les fichiers `.pcap` dans le dépôt git et côté rendu Markdown, vous me faites un lien vers le fichier, c'est cette syntaxe :

---

☀️ **Capture ARP**

- 📁 fichier `arp.pcap`
- capturez un échange ARP entre votre PC et la passerelle du réseau

Filtre "arp"

[Lien vers capture ARP](./captures/arp.pcapng)

---

☀️ **Capture DNS**

- 📁 fichier `dns.pcap`
- capturez une requête DNS vers le domaine de votre choix et la réponse
- vous effectuerez la requête DNS en ligne de commande

Filtre "dns"

[Lien vers capture DNS](./captures/dns.pcapng)

---

☀️ **Capture TCP**

- 📁 fichier `tcp.pcap`
- effectuez une connexion qui sollicite le protocole TCP
- je veux voir dans la capture :
  - un 3-way handshake
  - un peu de trafic
  - la fin de la connexion TCP

> Si vous utilisez un filtre Wireshark pour mieux voir ce trafic, précisez-le moi dans le compte-rendu.

---