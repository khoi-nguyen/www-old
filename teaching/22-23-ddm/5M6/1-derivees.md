---
title: Dérivées
output: revealjs
...

# La pente {.split}

::: text-center
<!-- Pente = tangente angle -->
![](/static/images/1676631636.png){width=50%}
:::

::: question
Pourquoi utilise-t-on
$$\tan \theta = \frac {\Delta y} {\Delta x}$$
comme mesure d'inclinaison d'une droite?
Pourquoi pas juste $\theta$?
:::

# Pente et croissance {.split}

~~~ {.julia .plot}
x = -5:0.05:5
cste = [4 for x in x]
plot(x, 3x .- 2, label=L"y = 3x + 2", framestyle=:origin)
plot!(x, -2x .+ 1, label=L"y = -2x + 1")
plot!(x, cste, label=L"y = 4")
~~~

Il existe un lien fort entre **pente** et **croissance**.

::: proposition
Soit $f(x) = mx + p$.

- $f$ est **croissante** si et seulement si $m \geq 0$
- $f$ est **décroissante** si et seulement si $m \leq 0$
- $f$ est **constante** si et seulement si $m = 0$
:::

# Pente et opérations de fonction {.split}

- Si $f(x) = mx + p$, notons sa pente $f'$.
- On notera $f \circ g$ la fonction $x \to f(g(x))$

::: proposition
Soient $f(x) = mx + p$ et $g(x) = rx + s$.
On a

\begin{align}
(f \pm g)' = f' \pm g'\\
(f \circ g)' = f' \cdot g'
\end{align}
:::

# Motivations {.split}

- **Généraliser la pente** pour une fonction quelconque $\to$ **dérivée**
- Étudier le lien avec la **croissance**
- Étudier le comportement avec les **opérations de fonctions**

# Einstein à propos de la dérivée {.split}

