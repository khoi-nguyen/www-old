---
title: "Chapter 4: Higher-Order ODEs"
output: revealjs
kernel: python
...

# 25 May 2023

## Homework

::::: {.col}

Homework is on Moodle

![](/static/images/1684968700.png){width=100%}

:::::

::::: {.col}

## French sentence of the day

![](/static/images/1684969790.png){height=500px}

If you ever find yourself in Emily's situation,
you can tell your new friend the following:

**Tu pues, va te laver** - *you stink, have a shower*.

Again, you're welcome.

:::::


# IVP vs BVP

\begin{align*}
a_n(x) \frac {\dd^n y} {\dd x^n}
+ a_{n - 1}(x) \frac {\dd^{n - 1} y} {\dd x^{n - 1}}
+ \dots +
+ a_1(x) \frac {\dd y} {\dd x}
+ a_0(x) y = g(x)
\end{align*}

Condition name              Example
----------------            --------
Initial value               $y(x_0) = y_0$, $y'(x_0) = y_1$, $\dots$, $y^{(n - 1)}(x_0) = y_{n - 1}$
Boundary value              $y(a) = y_0$, $y(b) = y_1$.

# Uniqueness result for IVPs

\begin{align*}
a_n(x) \frac {\dd^n y} {\dd x^n}
+ a_{n - 1}(x) \frac {\dd^{n - 1} y} {\dd x^{n - 1}}
+ \dots +
+ a_1(x) \frac {\dd y} {\dd x}
+ a_0(x) y = g(x)
\end{align*}

::: theorem
Assume all the functions involved are continuous
and $a_n$ never vanishes on an interval $I$.
Then there is a **unique solution** on $I$ if $x_0 \in I$.
:::

![](/static/images/1684963321.png){width=100%}

# BVP and uniquenes

\begin{align*}
\begin{cases}
x'' + 16 x = 0\\
x(0) = 0, x(a) = b.
\end{cases}
\implies
x = \cancel{c_1 \cos 4t} + c_2 \sin 4t
\end{align*}

- $a = \frac \pi 2$, $b = 0$: Infinitely many solutions
- $a = \frac \pi 8$, $b = 0$: One solution
- $a = \frac \pi 2$, $b = 1$: No solution

![](/static/images/1684963880.png){width=80%}

# Homogenous equation

::: {.definition title="Homogenous linear ODE"}
\begin{align*}
a_n(x) \frac {\dd^n y} {\dd x^n}
+ a_{n - 1}(x) \frac {\dd^{n - 1} y} {\dd x^{n - 1}}
+ \dots +
+ a_1(x) \frac {\dd y} {\dd x}
+ a_0(x) y = 0
\end{align*}
:::

TLDR: linear ODE is homogeneous if independent term is $0$.

::: remark
Not related to the concept of **homogeneous function**.
:::

# Differential operator

Write $D = \frac {\dd} {\dd x}$ and
\begin{align*}
L \defeq
a_n(x) D^n
+ a_{n - 1}(x) D^{n - 1}
+ \dots +
+ a_1(x) D
+ a_0(x)
\end{align*}

The equation
\begin{align*}
a_n(x) \frac {\dd^n y} {\dd x^n}
+ a_{n - 1}(x) \frac {\dd^{n - 1} y} {\dd x^{n - 1}}
+ \dots +
+ a_1(x) \frac {\dd y} {\dd x}
+ a_0(x) y = g(x)
\end{align*}
becomes
\begin{align*}
L y(x) = g(x).
\end{align*}

Note that $L$ is **linear**,
\begin{align*}
L(\alpha y_1(x) + \beta y_1(x)) = \alpha L y_1(x) + \beta L y_2(x).
\end{align*}

# Superposition principle

The solution space is a **vector space**.

::: proposition
In a homogeneous linear $L y = 0$,
any linear combination of two solutions is also a solution.
:::

![](/static/images/1684964826.png){width=100%}

# Linear independence

::: definition
The functions $f_1$, $\dots$, $f_n$ are **linearly dependent** on $I$
if there exist constants $c_1, \dots, c_n$, not all zero, such that
\begin{align*}
c_1 f_1(x) + c_2 f_2(x) + \dots + c_n f_n(x) = 0
\end{align*}
for every $x \in I$.
:::

