---
title: Intégrales
output: revealjs
notes: |
  - 15/01: Introduction à l'intégration
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

# Introduction: calcul d'aire sous $x^2$ {.split}

::::: {.col}
::: task
Calculons l'aire sous la fonction $f(x) = x^2$
entre $0$ et $1$.
:::

~~~ {.javascript .jsxgraph .fragment}
const f = x => x ** 2;
board.boundingbox = [-0.4, 1.2, 1.2, -1.2];
let n = board.slider([-0.2, 0.6], 0.6, [5, 10, 30]);
board.riemannSum(f, () => n.Value(), 0, 1, "right");
board.plot(f)
~~~

::: fragment
Nous aurons besoin de la formule

$$\sum_{i = 1}^n i^2 = \frac {n (n + 1) (2n + 1)} 6$$
:::
:::::

# Introduction: calcul d'aire sous $e^x$ {.split}

::: task
Calculons l'aire sous la fonction $f(x) = e^x$
entre $0$ et $1$.
:::

# Introduction: calcul de $\pi$ à l'ordinateur {.row}

::::: {.col}
~~~ {.julia .plot}
x = 0:0.001:1
y = @. sqrt(1 - x^2)
plot(x, y, aspect_ratio=:equal, framestyle=:origin)
~~~
:::::

::::: {.col}
~~~ julia
# La fonction dont on cherche à calculer l'aire, càd le quart de cercle
f(x) = √(1 - x^2)

# Le nombre d'intervalles qu'on utilisera
n = 1000000

# x est un ensemble de n points équidistants entre 0 et 1
x = range(0, 1, length=n)

# On approxime l'aire du quart du disque
aire = sum(1/n * f.(x))

# On multiplie par 4 pour avoir l'aire du disque
4 * aire
~~~
:::::

# La méthode de Monte-Carlo {.row}

