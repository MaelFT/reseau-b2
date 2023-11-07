# III. COMPUTE

**Dans cette partie, on va ajouter une "vrai" fonctionnalité au serveur : résoudre des opérations arithmétiques que le client lui envoie.** Coder une calculette réseau quoi. Ca c'est une folie dis-donc. Encore une fois, on y va petit à petit pour introduire les nouvelles notions une à une.

> *Puis plus tu dév, plus t'es bon. La répétition fait le travail. Et le fait de se creuser la tête sur des problèmes de merde une fois, c'est les résoudre instantanément toutes les fois suivantes.*

DONC dans cette partie, on va faire évoluer simplement le serveur pour qu'il résolve des opérations arithmétiques simples que lui envoie le client.

**Par exemple**, si le client envoie au serveur `2 + 2`, alors le serveur répondra `4`.

![Maths.](../img/compute.jpg)

🌞 **`bs_client_III.py`**

- doit générer des logs
- demande au client de saisir une opération arithmétique
- ajoutez du contrôle (expression régulière) pour ne tolérer que :
  - additions, soustractions, multiplications
  - des nombres entiers compris entre -100000 et +100000

🌞 **`bs_server_III.py`**

- doit générer des logs
- récupérez le code de `bs_server_II2A.py` si vous voulez mais enlevez tout ce qui est en rapport avec les meos et les wafs, on fait une calculette ici !
- la string qu'envoie le client, il faut l'interpréter comme un calcul pour stocker le résultat dans une variable
- en Python y'a par exemple la fonction native `eval()` qui permet de faire ça

```python
>>> client_request = "3 + 3"
>>> result = eval(client_request)
>>> print(result)
6
```