![](/static/images/1684965351.png){width=100%}

# Linear independence

::: theorem
Let $y_1, \dots, y_n$ be solutions to a homogeneous linear nth-order ODE on $I$.
These solutions are **linearly independent** iff
\begin{align*}
\underbrace{
\begin{vmatrix}
f_1 & f_2 & \dots & f_n\\
f_1'& f_2'& \dots & f_n'\\
\vdots & \vdots & & \vdots\\
f_1^{(n-1)} & f_2^{(n - 1)} & \dots & f_n^{(n - 1)}
\end{vmatrix}
}_{\text{Wronskian}}
\neq 0
\end{align*}
for every $x \in I$>
:::

Wronskian is either identically 0 or never vanishes.

# Fundamental set of solutions

A set of $n$ linearly independent solution of
an homogeneous linear nth-order ODE is called
a **fundamental set of solutions**.

::: theorem
There exists a fundamental set for homogeneous linear nth-dimensional ODE.

Moreover, any solution is a linear combination of the fundamental set.
:::

# Examples

![](/static/images/1684966249.png)
![](/static/images/1684966315.png)

# Nonhomogeneous equation

\begin{align*}
a_n(x) \frac {\dd^n y} {\dd x^n}
+ a_{n - 1}(x) \frac {\dd^{n - 1} y} {\dd x^{n - 1}}
+ \dots +
+ a_1(x) \frac {\dd y} {\dd x}
+ a_0(x) y = g(x)
\end{align*}

::: theorem
The solution set is

\begin{align*}
y_p(x) + \span\{\text{fundamental set of homogeneous equation}\}
\end{align*}
:::

# General solution

![](/static/images/1684966550.png)

# Superposition principle

::: theorem
Assume that we have
\begin{align*}
Ly_i(x) = g_i(x), \quad i = 1, \dots, k.
\end{align*}

Then $y = y_1 + \dots + y_n$ is solution of
\begin{align*}
L y(x) = g_1(x) + \dots + g_k(x).
\end{align*}
:::

![](/static/images/1684966746.png)

# Exercises

<pdf-reader src="/static/documents/zill-4.1.pdf" width="100%" height="900" />

# Answers

![](/static/images/1684967450.png)
![](/static/images/1684967459.png)

# Reduction of order

- Homogeneous linear ODE
- Constant coefficients
- $y_1$ nontrivial solution

**Reduction of order**.
Substitute $y_2(x) = u(x) y_1(x)$ into the differential equation
allows to find another solution.

# Reduction of order: example

![](/static/images/1684967102.png){width=100%}

# Other example

![](/static/images/1684967305.png){width=100%}

# Exercises

<pdf-reader src="/static/documents/zill-4.2.pdf" width="100%" height="900" />

# Answers

![](/static/images/1684967469.png)

# French culture through Youtube

You might have been lured into visiting France under false pretences
such as a lower drinking age, phallic monuments,
overpriced wine and animated movies involving rats.
But fear not, for I am here to show you *ze true France*.

::::: {.col}

~~~ {.yaml .widget name="youtube"}
url: https://www.youtube.com/watch?v=16k-yhcRNk8
zoom: 1
~~~

Driving while blind

~~~ {.yaml .widget name="youtube"}
url: https://www.youtube.com/watch?v=MytfhzcSF-Y
zoom: 1
~~~

Getting dressed as Mario, go kart into a shop to steal bananas

:::::

::::: {.col}

~~~ {.yaml .widget name="youtube"}
url: https://www.youtube.com/watch?v=JTiPqZbM5ls
zoom: 1
~~~

Getting dressed as a sheep and go into a kebab shop with flowers

~~~ {.yaml .widget name="youtube"}
url: https://www.youtube.com/watch?v=gHCxdlZ7G18
zoom: 1
~~~

Geting dressed as a snail and slow down traffic.

:::::

# Homogeneous linear equations with constant coefficients

We'll focus on how to solve
\begin{align*}
ay'' + by' + c = 0.
\end{align*}

