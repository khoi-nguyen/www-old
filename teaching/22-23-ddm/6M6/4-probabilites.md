---
title: Probabilités
output: revealjs
...

# Probabilités {.split}

Catégorie d'épreuve
:   Ensemble des résultats possibles

Événement
:   Sous-ensemble de $\Omega$

\begin{align*}
\text{Événement certain} = \Omega\\
\text{Événement impossible} = \emptyset\\
\end{align*}

Deux événements $A, B \subset \Omega$ sont

- **incompatibles** si $A \cap B = \emptyset$.
- **contraires** si $A = \Omega \setminus B$.

::: remark
- L'événement contraire de $A$ est noté $\overline A$.
:::

# Exercices {.split}

![](/static/images/1679902658.png)


# Probabilité: définition {.split}

::: {.definition title="Définition"}
Soit $\Omega$ une catégorie d'épreuve avec un nombre **fini** d'éléments.

Une probabilité est une fonction
\begin{align*}
\P : \Omega \to [0, 1]
\end{align*}
telle que
\begin{align*}
\sum_{\omega \in \Omega} \P(\omega) = 1.
\end{align*}

Ensuite, pour chaque sous-ensemble $A$, on définit
\begin{align*}
\P(A) \defeq \sum_{\omega \in A} P(\omega)
\end{align*}
:::

# Propriétés des probabilités {.split}

::: proposition
Soient deux événements $A, B \subset \Omega$.

- $\P(\emptyset) = 0$, $\P(\Omega) = 1$
- On a
\begin{align*}
\P(A \cup B) = \P(A) + \P(B) - \P(A \cap B)
\end{align*}
- En particulier, si $A$ et $B$ sont incompatibles, on a
\begin{align*}
\P(A \cup B) = \P(A) + \P(B)
\end{align*}
- $\P(\overline A) = 1 - \P(A)$.
:::

# Diagramme de Venn {.split}

![](/static/images/1679902841.png)

# Arbre {.split}

![](/static/images/1679902919.png)

# Tableaux à double entrée {.split}

![](/static/images/1679902809.png)

# À votre tour {.split}

![](/static/images/1679902963.png)

![](/static/images/1679902996.png)

# Exercices {.split}

![](/static/images/1679903030.png)
![](/static/images/1679903069.png)

# Probabilité conditionnelle {.split}

::: {.definition title="Probabilité conditionnelle"}
La probabilité de $A$ *si* $B$ est donnée par
\begin{align*}
\P(A | B) \defeq \frac {\P(A \cap B)} {\P(B)}
\end{align*}
:::

::: remark
Il est préférable, si possible, de juste se restreindre
aux possibilités qui satisfont $B$.
:::

![](/static/images/1680069286.png)
![](/static/images/1680069319.png)

# Indépendance {.split}

::: definition
On dit que $A$ et $B$ sont indépendants si
\begin{align*}
\P(A | B) = \P(A)
\quad \text{et} \quad
\P(B | A) = \P(B).
\end{align*}
:::

En pratique, on utilise le critère suivant.

::: proposition
$A$ et $B$ sont indépendants si et seulement si
\begin{align*}
\P(A \cap B) = \P(A) \P(B).
\end{align*}
:::

![](/static/images/1680069612.png)

# Probabilité: définition continue {.row}

::::: {.col}
::: {.definition title="Probabilité"}
Soit $\Omega$ une catégorie d'épreuve avec un nombre **fini** d'éléments.

Une **probabilité** est une fonction
\begin{align*}
\P : \Omega \to [0, 1]
\end{align*}
telle que
\begin{align*}
\sum_{\omega \in \Omega} \P(\omega) = 1.
\end{align*}

Ensuite, pour chaque sous-ensemble $A$, on définit
\begin{align*}
\P(A) \defeq \sum_{\omega \in A} P(\omega)
\end{align*}
:::
:::::

::::: {.col}
::: {.definition}
Soit $\Omega = \R$.

Une **densité de probabilité** est une fonction
\begin{align*}
f: \R \to \R^+
\end{align*}
telle que
\begin{align*}
\int_{-\infty}^{+\infty} f(x) \dd x = 1.
\end{align*}

Pour chaque intervalle $A = [a, b]$, on définit
\begin{align*}
\P(A) \defeq \int_a^b f(x) \dd x.
\end{align*}
:::
:::::