::::: {.col}
![](https://upload.wikimedia.org/wikipedia/commons/8/84/Pi_30K.gif)
:::::

::::: {.col}
::: {.idea .fragment}
On estime l'aire rouge sous la courbe $\frac \pi 4$ via

$$\frac {\pi} 4 = \frac {\text{nombre de points rouge (n)}} {\text{nombre total de points (N)}}$$
:::

~~~ {.python .fragment}
import random

n = 0 # Nombre de points rouges
N = 0 # Nombre total de points

# Répète indéfiniment:
while True is True:
    # Choisis un point (x, y) dans le carré
    x = random.uniform(0, 1)
    y = random.uniform(0, 1)

    # Si on est dans la zone rouge...
    if x ** 2 + y ** 2 < 1:
        n += 1

    # Dans tous les cas, on a ajouté un point
    N += 1

    print("Notre estimation de pi est", 4 * n / N)
~~~
:::::

# Un peu d'histoire {.row}

::::: {.col}
- Antiquité: essayent de calculer des aires (très long)
- 1666: Newton découvre ??? qui lui permet de calculer l'aire très facilement.
  Grâce à sa découverte, il a ensuite
  - écrit les lois du mouvement
  - découvert la loi universelle de la gravitation
  - fait des avancées en optique (mais ce n'est pas lié)
- Cette théorie mathématique de Newton a mis presque 3 siècles à être
  correctement formalisée.

::: {.block title="Enstein à propos de Newton"}
In order to put his system into mathematical form at all,
Newton had to devise the concept of ???
and propound the laws of motion in the form of ??? -- perhaps
the **greatest advance in thought**
that a single individual was ever privileged to make.
:::
:::::

::::: {.col}
![](/static/images/1673833978.png)
:::::

# Intégrale et aire

![](/static/images/1673835767.png)

L'intégrale est la quantité:
$$-A_1 + A_2 - A_3 + A_4$$

Les aires des portions où la fonction est **négative**
sont soustraites.

# Application de l'intégrale: la moyenne {.split}

::: proposition
Soit $f$ une fonction continue définie sur $[a, b]$.

La moyenne de $f$ est donnée par
$$\text{moyenne} = \frac {\text{intégrale}} {\text{longueur de l'intervalle}}$$
:::

::: {.remark .fragment}
Étant donné qu'une **moyenne peut être négative**,
ce résultat n'est possible que parce que l'intégrale peut être négative.
:::

# Définition: l'intégrale {.split}

::: {.definition title="Intégrale"}
Soit $f$ une fonction continue sur $[a, b]$.
L'intégrale de $f$ sur $[a, b]$, dénotée $\int_a^b f(x) \dd x$, est la limite

$$\int_a^b f(x) \dd x = \lim_{n \to \infty} \sum_{i = 1}^n f(x_i) \Delta x,
\quad \text{où }
\begin{cases}
\Delta x &= \frac {b - a} n\\
x_i &= a + i \Delta x
\end{cases}.$$
:::

::: remark
Nous admettrons que la limite existe,
et que l'on peut considérer des divisions de $[a, b]$ non équidistantes
et choisir le point $x_i$ plus librement.
:::

# Propriétés de l'intégrale indéfinie {.split}

![](/static/images/1673859961.png)

# Propriétés de l'intégrale indéfinie {.split}

![](/static/images/1673859988.png)

# Propriétés de l'intégrale indéfinie: exercices {.split}

![](/static/images/1673859537.png){width=100%}

# L'idée de Newton

::: {.block title="Citation (Isaac Newton)"}
I consider mathematical quantities in this place not as consisting of parts;
but as described by a **continued motion**.
Lines are described, and thereby generated not by the apposition of parts,
but by the continued motion of points;
**surfaces by the motion of lines**;
Solids by the motion of surfaces;
Angles by the rotation of the sides; Portion of time by a continual flux: and so in other quantities. These geneses really take place in nature of things, and are daily seen in the motion of bodies. And after this manner the ancients, by drawing moveable right lines along immoveable right lines taught the genesis of reflection...
:::

~~~ {.yaml .widget name="geogebra"}
url: https://www.geogebra.org/m/tcgmvhje
~~~

# L'intégrale indéfinie {.split}

::: {.definition title="Intégrale indéfinie"}
Soit $f$ une fonction continue sur $[a, b]$.
Une fonction de la forme
$$F(x) = \int_c^x f(t) \dd t$$
est appelée **intégrale indéfinie** de $f$.
:::

::: {.proposition title="Flux"}
Notons que
$$F(b) - F(a) = \int_a^b f(t) \dd t$$
:::

# Théorème fondamental de l'analyse {.split}

::: {.theorem title="Théorème fondamental de l'analyse, partie I"}
Soit $f$ une fonction continue sur $[a, b]$.
L'intégrale indéfinie

$$F(x) = \int_a^x f(t) \dd t$$

satisfait $F' = f$.
:::

::: {.theorem .fragment title="Théorème fondamental de l'analyse, partie II"}
Soit $f$ une fonction continue sur $[a, b]$
Si $F$ satisfait $F' = f$, alors
$$\int_a^b f(x) \dd x = F(b) - F(a).$$
:::

Aire et dérivées sont des opérations inverses!

# Primitives {.split}

::: {.definition .fragment}
Soit $F$ une fonction dérivable sur $[a, b]$.
On dit que $F$ est une **primitive** de $F'$.
:::

# Vérifier que c'est une primitive {.split}

![](/static/images/1673859464.png){width=100%}

# Primitive et non-unicité {.split}

::: {.definition .fragment}
Soit $F$ une fonction dérivable sur $[a, b]$.
On dit que $F$ est une **primitive** de $f = F'$.
:::

Généralement, la primitive n'est **pas unique**.

Par exemple, $\frac {x^3} 3 + 3$ et $\frac {x^3} 3$
sont des primitives de $x^2$.

On notera

$$\int x^2 \dd x = \frac {x^3} 3 + c$$

# Primitives de fonctions usuelles

Primitiver c'est l'opération inverse de la dérivation.

![](/static/images/1673858086.png){width=100%}