::::: text-center
![](https://upload.wikimedia.org/wikipedia/commons/3/3b/Portrait_of_Sir_Isaac_Newton%2C_1689.jpg){height=300}
:::::

::: {.quote title="Albert Einstein"}
In order to put his system into mathematical form at all,
Newton had to devise the concept of differential quotients and
propound the laws of motion in the form of total differential 
equations—perhaps the **greatest advance in thought** that a
single individual was ever privileged to make.
:::

1666: Durant un confinement dû à la peste noire à Cambridge,
Newton, âgé de 23 ans, découvre la dérivée, le théorème fondamental de l'analyse,
écrit les lois du mouvement, et énonce la loi de la gravitation universelle.
Il fait également des découvertes importantes en optique.

De mon côté, pendant le confinement,
j'ai essayé d'apprendre à un perroquet madrilène un chant indépendentiste catalan.

# Comment définir la pente en un point? {.row}

::::: {.col}
::: question
Comment définir la pente en un point?
:::

~~~ {.julia .jupyter}
using Plots
x = 0:0.01:0.5
a, b = 0.2, 0.5
f(x) = x^2.5
secant(f, a, b, x) = (f(b) - f(a)) / (b - a) * (x - a) + f(a)
plot(x, f, label="f(x)")
scatter!([a, b], f, label="")
plot!(0.1:0.01:0.45, x -> secant(f, a, b, x), label="sécante")
~~~
:::::

::::: {.col .fragment}
\begin{align}
\lim_{\Delta x \to 0} \frac {\Delta y} {\Delta x}
= \lim_{x \to a} \frac {f(x) - f(a)} {x - a}
\end{align}
:::::

# Nombre dérivé: définition {.split}

::: definition
Une fonction $f$ est **dérivable** en $a$
si la limite
\begin{align}
\lim_{x \to a} \frac {\overbrace{f(x) - f(a)}^{\Delta y}} {\underbrace{x - a}_{\Delta x}}
\end{align}
existe et est réelle.
:::

::: notation
\begin{align}
f'(a) = \lim_{x \to a} \frac {f(x) - f(a)} {x - a}
\end{align}

Notations alternatives: $\frac {\d f} {\d x}$, $\dot f(a)$.
:::

# Nombre dérivé: interpretation {.split}

::: remark
$f'(a)$ représente la pente en $a$
:::

~~~ {.julia .plot}
x = 0:0.01:1
a = 0.4
f(x) = sqrt(x)
g(x, a) = 1/(2 * sqrt(a)) * (x - a) + f(a)
plot(x, f, label=L"f(x)")
plot!(x, x -> g(x, a))
scatter!([a], f, label="(a, f(a))")
~~~

# Pente {.split}

La **dérivée** généralise la **pente**.

::: info
\begin{align}
f'(a) = \lim_{x \to a} \frac {f(x) - f(a)} {x - a}
\end{align}
:::

::: proposition
Si $f(x) = mx + p$, alors $f'(a) = m.$
:::

~~~ {.julia .plot}
x = 0:0.01:2
f(x) = 2*x + 3
plot(x, f, label=L"f(x)")
scatter!([0.3], f, label=L"(a, f(a))")
scatter!([0.5], f, label=L"(x, f(x))")
~~~

# Dérivée de $x^2$ {.split}

::: proposition
Si $f(x) = x^2$, alors $f'(a) = 2 a.$
:::

~~~ {.julia .plot}
x = -2:0.01:2
plot(x, x.^2, label=L"x^2", framestyle=:origin)

x = 0:0.01:2
y = @. 2 * (x - 1) + 1
plot!(x, y, label="tangente")
scatter!([1], [1], label=L"(a, f(a))")
~~~

# Paraboles et croissance {.split}

::: example
Calculer la dérivée et étudier la croissance de

- $f(x) = x^2 - 2x + 3$ (ensemble)
- $g(x) = -x^2 + 3x + 5$ (à faire soi-même)
- $h(x) = ax^2 + bx + c$ (ensemble)
:::

~~~ {.julia .plot .fragment}
x = -2:0.01:4
plot(x, x -> x^2 - 2x + 3, label=L"x^2 - 2x + 3", framestyle=:origin)
~~~

# Dérivée de $x^3$ {.split}

::: proposition
Si $f(x) = x^3$, alors $f'(a) = 3 a^2$
:::

~~~ {.julia .plot}
x = -2:0.01:2
plot(x, x.^3, label=L"x^3", framestyle=:origin)

x = 0:0.01:2
y = @. 3 * (x - 1) + 1
plot!(x, y, label="tangente")
scatter!([1], [1], label=L"(a, f(a))")
~~~

# Étude de fonctions cubiques {.split}

Rappelons que $(x^3)' = 3x^2$ et $(x^2)' = 2x$.

::: example
Étudier la croissance de $f(x) = x^3 - 3 x$
:::

::: exercise
Étudier la croissance de $f(x) = 2x^3 - 15x^2 + 36x$
:::

~~~ {.julia .plot .fragment}
x = -2:0.01:2
plot(x, x -> x^3 - 3x, label=L"x^3 - 3x", framestyle=:origin)
~~~

# Dérivée de $\sqrt x$ {.split}

::: proposition
Si $f(x) = \sqrt x$, alors $f'(a) = \frac 1 {2 \sqrt a}$
:::

~~~ {.julia .plot}
x = 0:0.01:2
plot(x, sqrt.(x), label=L"\sqrt{x}", framestyle=:origin)

x = 0:0.01:2
y = @. 0.5 * (x - 1) + 1
plot!(x, y, label="tangente")
scatter!([1], [1], label=L"(a, f(a))")
~~~

# Dérivée de $\frac 1 x$ {.split}

::: proposition
Si $f(x) = \frac 1 x$, alors $f'(a) = -\frac 1 {a^2}$
:::

~~~ {.julia .plot}
x = 0.5:0.01:2
plot(x, x -> 1/x, label=L"\frac 1 x", framestyle=:origin)

x = 0.7:0.01:1.5
y = @. -1 * (x - 1) + 1
plot!(x, y, label="tangente")
scatter!([1], [1], label=L"(a, f(a))")
~~~

# Dérivée de $x^n$ {.split}

One rule to rule them all.
Nous admettons la proposition suivante sans preuve
(je peux vous guider si vous êtes intéressés).

::: proposition
Si $f(x) = x^n$, alors $f'(x) = n x^{n - 1}.$
:::

::: example
Calculer la dérivée de

- $f(x) = x^5$
- $g(x) = \sqrt[3] x$
- $h(x) = \frac 1 {\sqrt x}$
- $i(x) = \frac 1 {x^3}$
:::

La dérivée d'une puissance est une puissance.

# Application: MRUA {.split}

Puisque la vitesse est une pente,
nous l'avons également généralisée aux mouvements qui ne sont pas des droites
(appelés MRU).

Remarquons que la vitesse est
\begin{align}
\lim_{\Delta t \to 0} \frac {\Delta x} {\Delta t},
\end{align}
c'est-à-dire la dérivée de la position.

::: exercise
Dériver deux fois $x(t) = \frac 1 2 a t^2 + v t + x_0$ par rapport au temps.
:::

::: question
Comprenez-vous pourquoi il y a un $\frac 1 2$ maintenant?
:::


# Une limite en radians importante {.split}

::: proposition
En **radians**:
\begin{align}
\lim_{x \to 0} \frac {\sin x} x = 1
\end{align}
:::

::: question
L'équation est-elle vraie en degrés?
:::

::: text-center
![](/static/images/1678151714.png){width=70%}
:::


# Dérivée de $\sin x$ {.split}

::: proposition
En **radians** (ne fonctionne pas en degrés):
\begin{align}
\sin'(x) = \cos(x)
\end{align}
:::

::: remark
\begin{align}
\sin x - \sin a = 2 \cos \left(\frac {x + a} 2\right) \sin \left(\frac {x - a} 2\right)
\end{align}
:::

# Dérivée de $\cos x$ {.split}

::: proposition
En **radians** (ne fonctionne pas en degrés):
\begin{align}
\cos'(x) = -\sin x
\end{align}
:::

::: remark
\begin{align}
\cos x - \cos a = -2 \sin \left(\frac {x + a} 2\right) \sin \left(\frac {x - a} 2\right)
\end{align}
:::

# Application: $\sin x$ pour $0 \leq x \ll 1$ {.split}

::: question
L'ordinateur ne connaît que les opérations mathématiques de base.
Comment calcule-t-elle $\sin x$?
:::

::: idea
\begin{align}
\sin x \approx \underbrace{a + b x + c x^2}_{f(x)}
\end{align}

On essayera d'avoir: $f(0) = \sin 0$, $f'(0) = \sin'(0)$, etc.
:::

~~~ {.julia .plot}
x = -1.5:0.01:1.5
plot(x, sin, label=L"\sin x", framestyle=:origin)
plot!(x, x -> x, label=L"x")
plot!(x, x -> x - x^3/6, label=L"x - \frac{x^3}{6}")
~~~

# Dérivée de $\tan x$ {.split}

::: question
Quelle est la dérivée de $\tan$?
:::

Nous répondrons à cette question plus tard.

Nous déduirons la dérivée de $\tan$ à partir de celle de $\sin$ et $\cos$,
puisque
\begin{align}
\tan x = \frac {\sin x} {\cos x}
\end{align}

Le fait que la pente de $\tan$ peut se déduire de la pente de $\sin$ et de celle de $\cos$
est remarquable.

# Comportement avec les opérations de fonction {.split}

Souvenons-nous que pour les droites:

\begin{align}
(f \pm g)' &= f' \pm g'\\
(f \circ g)' &= f' \cdot g'\\
\end{align}

::: remark
Remarquons qu'on ne pouvait pas parler de pente pour $fg$ ou $\frac f g$.
Avec les dérivées, on peut!
:::

On va montrer:

\begin{align}
(fg)' &= f'g + fg'\\
\left(\frac {f}{g}\right)' &= \frac {f'g - fg'} {g'}
\end{align}

