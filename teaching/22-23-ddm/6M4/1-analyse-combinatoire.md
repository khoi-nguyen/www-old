---
title: Analyse combinatoire
output: revealjs
notes: |
  - 13/01: début de l'analyse combinatoire
...

# Exploration: introduire un code {.split}

![](/static/images/1673567176.png){width=100%}

# Exploration: anagrammes {.split}

![](/static/images/1673567352.png){width=100%}

# Exploration: former des équipes {.split}

![](/static/images/1673567431.png){width=100%}

# Arrangements simples {.row}

::::: {.col}
::: {.definition title="Arrangements simples"}
Un **arrangement simple** est un **choix ordonné sans répétitions** parmi des éléments **distincts**.
:::

::: {.example .fragment}
- Combien y a-t-il de nombres de quatre chiffres différents
  formés à partir des chiffres $1$, $2$, $5$, $7$, $8$ et $9$.
:::
:::::

::::: {.col}
::: {.definition .fragment title="Arrangements avec répétitions"}
Un **arrangement** est un **choix ordonné avec répétitions** parmi des éléments **distincts**.
:::

::: {.example .fragment}
- Combien y a-t-il de nombres de quatre chiffres
  formés à partir des chiffres $1$, $2$, $5$, $7$, $8$ et $9$?
:::
:::::

# Exercices sur les arrangements {.split}

::: {.exercise}
- Combien y-a-t-il de façons d'assoir 10 personnes sur un banc
  qui ne comporte que 4 places ?
- 12 candidats se présentent aux éléctions
  à un conseil d'administration d'un établissement comportant 8 places.
  La liste des élus est publiée
  par ordre alphabétique.
  Combien y-a-t-il de listes possibles ?
- Combien de nombres de quatre chiffres pairs y a-t-il?
:::

::: {.exercise}
Combien de nombres de quatre chiffres peut-on former dans les cas suivants:

#. Les chiffres peuvent se répéter.
#. Les chiffres ne peuvent pas se répéter.
#. Les chiffres peuvent se répéter
   et les nombres formés sont divisibles par 5.
#. Les chiffres ne peuvent pas se répéter
   et les nombres formés ne contiennent que des chiffres impairs.
:::

# Cas particulier de l'arrangement simple: la permutation simple {.row}

::::: {.col}
::: {.definition title="Arrangements simples"}
Un **arrangement simple** est un **choix ordonné sans répétitions** parmi des éléments **distincts**.
:::

::: fragment
Lorsque l'on prend **tous** les éléments
mais on change l'ordre,
on a un type particulier d'arrangement qu'on appelle **permutation**.
:::

::: {.example .fragment}
- Combien y a-t-il de "mots" de quatre lettres différentes formés avec les lettres A, E, M et R?
- Combien y a-t-il de permutations de l'alphabet?
:::
:::::

::::: {.col}
::: fragment
Ces multiplications sont parfois longues à écrire,
:::

::: {.definition .fragment title="Factorielle"}
$$n! = n \cdot (n - 1) \cdot (n - 2) \dots 3 \cdot 2 \cdot 1$$

$n!$ se lit "$n$ factorielle".
:::
:::::

# Factorielle {.split}

![](/static/images/1673570571.png){width=100%}

# Nombre de permutations {.split}

::: question
Combien y a-t-il d'anagrammes du mot INTERPRETE?
:::

::: warning
Remarquons qu'il y a 3E, 2 R et 2 T.
:::

# Exercices sur les permutations avec répétitions {.split}

::: exercise
Combien existe-t-il d'anagrammes du mot:

- BAOBAB ?
- MISSISSIPI ?
:::

::: {.exercise}
a) Combien y a-t-il de possibilités d’aligner 12 élèves ?
b) A raison de 10 secondes par permutations, combien de temps faudrait-il pour épuiser toutes les
possibilités ?
:::

# Combinaison {.split}

::: definition
Une **combinaison** est un choix (non-ordonné) **sans répétitions** parmi des éléments distincts
:::

::: {.example .fragment}
Combien peut-on former d'équipe de trois personnes à partir d'un ensemble de dix personnes?
:::

# Combinaisons: exercices {.split}

![](/static/images/1673571219.png){width=100%}

# Résumé {.split}

![](/static/images/1673571374.png){width=100%}

# Exercices {.split}

![](/static/images/1673571452.png){width=100%}

# Exercices {.split}

![](/static/images/1673571574.png){height=100%}

# Exercices {.split}

![](/static/images/1673571606.png){height=100%}

# Exercices {.split}

![](/static/images/1673571669.png){height=100%}
