---
title: Informatique
output: revealjs
kernel: python
...

# Google Colab

Vous aurez besoin d'un **compte Gmail**.

<https://colab.research.google.com>

::: info
Google Colab vous permet de programmer sans rien installer sur votre ordinateur.
Le code est effectué sur un ordinateur de google
qui ensuite vous renvoie le résultat.
:::

# Rappels

- `input`: permet à l'utilisateur d'entrer du texte et retenir le résultat
- `print`: affiche à l'écran
- `float`: convertit en nombre à virgule

~~~ {.python .jupyter}
longueur = float(input("Entrer la longueur"))
largeur = float(input("Entrer la largeur"))
aire = longueur * largeur

print("L'aire est", aire)
~~~

::: check
- Pourquoi nous devons employer la commande `float`?
- Pourquoi utilisons-nous parfois des guillemets et parfois pas?
:::

# Conditions

::::: {.col}

::: info
Les instructions `if` (si), `elif` (*else if*, sinon si) et `else` (sinon)
execute les instructions indentées
si la condition qui suit (impérativement terminée par un `:`)
est vraie.
L'égalité se vérifie avec le double égal `==`.
:::

~~~ {.python .jupyter}
age = float(input("Quel âge avez-vous?"))
if age > 65:
    print("Que faites-vous dans une école?")
elif age > 21:
    print("Vous êtes enseignant")
else:
    print("Vous êtes un élève")
~~~

::: exercise
Ecrire un code qui calcule les longueurs d'arc $L = \text{angle en rad} \times \text{rayon}$.
Demander préalablement si l'angle est en degrés ou en radians.
:::

:::::

::::: {.col}

::: check
- Pourquoi doit-on distinguer `==` et `=`?
:::

~~~ {.python .jupyter}
from math import pi # pour avoir une variable pi
rayon = float(input("Quel est le rayon du cercle?"))
angle = float(input("Quel est l'amplitude?"))
unité = input("'radians' ou 'degrés' ?")

# À vous de continuer
~~~

:::::

# Solution de l'exercice {.split}

~~~ {.python .jupyter}
from math import pi
rayon = float(input("Quel est le rayon du cercle?"))
angle = float(input("Quel est l'amplitude?"))
unité = input("'radians' ou 'degrés' ?")

# Convertir en radians si nécéssaire
if unité == "degrés":
    angle = angle * pi / 180

L = rayon * angle
~~~

# Répéter des instructions

::::: {.col}

::: info
Pour répéter des instructions, on emploie `for`.
Attention aux deux points (`:`),
et à l'indentation nécéssaire

~~~ {.python .jupyter}
for i in range(10):
    print("Bonjour", i, "fois")
    print("Cette instruction est répétée")
print("Cette instruction n'est pas répétée car non indentée")
~~~
:::

:::::

::::: {.col}

::: exercise
- Afficher la table de multiplications de $7$
- Afficher toutes les tables de multiplications de $1$ à $10$
:::

~~~ {.python .jupyter}
# Écrire le code ici
~~~
:::::

# Nombres triangulaires

::::: {.col}
::: exercise
Afficher $1000$ termes de la suite $1, 3, 6, 10, 15, \dots$ (nombres triangulaires)
:::
:::::

::::: {.col}
~~~ {.python .jupyter}
7 % 3
~~~
:::::

# Fibonacci

::::: {.col}
::: exercise
Afficher $1000$ termes de la *suite de Fibonacci*
\begin{align*}
1, 1, 2, 3, 5, 8, \dots
\end{align*}
En déduire une approximation du *nombre d'or*.
:::
:::::

::::: {.col}
~~~ {.python .jupyter}
7 % 3
~~~
:::::

# Fizzbuzz

::::: {.col}
::: exercise
Afficher les nombres de $1$ à $100$.

- Si le nombre est divisible par $3$, écrire "fizz" à la place
- Si le nombre est divisible par $5$, écrire "buzz" à la place
- Si le nombre est divisible par $3$ et par $5$, afficher "fizzbuzz"
:::

Indice: l'opérateur $\%$ retourne le reste de la division.
:::::

::::: {.col}
~~~ {.python .jupyter}
7 % 3
~~~
:::::
