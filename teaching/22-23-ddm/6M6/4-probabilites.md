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
Soit $\Omega$ une catégorie d'épreuve.

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
- En particulier, si $A$ et $B$ son incompatibles, on a
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