# Comportement avec la somme {.split}

::: proposition
\begin{align}
(f + g)'(a) = f'(a) + g'(a)
\end{align}
:::

::: {.info title="Rappel"}
\begin{align}
f'(a) = \lim_{x \to a} \frac {f(x) - f(a)} {x - a}
\end{align}
:::

::: exercise
Prouver la règle pour $f - g$.
:::

# Comportement avec le produit {.split}

::: proposition
\begin{align}
(f g)'(a) = f'(a) g(a) + f(a) g'(a).
\end{align}
:::

::: {.info title="Rappel"}
\begin{align}
f'(a) = \lim_{x \to a} \frac {f(x) - f(a)} {x - a}
\end{align}
:::

# Exemples

# Comportement avec la composition {.split}

::: proposition
\begin{align}
(f \circ g)'(a) = f'(g(a)) g'(a)
\end{align}
:::

::: {.info title="Rappel"}
\begin{align}
f'(a) = \lim_{x \to a} \frac {f(x) - f(a)} {x - a}
\end{align}
:::

# Comportement avec le quotient {.split}

::: proposition
\begin{align}
\left(\frac f g\right)'(a) = \frac {f'(a) g(a) - f(a) g'(a)} {g^2(a)}
\end{align}
:::

::: {.info title="Rappel"}
\begin{align}
f'(a) = \lim_{x \to a} \frac {f(x) - f(a)} {x - a}
\end{align}
:::
