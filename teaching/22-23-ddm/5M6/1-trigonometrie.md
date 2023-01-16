---
title: Fonctions trigonométriques
output: revealjs
notes: |
  - 15/01: Rappel sur la trigonométrie, radians et longueur d'arc
...

# Bonjour à tous! {.row}

::::: {.col}
::: info
- **Nom**: M. Nguyen
- **Notes de cours**:
  - disponibles sur <https://nguyen.me.uk>
  - avec annotations faites durant le cours
:::
:::::

::::: {.col .fragment}
<iframe data-src="index.html" width="100%" height="500">
</iframe>
:::::

# Trigonométrie (3ème année)

::: text-center
![](/static/images/1673820271.png){height=400}
:::

# Trigonométrie (4ème année) {.row}

::::: col
~~~ {.yaml .widget name="geogebra"}
url: https://www.geogebra.org/m/SQXdnzAe
~~~
:::::

::::: {.col .fragment}
::: remark
- On étend $\sin$, $\cos$, $\tan$ aux angles **obtus**, **négatifs**, etc.
- Les fonctions trigonométriques sont **périodiques** et permettent de décrire
  les mouvements **circulaires**.
- Connaissez-vous les **radians**? À quoi servent-ils?
:::
:::::

# Trigonométrie dans la "vie réelle" {.row}

::::: {.col}
<iframe data-src="https://www.myfourierepicycles.com/" width="100%" height="900">
</iframe>
:::::

::::: {.col .fragment}
::: info
- **Mathématiquement**,
  pratiquement **toutes les fonctions** peuvent s'écrire en terme de $\sin$, $\cos$
  (théorie de Fourier)
- D'un point de vue de la **physique**,
  beaucoup de phénomènes sont **ondulatoires**
  (électromagnétisme, physique quantique, etc.)
- La **tangente** est la meilleure manière de mesurer l'**inclinaison** d'une droite.
  Cela mènera Newton et Leibniz au calcul différentiel et intégral.
:::

::: {.info title="MP3 et JPEG" .fragment}
La **compression** des fichiers images et audio utilisent cette "décomposition circulaire".

- Au plus de cercles on emploie, au plus la reproduction est fidèle,
- Si l'on emploie moins de cercles, le fichier sera plus léger.
:::

::: fragment
En d'autres termes,
les triangles ne sont qu'une application peu importante dans les mathématiques modernes.
:::
:::::

# Arcs de cercle {.split}

::::: col
::: text-center
![](/static/images/1673820564.png)
:::

::: proposition
La longueur d'un arc de cercle de rayon $r$
sous-tendu par un angle $\alpha$ (en **degrés**) est donnée par
$$L = \frac \pi {180} \cdot \alpha \cdot r.$$
:::
:::::

# Aire de secteur {.split}

::::: col
::: text-center
![](/static/images/1673820564.png)
:::

::: proposition
L'aire d'un secteur circulaire de rayon $r$
sous-tendu par un angle $\alpha$ (en **degrés**) est donnée par
$$A = \frac \pi {360} \cdot \alpha \cdot r^2.$$
:::
:::::

# Parenthèse: comment fonctionne la calculatrice?

Pour calculer la fonction $\sin(x^{\circ})$,
la calculatrice utilise la formule

~~~ {.python .eval}
series(sin(x), x=x, x0=0, n=10).subs(x, pi / 180 * x)
~~~

Par exemple, en remplaçant $x$ par $0,1$ dans la formule ci-dessus,
on obtient
`series(sin(x), x=x, x0=0, n=10).removeO().subs(x, pi / 180 * 0.1).evalf()`{.python .eval}.

En posant $y = \frac {\pi} {180} \cdot x$,
on obtient la formule:

~~~ {.python .eval}
series(sin(y), x=y, x0=0, n=10)
~~~

::: {.info .fragment}
Les formules deviennent nettement plus facile
si on multiplie les angles en degrés par $\frac \pi {180}$.
:::

# Radians {.row}

::::: {.col}
::: {.definition title="Angle en radian"}
Soit un angle dont la mesure en degré est $x_{\text{deg}}$.
Sa mesure en **radians** $x_\text{rad}$ est donnée par
$$x_\text{rad} = \frac {\pi} {180} \cdot x_{\text{deg}}.$$
:::

