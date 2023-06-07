---
title: "Chapter 6: Series solutions"
output: revealjs
kernel: python
...

# 05-06

::::: {.col}

### Announcements

- I'll give you your **midterms on Wednesday**
- **Today**: using Taylor series

#### French sentence of the day

You might feel discouraged that French always switch to English when you speak to them.
Don't worry, I have a solution.

**Hé... euh... You speak ze Eengleesh?**

Don't forget to be a bit agressive.
That bloody foreigner is making you switch to English.
Make it a bit sensual too, wee'rre in ze ceetee of love.

:::::

::::: {.col}
A lot of work goes into the French sentence of the day,
and ChatGPT refuses to help.

![](/static/images/1685958276.png)
:::::

# Power series: review

Power series **centered at $a$**.
\begin{align*}
\sum_{n = 0}^{+\infty} c_n (x - a)^n
= c_0 + c_1(x - a) + c_2(x - a^2 + \dots
\end{align*}

Such a power series **converges** if the following limit exists
\begin{align*}
\lim_{n \to +\infty} \sum_{n = 0}^N c_n (x - a)^n.
\end{align*}

It converges **absolutely** if
\begin{align*}
\lim_{n \to +\infty} \sum_{n = 0}^N \abs{c_n (x - a)^n}.
\end{align*}

::: remark
Absolute convergence is necessary to talk about operations on series.
:::

# Radius and interval of convergence

\begin{align*}
\sum_{n = 0}^{+\infty} c_n (x - a)^n
= c_0 + c_1(x - a) + c_2(x - a^2 + \dots
\end{align*}

- The **interval of convergence** is symmetric,
  and has the form $[a - R, a + R]$.
\begin{align*}
[a - R, a + R], (a - R, a + R], [a - R, a + R), (a - R, a + R)
\end{align*}
  $R$ is called the **radius of convergence**.
  Remark

![](/static/images/1685946379.png)

# Convergence

::: proposition
The series
\begin{align*}
\sum_{n = 0}^{+\infty} c_n (x - a)^n
= c_0 + c_1(x - a) + c_2(x - a^2 + \dots
\end{align*}
converges if
\begin{align*}
\lim_{n \to +\infty} \abs{x - a} \abs{\frac {c_{n + 1}} {c_n}} < 1.
\end{align*}
:::

# Example: interval of convergence

![](/static/images/1685947101.png)

# Functions as power series

- A power series defines a function
\begin{align*}
f(x) \defeq \sum_{n = 0}^{+\infty} c_n(x - a)^n
\end{align*}
- Functions that have power series are called **analytic**.
- Identity property
\begin{align*}
\sum_{n = 0}^{+\infty} c_n (x - a)^n = 0
\text{ for } x \in (a - R, a + R)
\implies c_n = 0
\end{align*}
- Power series are the **Taylor series** of the function
\begin{align*}
f(x) \defeq \sum_{n = 0}^{+\infty} \frac {f^{(n)}(a)} {n!}(x - a)^n
\end{align*}

# Differentiation and integration

\begin{align*}
y = \sum_{n = 0}^{+\infty} c_n(x - a)^n
\end{align*}

Differentiation and integration can be performed term by term

\begin{align*}
y' = \sum_{n = 1}^{+\infty} c_n n (x - a)^{n - 1}\\
\int y \dd x = \sum_{n = 0}^{+\infty} \frac {c_n} {n + 1} (x - a)^{n + 1}
\end{align*}

The convergence radius is the same (check using the ratio test)
but we may lose convergence when differentiation or gain convergence
when integrating at endpoints.

# Some Taylor series

![](/static/images/1685950472.png)

# Example: multiplication of power series

![](/static/images/1685950524.png)

# Example: addition of power series

![](/static/images/1685950634.png)
![](/static/images/1685950653.png)

# Example: power series solution

![](/static/images/1685950738.png)

# Exercises

<pdf-reader src="/static/documents/zill-6.1.pdf" width="100%" height="900" />

# 06/06

I've decided to write the date the American way today.

::::: {.col}

## Power series

\begin{align*}
y = \sum_{n = 0}^{+\infty} c_n(x - a)^n
\end{align*}

Substitute in the ODE,
use the **identity property** (uniqueness of power series expansion).

Today, we'll do the same, but with equations of order $2$.
We'll need two solutions.

:::::

::::: {.col}

## French **song** of the day


~~~ {.widget name="youtube"}
url: https://www.youtube.com/watch?v=JAs4edeYUJY
~~~

  " Tout mes amis ont une queue, mais moi non. (...) Je sais ce que je ferais si j'avais une queue !

  (musique) Si j'avais une queue, elle me ferait bondir, frétiller (!!)

  (...) J'en serais si fière que jamais je ne la laisserais tomber, je la balancerais : elle pointerait vers le soleil !

  Ma queue serait grande, puissante et jolie. Touffue (!!) et violette aussi ! Et tout le monde dirait qu'elle n'as pas son pareil, si j'avais une queue comme les amis ! (/musique)

  Je dois trouver une queue Winnie, mais... Comment ?!?! "

:::::

# Raili is lazy

::::: {.col}
![](/static/images/1686045359.png)
:::::

::::: {.col}
![](/static/images/1686045395.png)
:::::

# Ordinary and singular points

\begin{align*}
y'' + P(x) y' + Q(x) y = 0.
\end{align*}

- **ordinary point**: $P$ and $Q$ are **analytic** at that point
- **singular point**: not ordinary

# Example: ordinary point

![](/static/images/1685951446.png)

# Singular points

![](/static/images/1685951466.png)

# Polynomial coefficients and division

![](/static/images/1685951501.png)

# Existence of power series solution

::: theorem
Assume $x_0$ is an **ordinary point** of
a_2(x) y'' + a_1(x) y' + a_0(x) y = 0.
We can find two linearly independent solutions
expressed as power series whose convergence radius
is greater than the distance from $x_0$ to the closest singular point.
:::

# Example: minimum radius of convergence

![](/static/images/1685951931.png)
![](/static/images/1685951941.png)

# Example: Power Series solution

![](/static/images/1685952258.png){width=100%}

# Example 6: Power series solution

![](/static/images/1685952518.png)

# Example 7: three-term recurrence relation

![](/static/images/1685952902.png)
![](/static/images/1685952922.png)

# Example 8: DE with nonpolynomial coefficient

![](/static/images/1685953290.png)

# Exercises

<pdf-reader src="/static/documents/zill-6.2.pdf" width="100%" height="900" />

# 07/06

::::: {.col}

### Ordinary points

Ordinary point: coefficients in standard form are analytic.

- Substitute $y = \sum c_n x^n$ into an ODE
- Rewrite the equation as one power series
- The coefficients vanish -> recurrence relation
- two terms: separate in two sums ($c_0$, $c_1$)
- three terms: Assume $c_0 = 0$, get one solution, assume $c_1 = 0$, get the other.

:::::

::::: {.col}

- Courtney's parents are from Ohio
  and she hates Michigan.
  It's a secret, Khoi, don't put that on the slide.

### Dating while in France

- Je suis majeur^[Suggestion by Arnuv] - I am of legal age
- Bon gars avec une arme à feu - Good guy with a gun
- Montrez-moi votre belle tour Eiffel - Show me your beautiful Eiffel tower
- Chercher à goûter les meilleures baguettes françaises - Looking to taste the best French baguettes.

:::::

# Regular singular point

::: definition
A **singular** point of a linear differential equation
\begin{align*}
y'' + P(x) y' + Q(x) y = 0
\end{align*}
is **regular** if $(x - x_0) P(x)$ and $(x - x_0)^2 Q(x)$ are analytic at $x_0$.
:::

Irregular if not regular.

When the coefficient is polynomial,
this means $(x - x_0)$ can appear at most to the first order in the denominator of $P$
and at most to the second order in the denominator of $Q$.

# Classification of singular points

![](/static/images/1686089315.png)
![](/static/images/1686089329.png)

# Frobenius's method

::: theorem
If $x_0$ is a regular singular point,
there is at least a solution of the form
\begin{align*}
y = \sum_{n = 0}^{+\infty} c_n (x - x_0)^{n + r}
\end{align*}
:::

::: remark
- We need to find $r$
- $r \notin \N$, not a power series
- We don't necessarily have two solutions
:::

# Example: two series solution

![](/static/images/1686089583.png)

# Indicial equation

As $xP(x)$ and $x^2 Q(x)$ are **analytic**, we can write
\begin{align*}
x P(x) &= \sum_{n = 0}^n a_n x^n\\
x^2 Q(x) &= \sum_{n = 0}^n b_n x^n\\
\end{align*}

Multiplying by $x^2$ and substituting $y = \sum c_n x^{n + r}$ in
\begin{align*}
x^2 y'' + x(xP(x)) y' + [x^2Q(x)]y = 0
\end{align*}
yields
\begin{align*}
r(r - 1) + a_0 r + b_0 = 0.
\end{align*}

# One series solution

![](/static/images/1686090987.png)

# One or two series solution

Let $r_1$ and $r_2$ be the indicial roots, with $r_1 \geq r_2$.

- $r_1 - r_2$ is not an integer, then we'll have two solutions

- $r_1 - r_2$ is a positive integer, we may only find one solution

- $r_1 = r_2$, we will only find one solution.

The second solution is obtained via **reduction of order**.

\begin{align*}
y_2(x) = y_1(x) \int \frac {e^{-\int P(x) \dd x}} {y_1^2(x)} \dd x.
\end{align*}

# Exercises

<pdf-reader src="/static/documents/zill-6.3.pdf" width="100%" height="900" />