::: proposition
Let $y = e^{mx}$.

\begin{align*}
ay'' + by' + c = 0 \iff \underbrace{am^2 + bm + c = 0}_{\text{auxiliary equation}}
\end{align*}
:::

# Different cases

Let $y = e^{mx}$.
\begin{align*}
ay'' + by' + c = 0 \iff \underbrace{am^2 + bm + c = 0}_{\text{auxiliary equation}}
\end{align*}

**Distinct real roots** ($\Delta > 0$) $m_1 \neq m_2$.
\begin{align*}
y = c_1 e^{m_1 x} + c_2 e^{m_2 x}
\end{align*}

**Repeated real roots** ($\Delta = 0$) $m_1 = m_2$.
\begin{align*}
y = c_1 e^{m_1 x} + c_2 {\color{red} x} e^{m_1 x}
\end{align*}

**Complex conjugate solutions** ($\Delta < 0$) $m_1 = \alpha + i \beta$, $m_2 = \alpha - i \beta$
\begin{align*}
y &= c_1 e^{m_1 x} + c_2 e^{m_2 x}\\
&= e^{\alpha x} (c_1 \cos \beta x + c_2 \sin \beta x)
\end{align*}

::: exercise
Use reduction of order to find the second solution for the $\Delta = 0$ case.
:::

# Example 1

![](/static/images/1685049949.png)

# Example 2: IVP

![](/static/images/1685049980.png)

# Example 3: third-order

![](/static/images/1685050006.png)

# Example 4: fourth-order

![](/static/images/1685050076.png)

# Exercises

<pdf-reader src="/static/documents/zill-4.3.pdf" width="100%" height="900" />

# Answers

![](/static/images/1685052199.png)
![](/static/images/1685052220.png)

# Undetermined Coefficients approach

Now the book goes into a very lengthy description of the method.
I have a short attention span, so let me TLDR it for you:

Guess and pray

# Example 1: polynomials

![](/static/images/1685050763.png){width=100%}

# Example 2: trigonometric functions

![](/static/images/1685050784.png){width=100%}

# Example 3: exponentials

![](/static/images/1685050934.png){height=100%}

# Example 4: exponentials

![](/static/images/1685050976.png)

# More Examples {.nosplit}

![](/static/images/1685051003.png){width=100%}

# General method

#. Solve the homogenous equation

#. Try a linear combination of $g(x)$, $g'(x)$, $g''(x)$

#. If a term appears in both the above steps, multiply by $x^n$ with $n$ as
small as possible

# Example: guessing the form

![](/static/images/1685051379.png){width=100%}

# Example: using superposition

![](/static/images/1685051425.png){width=100%}

# Case 2

![](/static/images/1685051565.png){width=100%}

# Example 8

![](/static/images/1685051995.png){width=100%}

# Example 9

![](/static/images/1685052022.png){width=100%}

# Example 10

![](/static/images/1685052064.png){width=100%}

# Example 11

![](/static/images/1685052080.png){width=100%}

# Exercises

<pdf-reader src="/static/documents/zill-4.4.pdf" width="100%" height="900" />

# Answers

![](/static/images/1685052164.png){height=100%}

# 29/05/2023

::::: {.col}
\begin{align*}
ay'' + by' + cy = g(x)
\end{align*}

- Solve the homogeneous equation (rhs equals 0)
  - Solve auxiliary equation: $am^2 + bm + c = 0$.
  - Solution is a linear combination of
  \begin{align*}
  c_1 e^{m_1 x} + c_2 e^{m_2 x}
  \quad \text{or} \quad
  c_1 e^{m_1 x} + c_2 x e^{m_2 x}
  \text{ if } m_1 = m_2
  \end{align*}
- Find a particular solution.
  Try a linear combination of $g, g', g''$.
- Combine:
  \begin{align*}
  y = y_p + y_h
  \end{align*}
:::::

::::: {.col}
<iframe src="../index.html" width="100%" height="900">
</iframe>
:::::

# Factoring and annihilator operators

**Factoring operators**:
\begin{align*}
(D^2 + 5 D + 6) y = (D + 2) (D + 3) y
\end{align*}

