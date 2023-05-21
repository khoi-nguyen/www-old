---
title: "Chapter 2: First-Order Differential Equations"
output: revealjs
kernel: python
notes: |
  - 19/05: Direction fields, autonomous equations, phase portraits, separable equations (1-18)
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
