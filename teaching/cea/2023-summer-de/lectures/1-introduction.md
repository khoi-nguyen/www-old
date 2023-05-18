---
title: "Chapter 1: Introduction to Differential Equations"
output: revealjs
kernel: python
notes: |
  - 09/05: type, order, linearity, implicit form, and solutions (1-20)
...

# Introduction

- My name is **Khôi Nguyễn**^[Don't ask me how to pronounce it, I don't know].

- I'm a **software developer** and **lecturer**.

- My specialty in maths was **pseudo-differential equations**.

- I speak English, French, Spanish^[But I sound foreign in all of them].

# Lecture notes and resources

- Lecture notes with annotations available on my website
- Source code available on [Github](https://github.com/khoi-nguyen/www)

Website
:    <https://nguyen.me.uk>

Textbook
:    Differential Equations with Boundary-Value problems, D.G. Zill

# Short introduction

::::: text-center
![](https://upload.wikimedia.org/wikipedia/commons/3/3b/Portrait_of_Sir_Isaac_Newton%2C_1689.jpg){height=300}
:::::

::: {.quote title="Albert Einstein"}
In order to put his system into mathematical form at all,
Newton had to devise the concept of differential quotients and
propound the laws of motion in the form of total **differential 
equations**—perhaps the **greatest advance in thought** that a
single individual was ever privileged to make.
:::

# Definition and terminology p. 3

::: definition
An **equation** containing the **derivative** of one or more **unknown functions**
with respect to one or more independent variable.
:::

::: example
\begin{align*}
\frac {\dd x} {\dd t} + \frac {\dd y} {\dd t} = 2 x + y
\end{align*}

\begin{align*}
\frac {\partial^2 u} {\partial x^2}
+ \frac {\partial^2 u} {\partial y^2}
+ \frac {\partial^2 u} {\partial z^2}
= 0
\end{align*}
:::

# Classification p. 5

- **Type**: *partial* $\frac {\partial} {\partial x}$ or *ordinary* $\frac {\dd} {\dd x}$

\begin{align*}
\underbrace{
\frac {\partial^2 u} {\partial t^2} = c^2 \frac {\partial^2 u} {\partial x^2}
}_{\text{PDE}}
\qquad
\underbrace{\frac {\dd x} {\dd t} = 2 x + t}_{\text{ODE}}
\end{align*}

- **Order**: order of highest derivative

\begin{align*}
m \underbrace{\frac {\dd^2 x} {\dd t^2}}_{\text{order}\ 2} = \frac {G M m} {x^2},
\qquad
\underbrace{\frac {\dd^2 y} {\dd x^2}}_{\text{order}\ 2} +
5 \left(\underbrace{\frac {\dd y} {\dd x}}_{\text{order}\ 1}\right)^3 - 4y= e^x
\end{align*}

- **Linear** or **non-linear**:

\begin{align*}
a_n(x) \frac {\dd^n y} {\dd x^n}
+ a_{n - 1}(x) \frac {\dd^{n - 1} y} {\dd x^{n - 1}}
+ \dots
+ a_1(x) \frac {\dd y} {\dd x}
= g(x).
\end{align*}

# Examples: type

![](/static/images/1684185425.png)

# Differential form of an ODE

We'll often write $\dd y = y' \dd x.$

::: example
- Transform
\begin{align*}
(y - x) \dd x + 4 x \dd y = 0
\end{align*}
back into a "more normal" form.

- Convert
\begin{align*}
6xy + \frac {\dd y} {\dd x} + x^2 + y^2 = 0
\end{align*}
into a *differential form*.
:::

# Normal form p. 5

General form
:   \begin{align*}
    F(x, y, y', \dots, y^{(n)}) = 0
    \end{align*}

Normal form
:   \begin{align*}
    \frac {\dd^n y} {\dd x} = f(x, y, y', \dots, y^{(n - 1)})
    \end{align*}

::: example

\begin{align*}
\frac {\dd y} {\dd x} = f(x, y)
\qquad
\frac {\dd^2 y} {\dd x^2} = f(x, y, y')
\end{align*}
are normal forms to represent first- and second-order ODEs.
:::

# Normal form: example p. 5

![](/static/images/1684249471.png)

# Linear and non-linear p. 6

![](/static/images/1684249675.png)

# Solution of an ODE p. 6

::: definition
A **solution** of a differential equation
\begin{align*}
F(x, y, y', \dots, y^{(n)}) = 0
\end{align*}
is a function $\phi$ that possesses at least $n$ derivatives
and for which
\begin{align*}
F(x, \phi(x), \phi'(x), \dots, \phi^{(n)}(x)) = 0
\end{align*}
for all $x$ in some interval $I$.
:::

# Example: verification of a solution p. 7

![](/static/images/1684298170.png)

# Solution vs function p. 7

![](/static/images/1684298265.png)

# Implicit solutions

::: definition
A relation $G(x, y) = 0$ is an **implicit solution** of an ODE on $I$
provided that there is at least one function which satisfies
the relation as well as the differential equation on $I$.
:::

![](/static/images/1684298483.png)
![](/static/images/1684298521.png)

# Particular solutions

![](/static/images/1684298673.png)

# Using different symbols

![](/static/images/1684298757.png)

# Piecewise-defined solution

![](/static/images/1684298789.png)

# Systems of ODEs

\begin{align*}
\begin{cases}
\frac {\dd x} {\dd t} &= f(t, x, y)\\
\frac {\dd y} {\dd t} &= g(t, x, y)
\end{cases}
\end{align*}

A **solution** is a **pair** of function
\begin{align*}
x = \phi_1(t),
\quad
y = \phi_2(t)
\end{align*}
which satisfy each equation on a common interval.

# Exercises p. 12

<pdf-reader src="/static/documents/zill-1.1.pdf" width="100%" height="900" />

# 18 May 2023

::::: {.col}

## Classification

- **Type**: *partial* $\frac {\partial} {\partial x}$ or *ordinary* $\frac {\dd} {\dd x}$

\begin{align*}
\underbrace{
\frac {\partial^2 u} {\partial t^2} = c^2 \frac {\partial^2 u} {\partial x^2}
}_{\text{PDE}}
\qquad
\underbrace{\frac {\dd x} {\dd t} = 2 x + t}_{\text{ODE}}
\end{align*}

- **Order**: order of highest derivative

\begin{align*}
m \underbrace{\frac {\dd^2 x} {\dd t^2}}_{\text{order}\ 2} = \frac {G M m} {x^2},
\qquad
\underbrace{\frac {\dd^2 y} {\dd x^2}}_{\text{order}\ 2} +
5 \left(\underbrace{\frac {\dd y} {\dd x}}_{\text{order}\ 1}\right)^3 - 4y= e^x
\end{align*}

- **Linear** or **non-linear**:

\begin{align*}
a_n(x) \frac {\dd^n y} {\dd x^n}
+ a_{n - 1}(x) \frac {\dd^{n - 1} y} {\dd x^{n - 1}}
+ \dots
+ a_1(x) \frac {\dd y} {\dd x}
+ a_0(x) y
= g(x).
\end{align*}

:::::

::::: {.col}

## Solution

#. Calculate the required derivatives
#. Substitute into lhs, rhs and check equality

### French sentence of the day

Before I teach you how to order alcohol,
I need to ensure you can do so without getting in trouble with the law,
or you might miss differential equations the next day
(we don't want that).

**Je veux parler à mon avocat∙e** - *I want to speak to my lawyer*.
:::::

# Initial Value problems

Solving an ODE subject to **initial conditions**.

\begin{align*}
\begin{cases}
\frac {\dd^n y} {\dd x^n} = f(x, y, y', \dots, y^{(n - 1)})\\
y(x_0) = y_0, y'(x_0) = y_1
\end{cases}
\end{align*}

We call them **IVPs**.

# Geometric interpretation p. 15

![](/static/images/1684305150.png)

# Example of IVPs

![](/static/images/1684305198.png)

# Interval of definition

::: col
![](/static/images/1684305264.png)
:::

::: col
![](/static/images/1684305297.png)
:::

# Solving a second order IVPs

![](/static/images/1684305348.png)

# Existence and uniqueness p. 17

Two (actually three) questions arise when considering IVPs.

::: question
- Is there a solution?

- Is it **unique**?
:::

# IVP with several solutions p. 17

![](/static/images/1684305786.png)

# Existence and uniqueness

::: {.theorem title="Picard, Lindelöf, Lipschitz, Cauchy"}
If $f(x, y)$ and $\partial f / \partial y$ are continuous around $(x_0, y_0)$,
then locally around $x_0$,
the solution of
\begin{align*}
\begin{cases}
y(x) = f(x, y)\\
y(x_0) = y_0
\end{cases}
\end{align*}
exists and is unique.
:::

::: info
To check the solution exists:

- Calculate $\partial f / \partial y$ exists
- Check that both $f(x, y)$ and $\partial f / \partial y$ are **continuous**
  at the initial value.
:::

::: remark
:::

# Picard-Lindelöf-Cauchy-Lipschitz theorem

::: {.theorem title="Picard, Lindelöf, Lipschitz, Cauchy"}
If $f(x, y)$ and $\partial f / \partial y$ are continuous around $(x_0, y_0)$,
then locally around $x_0$,
the solution of
\begin{align*}
\begin{cases}
y(x) = f(x, y)\\
y(x_0) = y_0
\end{cases}
\end{align*}
exists and is unique.
:::

::: {.proof title="Idea of the proof"}
\begin{align*}
y_0(x) &\defeq y_0\\
y_1(x) &\defeq y_0 + \int_{x_0}^x f(t, y_0) \dd t\\
\vdots \\
y_{k + 1}(x) &\defeq y_0 + \int_{x_0}^x f(t, y_k(t)) \dd t\\
\end{align*}
:::

# Existence and uniqueness: example

![](/static/images/1684306274.png)

# Exercises 1.2

Selection: 5, 9, 13, 15, 17, 23, 31, 33.

<pdf-reader src="/static/documents/zill-1.2.pdf" width="100%" height="870" />

# Answers

![](/static/images/1684394613.png)

# ODES as mathematical models

![](/static/images/1684388169.png){width=100%}

# Population dynamics

::: {.info name="Population growth (Malthus)"}
The rate at which the population grows is proportional to its size.
:::

$P(t)$: population at time $t$

\begin{align*}
\underbrace{\frac {\dd P} {\dd t}}_{\text{rate of growth}}
\overbrace{= k}^{\text{proportional} \ (k > 0)}
P
\end{align*}

::: remark
Doesn't take into account death, the ~~wall~~ ~~fence~~ immigration.
:::

Radioactive decay is the same, but with negative $k < 0$.

::: {.info name="Radioactive decay (carbon dating)"}
Since The Flood^[Please don't think I'm a young earth creationist],
the rate at which the nuclei of a substance decay is proportional
to the amount of the substance remaining.
:::

# Population dynamics: exercises

![](/static/images/1684388617.png){height=900}

# Newton's law of cooling

- $T(t)$: temperature of a body at time $t$
- $T_m$: temperature of surrounding medium

::: {.info name="Newton's law of cooling"}
The rate at which the temperate of a body changes is proportional to
the temperature difference between the body and the medium.
:::

# Newton's law of cooling/warming: exercises

![](/static/images/1684388807.png){height=900}

# Spread of a disease

::: {.info name="Assumtion(s)"}
The rate at which the disease spreads is proportional to the number
of interactions between the contaminated group and the others.
:::

![](/static/images/1684389898.png)

# Mixture: example

::::: {.col}
![](/static/images/1684393540.png){height=900}
:::::

::::: {.col}
$A$: amount of salt
\begin{align*}
\frac {\dd A} {\dd t} = \text{salt input rate} - \text{salt output rate}
\end{align*}
:::::

# Mixture: exercises

![](/static/images/1684391260.png)

# Draining a tank

::::: {.col}
![](/static/images/1684393808.png)
:::::


::::: {.col}
::: {.info name="Torricelli's law"}
The speed of efflux of water is the speed that a drop of water
would acquire in falling freely from a height equal to that of the tank.
:::
$V(t)$: Volume in the tank.

\begin{align*}
\frac {\dd V} {\dd t} = -A_h \sqrt {2 g h}
\implies \frac {\dd h} {\dd t}
\end{align*}
:::::

# Circuits

::::: {.col}
::: {.info name="Kichhoff's second law"}
The impressed voltage on a closed loop must equal the sum of the voltage drops.
:::

\begin{align*}
L \frac {\dd^2 q} {\dd t^2} + R \frac {\dd q} {\dd t} + \frac 1 C q = E(t).
\end{align*}
:::::

::::: {.col}
![](/static/images/1684392515.png){height=900}
:::::

# Circuits: exercises

![](/static/images/1684393211.png){width=80%}
![](/static/images/1684393293.png){width=40%}


# Falling bodies with air resistance

::: {.info name="Assumptions"}
Air resistance is proportional to speed.
:::

\begin{align*}
m \frac {\dd v} {\dd t} = mg - kv
\end{align*}

![](/static/images/1684392782.png)

# Exercises

<pdf-reader src="/static/documents/zill-1.3.pdf" width="100%" height="900" />

# Answers

![](/static/images/1684394576.png)
![](/static/images/1684394592.png)