**Annihilator operator**:
\begin{align*}
L(f(x)) = 0
\end{align*}

::: example
- $y = k$ is **annihilated** by $D$
- $y = x$ is **annihilated** by $D^2$
:::

::: proposition
The operator $(D - \alpha)^n$ annihilates the following functions:
\begin{align*}
e^{\alpha x}, x e^{\alpha x}, x^2 e^{\alpha x}, \dots,
x^{n - 1} e^{\alpha x}
\end{align*}
:::

# Annihilating a sum

::: proposition
Let $L_1$ and $L_2$ be two linear differential operators with constant coefficients.
If $L_1(y_1) = L_2(y_2) = 0$,
then
\begin{align*}
L_1 L_2 (y_1 + y_2) = 0
\end{align*}
:::

# Annihilator operators: example

![](/static/images/1685309898.png){width=100%}

# Annihilatore operators: second example

![](/static/images/1685310199.png)
![](/static/images/1685310223.png)

# Undetermined coefficients - annihilator method

![](/static/images/1685312227.png)

# Undetermined coefficients

![](/static/images/1685310944.png){width=100%}

# Undetermined coefficients, 2nd example

![](/static/images/1685310962.png){width=100%}

# Undetermined coefficients

![](/static/images/1685311151.png){width=100%}

# Form of a particular solution

![](/static/images/1685312191.png)

# Form of a particular solution

![](/static/images/1685312214.png)

# Exercises

<pdf-reader src="/static/documents/zill-4.5.pdf" width="100%" height="900" />

# Answers

::::: {.col}
![](/static/images/1685314249.png)
:::::

::::: {.col}
![](/static/images/1685314263.png)
:::::

# Variation of parameters

::: idea
\begin{align*}
y'' + P(x) y' + Q(x) y = f(x)
\end{align*}

Assume $y_h(x) = c_1 y_1(x) + c_2 y_2(x)$.
To solve the general ODE, we consider
\begin{align*}
y_p(x) \defeq u_1(x) y_1(x) + u_2(x) y_2(x)
\end{align*}
:::

After some long calculations...

![](/static/images/1685313060.png){width=100%}

# Variation of parameters: example

![](/static/images/1685313114.png){width=100%}

# Variation of parameters: example

![](/static/images/1685313132.png){width=100%}

No need to introduce any integration constants. Why?

#  Variation of parameters with non-elementary integral

![](/static/images/1685313616.png)

![](/static/images/1685313580.png)

# Exercises

<pdf-reader src="/static/documents/zill-4.6.pdf" width="100%" height="900" />

# Answers

![](/static/images/1685314224.png){height=100%}

# Cauchy-Euler Equations: summary

![](/static/images/1685400879.png)

Constant coefficients                                 Cauchy-Euler
----------------------                                -------------
$ay'' + by' + cy = g(x)$                              $ax^2y'' + bxy' + cy = g(x)$
$e^{mx}$                                              $x^m$
$am^2 + bm + c = 0$                                   $am^2 + (b - a)m + c = 0$
$c_1 e^{m x} + c_2 x e^{m x}$                         $c^1 x^m + c_2 x^m \ln x$
$e^{\alpha x}(c_1 \cos \beta x + c_2 \sin \beta x)$   $x^{\alpha} (c_1 \cos (\beta \ln x) + c_2 \sin (\beta \ln x)$

# Method of solution

Substitute $y = x^m$ into $ax^2 y'' + bx y' + cy = 0$.

# Distinct roots

![](/static/images/1685399497.png){width=100%}

# Repeated roots

![](/static/images/1685399524.png){width=100%}

# IVP

![](/static/images/1685399712.png){width=100%}

# Third order equation

![](/static/images/1685399740.png){width=100%}

# Variation of parameters

![](/static/images/1685400003.png)
![](/static/images/1685400013.png)

# Reduction to constant coefficients

![](/static/images/1685400064.png)

# Example

![](/static/images/1685400452.png)
![](/static/images/1685400483.png)

# Concluding remarks

![](/static/images/1685400781.png)

# Exercises

<pdf-reader src="/static/documents/zill-4.7.pdf" width="100%" height="900" />
