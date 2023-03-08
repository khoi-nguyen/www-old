---
title: "Intégrales: applications"
output: revealjs
...

# Rappel: théorème fondamental {.split}

$$\int_a^b f(x) \dd x$$

::: theorem
L'intégrale indéfinie est une primitive:
$$\left(\int_c^x f(t) \dd t\right)' = f(x)$$

Les intégrales
$$\int_a^b f'(x) \dd x = \left[\int_a^b f(x) \dd x\right]_a^b$$
:::

# Énergie potentielle et mécanique {.split}

::: {.definition title="Énergie potentielle"}
Si une force ne dépend $F$ que de la position et pas du temps,
on définit l'**énergie potentielle** via

$$V(x) = - \int_c^x F(y) \dd y$$
:::

::: {.theorem title="Conservation de l'énergie"}
La quantité:

$$E(t) = \underbrace{\frac 1 2 m \left(\frac {\dd x}{\dd t}\right)^2}_{\text{énergie}\ \text{cinétique}} + V(x(t))$$

est constante au cours du temps.
:::

# Aire et changements de signe {.split}

::: example
Calculer l'aire comprise entre $f(x) = \sin x$ et l'axe $Ox$
entre $-\frac \pi 2$ et $\frac {3 \pi} 2$.

![](/static/images/1675934794.png){width=100%}
:::

# Aire entre deux fonctions {.split}

![](/static/images/1675935044.png){width=100%}

# Exemple: aire du cercle {.split}

~~~ {.julia .plot}
x = 0:0.01:1
f(x) = √(1 - x^2)
plot(x, f.(x), aspect_ratio = :equal, framestyle = :origin, label=L"\sqrt{1 - x^2}")
~~~

::: {.exampleblock title="Aire du cercle"}
$$A = 4 \int_0^r \sqrt{r^2 - x^2} \dd x$$
:::

# Un petit peu de musique {.row}

::::: {.col}
Supposons qu'on presse $3$ notes sur un clavier

$$f(t) = c_1 \sin(f_1 t) + c_2 \sin(f_2 t) + c_3 \sin(f_3 t),$$

où $f_1, f_2, f_3$ sont entières.

~~~ {.julia .plot}
x = 0:0.01:2*π
f(x) = 2 * sin(x) + sin(2 * x) + 0.5 * sin(3 * x)
plot(x, f.(x), label=L"f(t)", framestyle=:origin)
~~~

Quelles sont les notes et à quel volume sont-elles jouées?

::: {.theorem title="Orthogonalité"}
$$\int_{-\pi}^{\pi} \sin(mx) \sin(nx) \dd x =
\begin{cases}
0 & \text{if } m \neq n\\
\pi & \text{if } m = n.
\end{cases}$$
:::
:::::

::::: {.col}
$$\sin a \sin b = \frac {\cos (a - b) - \cos ( a + b)} 2$$
:::::

# Exercices {.split}

![](/static/images/1675935156.png){width=100%}

# Exercices avec paramètres {.split}

![](/static/images/1676277671.png){width=100%}

# Exercices d'aire {.split}

![](/static/images/1676277863.png){width=100%}

# Exercices d'aire {.split}

![](/static/images/1676277935.png)

# Volumes de revolution {.split}

![](/static/images/1676278281.png){width=100%}

![](/static/images/1676278472.png)

# Exercices sur les volumes de révolution {.split}

![](/static/images/1676279000.png){width=100%}

# Exercices sur les volumes de révolution {.split}

![](/static/images/1676318711.png){width=100%}

# MRU, MRUA

::: question
Calculer

$$v(t) = v_0 + \int_{t_0}^t a \dd x.$$
$$x(t) = x_0 + \int_{t_0}^t v(x) \dd x.$$
:::

# Longueur d'arc de cercle {.split}

![](/static/images/1676560803.png)

# Exercices: longueur d'arc de courbe {.split}

![](/static/images/1676318762.png){width=100%}

# Rappels {.split}

\begin{align}
\int_a^b f(x) \dd x
= \left[\int f(x) \dd x\right]_a^b
\end{align}

\begin{align}
\text{Aire} = \int_a^b \text{haut}(x) - \text{bas}(x) \dd x.
\end{align}

