---
title: "Chapter 2: First-Order Differential Equations"
output: revealjs
kernel: python
notes: |
  - 19/05: Direction fields, autonomous equations, phase portraits, separable equations (1-18)
  - 22/05: separable equations, linear equations (19-31)
...

# Direction fields

\begin{align*}
\begin{cases}
y' &= f(x, y)\\
y(x_0) &= y_0
\end{cases}
\end{align*}

We may not know $y(x)$,
but we know its **slope** at every point.

~~~ {.python .plot}
x = linspace(-5, 5, 30)
y = linspace(-5, 5, 30)
X, Y = meshgrid(x, y)
slope = 0.2 * X * Y
quiver(X, Y, ones_like(slope), slope, color="#255994")
# One solution curve
t = linspace(-5, 5, 100)
plot(t, 0.2 * exp(0.1 * t ** 2), color="red")
~~~

If solutions are always unique,
the direction fields don't cross.

# Direction fields with Python

~~~ {.python .jupyter}
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-5, 5, 30)
y = np.linspace(-5, 5, 30)
X, Y = np.meshgrid(x, y)
slope = 0.2 * X * Y
plt.quiver(X, Y, np.ones_like(slope), slope)
~~~

# Direction fields with geogebra {.nosplit}

~~~ {.widget name="geogebra"}
url: https://www.geogebra.org/m/W7dAdgqc
height: 900
width: 1600
~~~

# Example: direction field

::::: {.col}
![](/static/images/1684437573.png)

::: question
Does the solution exist? Is it unique?
:::
:::::

::::: {.col}
~~~ {.python .plot width=100%}
x = linspace(-5, 5, 30)
y = linspace(-5, 5, 30)
X, Y = meshgrid(x, y)
slope = sin(Y)
quiver(X, Y, ones_like(slope), slope, color="#255994")
plot(0, -1.5, "ro")
~~~
:::::

# Autonomous first-order ODEs

::: definition
An ODE is **autonomous** when the RHS in normal form does not depend
on the independent variable: $y' = f(y)$.
:::

Their direction fields are invariant under horizontal translations.

~~~ {.python .plot width=100%}
x = linspace(-5, 5, 30)
y = linspace(-5, 5, 30)
X, Y = meshgrid(x, y)
slope = cos(Y)
quiver(X, Y, ones_like(slope), slope, color="#255994")
~~~

# Critical points

Consider the ODE $y' = f(y)$.

::: definition
\begin{align*}
c \ \text{is critical point} \iff f(c) = 0
\end{align*}
:::

~~~ {.python .plot}
x = linspace(-5, 5, 30)
y = linspace(-5, 5, 30)
X, Y = meshgrid(x, y)
slope = cos(Y)
quiver(X, Y, ones_like(slope), slope, color="#255994")
~~~

::: proposition
$y(x) \defeq c$ satisfies $y' = f(y)$
iff $c$ is a critical point.
:::

# Example and phase portrait

::: example
\begin{align*}
\frac {\dd P} {\dd t} = P(a - b P)
\end{align*}
:::

::: cols
::::: {.col}
![](/static/images/1684442031.png)
:::::
::::: {.col}
![](/static/images/1684442063.png)
![](/static/images/1684442158.png)
:::::
:::

# Attractors and repellers

![](/static/images/1684451011.png){width=80%}

# Example: solution curves

![](/static/images/1684442303.png)

# Direction fields and translation property

::::: {.col}
![](/static/images/1684445327.png){height=900}
:::::

::::: {.col}
::: proposition
If $y(x)$ is a solution of
\begin{align*}
y' = f(y),
\end{align*}
then so is $\tilde y(x) \defeq y(x + k)$.
:::
:::::

# Exercises 2.1

::::: {.col}
<pdf-reader src="/static/documents/zill-2.1.pdf" width="100%" height="900" />
:::::

::::: {.col}
Selection: 19, 21, 27, 29, 39, 41
:::::

# Answers

![](/static/images/1684450837.png){width=100%}

# Separable equations

::: definition
A first-order ODE is **separable** if it has the form
\begin{align*}
\frac {\dd y} {\dd x} = g(x) h(y).
\end{align*}
:::

::: example
Exactly one of these equations is separable:
\begin{align*}
\frac {\dd y} {\dd x} = y^2 x e^{3x + 4y}
\quad \text{and} \quad
\frac {\dd y} {\dd x} = y + \sin x.
\end{align*}
Which one?
:::

# Solving a separable equation

The equation
\begin{align*}
\frac {\dd y} {\dd x} = g(x) h(y)
\end{align*}
can be reorganised into
\begin{align*}
\frac 1 {h(y)} \dd y = g(x) \dd x.
\end{align*}

We'll see that integrating both sides will allow us to find the solution.

# Example: separable DE

![](/static/images/1684449683.png){width=100%}

# Example: separable IVP