::: fragment
Contrairement au degré, le radian s'écrit par convention **sans unité**.
:::

::: fragment
Si $\alpha$ est en **radians**,

- *Longueur d'arc*: $L = \alpha r$
- *Aire de secteur*: $A = \frac {\alpha} 2 r^2.$
:::
:::::

::::: {.col}
::: {.exercise .fragment}
Convertir les mesures d'angles suivantes:

 Degrés              Radians
--------            ---------
 $0^\circ$
 $30^\circ$
                     $\frac \pi 4$
                     $1$
 $60^\circ$
 $90^\circ$
 $180^\circ$
 $270^\circ$
 $360^\circ$
:::
:::::

# Exercices {.split}

![](/static/images/1673825352.png){width=100%}

# Interprétation du radian

::::: col

Rappelons que nous avons $L = \alpha r$.

Dans le cercle trigonométrique ($r = 1$),
l'amplitude en radians correspond exactement à la longueur d'arc $L = \alpha$.

~~~ {.yaml .widget name="geogebra"}
url: https://www.geogebra.org/m/SQXdnzAe
~~~

L'angle en radians est **naturel** car ...
:::::

# Exercices: arcs et secteurs {.split}

Formule                Degrés                                   Radians
--------               -------                                  --------
Longueur d'arc         $L = \frac {\pi} {180} \alpha r$         $L = \alpha r$
Aire de secteur        $A = \frac {\pi} {360} \alpha r^2$       $A = \frac \alpha 2 r^2$

![](/static/images/1673825546.png){width=100%}

# Problème: arcs et secteurs {.split}

![](/static/images/1673866837.png){width=100%}

# Problème 2: arcs et secteurs {.split}

![](/static/images/1673867014.png){width=100%}

# Problème 3: arcs et secteurs

![](/static/images/1673867176.png){width=100%}

# La fonction $x \mapsto \sin x$ {.row}

::::: {.col}
~~~ {.yaml .widget name="geogebra"}
url: https://www.geogebra.org/m/Faf7wbhV
~~~
:::::

::::: {.col}
![](/static/images/1673826402.png){width=100% .fragment}

![](/static/images/1673826676.png){width=100% .fragment}
:::::

# La fonction $x \mapsto \cos x$ {.row}

::::: {.col}
~~~ {.yaml .widget name="geogebra"}
url: https://www.geogebra.org/m/VqR8KxDW
~~~
:::::

::::: {.col}
![](/static/images/1673826945.png){width=100% .fragment}

![](/static/images/1673827044.png){width=100% .fragment}
:::::

# La fonction $x \mapsto \tan x$ {.row}

::::: {.col}
~~~ {.yaml .widget name="geogebra"}
url: https://www.geogebra.org/m/tpfebt9w
~~~
:::::

::::: {.col}
![](/static/images/1673827399.png){width=100% .fragment}
:::::

# Caractéristiques de $\tan x$

![](/static/images/1673827535.png)

# Exercice: associer l'expression au graphique

![](/static/images/1673828065.png){width=75%}

![](/static/images/1673828098.png){width=75%}

# Graphe de $x \mapsto a \sin(b(x - c) + d$

$$f(x) = a \sin(b(x - c)) + d$$

~~~ {.yaml .widget name="geogebra"}
url: https://www.geogebra.org/m/QgE48Y5j
~~~

# Graphe de $x \mapsto a \sin(bx + c) + d$

![](/static/images/1673827851.png)

# Exercice {.split}

![](/static/images/1673866723.png){width=100%}

# Exemple

Tracer le graphe de $f(x) = 3 \sin\left(2 \left(x + \frac \pi 8\right)\right) + 1$.

![](/static/images/1673865621.png){width=80%}

# Exercices

![](/static/images/1673865849.png){height=100%}

# Trouver l'équation analytique depuis un graphe {.split}

![](/static/images/1673866353.png){width=100%}

# Exercices

![](/static/images/1673866268.png)

# Problème: trouver l'équation analytique

![](/static/images/1673868777.png){width=50%}

# Problème 2: trouver l'équation analytique

![](/static/images/1673868856.png)

# Problème 3: trouver l'équation analytique

![](/static/images/1673868894.png)