\begin{align}
\text{Volume} = \pi \int_a^b \underbrace{f^2(x)}_{r^2} \underbrace{\dd x}_h
\end{align}

\begin{align}
\text{Longueur d'arc} = \int_a^b \sqrt { 1 + (f'(x))^2 } \dd x
\end{align}

# Transférer 1 {.split}

![](/static/images/1676318845.png){width=80%}
![](/static/images/1676318866.png){width=80%}

# Transférer 2 {.split}

![](/static/images/1676318973.png){width=80%}

# Transférer 3 {.split}

![](/static/images/1676319095.png){width=80%}

# Transférer 4 {.split}

![](/static/images/1676319171.png){width=100%}

# Transférer 5 {.split}

![](/static/images/1676319195.png){width=80%}
![](/static/images/1676319206.png){width=80%}

# Transférer 6 {.split}

![](/static/images/1676319227.png){width=80%}

# Exercice 39 {.split}

![](/static/images/1678142479.png)
![](/static/images/1678142591.png)

# Exercice 40 {.split}

![](/static/images/1678142618.png){width=80%}

# Exercice 41 {.split}

![](/static/images/1678142650.png){width=100%}

# Exercice 42 {.split}

![](/static/images/1678142678.png){width=100%}

# 8 mars {.row}

::::: {.col}

### Aujourd'hui

- Note à moi-même: terminer la correction de l'exercice $42$.
- Interrogation le $21$ mars sur les intégrales
- Demain: probabilités

### Applications des intégrales

\begin{align*}
\int_a^b f(x) \dd x
= \left[\int f(x) \dd x\right]_a^b
\end{align*}

\begin{align*}
\text{Aire} = \int_a^b \text{haut}(x) - \text{bas}(x) \dd x.
\end{align*}

\begin{align*}
\text{Volume} = \pi \int_a^b \underbrace{f^2(x)}_{r^2} \underbrace{\dd x}_h
\end{align*}

\begin{align*}
\text{Longueur d'arc} = \int_a^b \sqrt { 1 + (f'(x))^2 } \dd x
\end{align*}

\begin{align*}
\text{Moyenne} = \frac 1 {b - a} \int_a^b f(x) \dd x.
\end{align*}

:::::

::::: {.col}

### Journée internationale des femmes

Ada Lovelace
:   A écrit le premier programme informatique

Emmy Noether (physique mathématique)
:   Conservation de l'énergie provient de l'invariance du temps sous les translations.

Maryam Mirzakhani (topologie et géométrie)
:   Première femme à recevoir la médaille Fields (2014)
:::::

# Questions d'examen d'entrée {.split}

::: {.question title="ULB, Juillet 1999"}
#. Calculer l'aire entre les courbes
\begin{align}
y = 1 + x^2, \qquad y = 9 - x^2
\end{align}
#. Calculer le volume du solide engendré par la rotation de cette surface autour de l'axe $Ox$.
:::

Si vous avez fini...

::: {.question title="Examen d'entrée d'Oxford, 2018"}
La trompette de Torricelli est obtenue
par la rotation de $$y = \frac 1 x$$ entre $1$ et $+\infty$.

- Montrer que la trompette de Torricelli a un volume **fini**.
  (Indication: calculer entre $1$ et $a$, où $a$ est "grand").
- (Difficile) Montrer que la surface extérieure est infinie.
:::

# Exercice 40 {.split}

![](/static/images/1678142618.png){width=80%}

# Exercice 43 {.split}

![](/static/images/1678142693.png){width=100%}

::: {.exampleblock title="Question supplémentaire de réflexion"}
Utiliser le calcul intégral pour calculer le volume d'une pyramide.
:::

# Du baccalauréat britannique

![](/static/images/1678258484.png)

# Du baccalauréat britannique

![](/static/images/1678259040.png)

# Exercices supplémentaires {.row}

::::: {.col}
<iframe src="https://www.bibmath.net/ressources/index.php?action=affiche&quoi=bde/analyse/integration/integration-calcul&type=fexo" width="100%" height=900></iframe>
:::::

::::: {.col}
À pouvoir faire: 1, 2, 3, 4, 5, 6, 7, 9, 10(1), 12, 17, 18, 19, 22,
25, 26, 27, 28, 29, 33, 34, 37, 38
:::::