![](/static/images/1684449776.png){width=90%}
![](/static/images/1684449784.png)

# Losing a solution: example

Be careful when **dividing**.

![](/static/images/1684449959.png)
![](/static/images/1684449975.png)

# 22/05/2023

::::: {.col}

### Autonomous first-order ODEs $y' = f(y)$

#. The only constant solutions are critical points (roots of $f$)
#. Critical points can be: attractors, repellers, semi-stable
#. Direction fields are translation invariant and can be summarized via **phase portraits**.

~~~ {.python .plot width=100%}
x = linspace(-3, 3, 30)
y = linspace(-3, 3, 30)
X, Y = meshgrid(x, y)
slope = cos(Y)
quiver(X, Y, ones_like(slope), slope, color="#255994")
~~~
:::::

::::: {.col}

### Solving separable first-order ODEs

\begin{align*}
\frac {\dd y} {\dd x} = \frac {g(x)} {h(y)}
\implies
\int h(y) \dd y = \int g(x) \dd x
\end{align*}

::: remark
Be careful when dividing by 0!
:::

### Announcements

I've decided to wait a bit more before giving you homework.

You will always have a full week's notice.

### French sentence of the day

::: {.info title="French sentence of the day"}
**Peux-tu répéter?**^[If mispronounced, you'll say "can you fart again?". No pressure] - *Can you repeat?*
:::

Always blame the other person when you don't understand their French.
You can add a "**non (euhhhh) parlo (euhhh) español**".
Don't forget to speak louder than them.
:::::

# IVPs

![](/static/images/1684450099.png){width=100%}

# Integral-defined functions

![](/static/images/1684450665.png){width=100%}

# Exercises 2.2

::: col
<pdf-reader src="/static/documents/zill-2.2.pdf" width="100%" height="900" />
:::

::::: {.col}
Selection: 5, 13, 23, 27, (29), 38
:::::

# Answers 2.2

![](/static/images/1684450887.png)
![](/static/images/1684450897.png)

# Solving linear equations

An ODE is **linear** if it's linear in $y$

::: definition
A first-order ODE is linear if ith as the form
\begin{align*}
a_1(x) \frac {\dd y} {\dd x} + a_0(x) y = g(x),
\end{align*}
:::

Normalizing the highest order coefficient yields the so-called **standard form**.

::: {.remark title="Standard form"}
\begin{align*}
\frac {\dd y} {\dd x} + P(x) y = f(x).
\end{align*}
:::

# Integrating factors

Start with the standard form:
\begin{align*}
\frac {\dd y} {\dd x} + P(x) y = f(x)
\end{align*}

Multiply both sides by $\mu(x)$:
\begin{align*}
{\color{red}\mu(x)} \frac {\dd y} {\dd x} + {\color{red}\mu(x)} P(x) y = {\color{red}\mu(x)} f(x).
\end{align*}

If $\mu$ is chosen so that $\boxed{\mu'(x) = \mu(x) P(x)}$, then we get:
\begin{align*}
\frac {\dd (\mu y)} {\dd x} = \mu(x) f(x),
\end{align*}
which is much easier to solve.

::: {.definition title="Integrating factor"}
\begin{align*}
\mu(x) \defeq e^{\int P(x) \dd x} \dd x
\end{align*}
:::

# Solving a linear equation: example

#. Write the equation in standard form.
#. Choose $\mu(x) \defeq e^{\int P(x) \dd x}$.
#. Multiply everything by $\mu$
#. Recognize the product rule on the LHS.

![](/static/images/1684701158.png)
![](/static/images/1684701184.png)

# General solution

![](/static/images/1684702676.png){width=100%}

# General solution: example 2

![](/static/images/1684702706.png){width=100%}

# Linear IVP: example

![](/static/images/1684702749.png){width=100%}

# Piecewise-linear DEs

![](/static/images/1684703099.png){width=100%}

# Exercises

<pdf-reader src="/static/documents/zill-2.3.pdf" width="100%" height="900" />

# 23/05/2023

::::: {.col}

### Linear first-order equations

\begin{align*}
\frac {\dd y} {\dd x} + P(x) y = f(x)
\end{align*}

If $\mu(x) = e^{\int P(x) \dd x}$, then
multiplying by $\mu$ gives
\begin{align*}
(\mu(x) y(x))' = \mu(x) f(x)
\end{align*}

You just need to integrate both sides.

:::::

::::: {.col}

### French sentence of the day

**L'ordinateur portable de Hunter Biden** - *Hunter Biden's laptop*.

Useful for the midterm when you don't know how to answer a question.

This shows two features of French:

- the *h* is silent ('ello, 'ow arrre you?)
- French forms the possessive differently (the laptop **OF** Hunter Biden)

:::::

# 2.4 Exact equations

We now turn our attention to functions $f: \R^2 \to \R$.

::: definition
The differential of $f$ is
\begin{align*}
\dd f = \frac {\partial f} {\partial x} \dd x + \frac {\partial f} {\partial y} \dd y.
\end{align*}
:::

::: question
Given $M$ and $N$, find $f$ such that
\begin{align*}
\dd f = M(x, y) \dd x + N(x, y) \dd y.
\end{align*}
:::

This will be helpful, as $\dd f = 0 \iff f(x, y) = c$.

# Symmetry of the derivatives

\begin{align*}
\dd f = M(x, y) \dd x + N(x, y) \dd y.
\iff
\begin{cases}
\partial_x f(x, y) = M(x, y)\\
\partial_y f(x, y) = N(x, y)\\
\end{cases}
\end{align*}

As $\partial_x \partial_y f = \partial_y \partial_x f$,
the equation is only solvable if
\begin{align*}
\partial_y M(x, y) = \partial_x N(x, y)
\end{align*}

# Example: solving an exact DE

![](/static/images/1684704066.png){width=100%}

# Example 2: solving an exact DE

![](/static/images/1684704779.png){width=100%}
![](/static/images/1684704796.png){width=100%}

# Example: IVP

![](/static/images/1684704834.png){width=100%}

# Integrating factors

Let's find $\mu$ to make the equation exact.

\begin{align*}
\mu(x, y) M(x, y) \dd x + \mu(x, y) N(x, y) \dd y = 0.
\end{align*}

::: proposition
The above equation is exact iff
\begin{align*}
(\partial_x \mu) N - (\partial_y \mu) M = (\partial_y M - \partial_x N) \mu
\end{align*}
:::

This is difficult, and we shall therefore assume that $\mu$ depends only on one variable:

\begin{align*}
\frac {\dd \mu} {\dd x} = \frac {\partial_y M - \partial_x N} N \mu.
\quad \text{or} \quad
\frac {\dd \mu} {\dd y} = \frac {\partial_x N - \partial_y M} M \mu.
\end{align*}

# Example: DE made exact

![](/static/images/1684705812.png)

# Exercises

<pdf-reader src="/static/documents/zill-2.4.pdf" width="100%" height="900" />

# Homogeneous equations

::: definition
The function $f(x, y)$ is **homogeneous** of degree $\alpha$ if
\begin{align*}
f(tx, ty) = t^\alpha f(x, y)
\end{align*}
:::

::: definition
A first-order DE in differential form
\begin{align*}
M(x, y) \dd x + N(x, y) \dd y = 0
\end{align*}
is **homogeneous** of degree $\alpha$
if both $M$ and $N$ are homogeneous of degree $\alpha$ as well.
:::

# Example: solving a homogeneous DE

Write $y = ux$ (or $x = uy$).

![](/static/images/1684707103.png){width=100%}

# Bernouilli's equation

::: {.definition title="Bernouilli's equation"}
\begin{align*}
\frac {\dd y} {\dd x} + P(x) y = f(x) y^n
\end{align*}
:::

Write $u = y^{1 - n}$.

# Example: Bernouilli's equation

![](/static/images/1684707304.png){width=100%}

# Reduction to separation of variables

\begin{align*}
\frac {\dd y} {\dd x} = f(\underbrace{Ax + By + C}_u)
\end{align*}

![](/static/images/1684707481.png)
![](/static/images/1684707501.png)

# Exercises

<pdf-reader src="/static/documents/zill-2.5.pdf" width="100%" height="900" />

# Euler's method

::: col
\begin{align*}
\begin{cases}
y' &= f(x, y)\\
y(x_0) &= y_0\\
\end{cases}
\end{align*}

As $y' \approx \Delta y / \Delta x$,
we know that
\begin{align*}
\underbrace{y_1 - y_0}_{\Delta y}
\approx \underbrace{f(x_0, y_0)}_{y'}
\underbrace{(x_1 - x_0)}_{\Delta x}
\implies
y_1 \approx y_0 + f(x_0, y_0) (x_1 - x_0)
\end{align*}

If $x_k = x_0 + kh$, then
\begin{align*}
\boxed{
y_{k + 1} \approx y_k + f(x_k, y_k) h
}
\end{align*}
:::

::: col
![](/static/images/1684781701.png)
:::

# Python implementation

~~~ {.python .jupyter}
from matplotlib.pyplot import *
from numpy import *

def euler(f, x_0, y_0, h, n):
    x = [x_0 + i * h for i in range(n)]
    y = [y_0] + [0] * (n - 1)
    for i in range(1, n):
        y[i] = y[i - 1] + f(x[i - 1], y[i - 1]) * h
    return x, y

f = lambda x, y: exp(x)

# Plot numerical solution
n = 100
x, y = euler(f, 0, 1, 1/n, n + 1)
plot(x, y)

# Plot real solution
x = linspace(0, 1, 1000)
plot(x, exp(x))
~~~

# Exercises

<pdf-reader src="/static/documents/zill-2.pdf" width="100%" height="900" />
