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
