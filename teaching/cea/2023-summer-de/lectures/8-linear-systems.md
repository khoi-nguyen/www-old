---
title: "Chapter 8: Linear systems"
output: revealjs
kernel: python
...

# Linear systems

![](/static/images/1686521709.png)

# Matrix form

![](/static/images/1686521742.png)

# Example

![](/static/images/1686521764.png)

# Verification of solution

![](/static/images/1686521795.png)

# IVP and solution

![](/static/images/1686522172.png)

# Homogeneous systems

![](/static/images/1686522199.png)

# Superposition principle

![](/static/images/1686522222.png)

# Linear independence

![](/static/images/1686522366.png)
![](/static/images/1686522379.png)

# Linear independence: solution

![](/static/images/1686523770.png)

# General solution: homogeneous system

![](/static/images/1686523800.png)
![](/static/images/1686523811.png)

# General solution

![](/static/images/1686523852.png)

# General system: nonhomogenous

![](/static/images/1686523903.png)
![](/static/images/1686523917.png)

# Exercises

<pdf-reader src="/static/documents/zill-8.1.pdf" width="100%" height="900" />

# Homogeneous linear systems and eigenvalues

Let's try to solve $\mat X' = \mat A \mat X$.

Let's try a solution of the form
\begin{align*}
\mat X = \mat K e^{\lambda t}
\end{align*}

::: proposition
\begin{align*}
\mat X' = \mat A \mat X
\iff (\mat A - \lambda \mat I) \mat K = 0.
\end{align*}
:::

We call $\lambda$ an **eigenvalue**
and $\mat K$ an **eigenvector**.

# Eigenvectors and eigenvalues

# Distinct eigenvalues

![](/static/images/1686526847.png)

# Distinct eigenvalues: example

![](/static/images/1686526866.png)
![](/static/images/1686526877.png)

# 13/06

The general solution of $\vec X' = \mat A \vec X + \vec F(t)$
has the form
\begin{align*}
\vec X = \vec X_p + \underbrace{c_1 \vec X_1 + \dots + c_n \vec X_n}_{\vec X_h}.
\end{align*}

- An $n$-dim system, requires $n$ linearly independent solutions of the homogeneous system
- Linear independence is checked via the Wronskian (without derivatives)
- For each eigenpair $(\lambda, \vec K)$ of $\mat A$, $c \vec K e^{\lambda t}$ is a solution to the homogeneous equation.

## Announcements

- Karma caught up with me, I dropped my phone in the gutter. Lesson learnt, I shall not wear that T-shirt again.

# Distinct eigenvalues

![](/static/images/1686549904.png)

# Repeated eigenvalues

![](/static/images/1686550152.png)

# Repeated eigenvalues: first example

![](/static/images/1686550182.png)

# Second solution

![](/static/images/1686550217.png)

# Second example

![](/static/images/1686550250.png)
![](/static/images/1686550270.png)

# Eigenvalues of multiplicity 3

![](/static/images/1686550297.png)

# Repeated eigenvalues

![](/static/images/1686550324.png)

# Complex eigenvalues

![](/static/images/1686550360.png)

# Complex eigenvalues

![](/static/images/1686550485.png)

# Complex eigenvalues example

![](/static/images/1686550520.png)

# Exercises

<pdf-reader src="/static/documents/zill-8.2.pdf" width="100%" height="900" />

# Nonhomogeneous linear systems

\begin{align*}
\vec X' = \mat A \vec X + \vec F(t)
\end{align*}

\begin{align*}
\vec X = \vec X_p + \underbrace{c_1 \vec X_1 + \dots + c_n \vec X_n}_{\vec X_h}
\end{align*}

- Undetermined coefficients (quicker)
- Variation of parameters (more powerful)

# Undetermined coefficients

![](/static/images/1686632474.png)
![](/static/images/1686632493.png)

# Undetermined coefficients

![](/static/images/1686632532.png)
![](/static/images/1686632551.png)

# 14/06

::::: {.col}

### Homogeneous systems $\mat X' = \mat A \mat X$.

\begin{align*}
\vec X = c_1 \vec X_1 + \dots + c_n \vec X_n.
\end{align*}

\begin{align*}
\vec X_i = \vec K e^{\lambda t},
\qquad (\vec K, \lambda) \ \text{eigenpair of} \ \mat A.
\end{align*}

If we need more vectors,
\begin{align*}
\vec X_i = \vec K t e^{\lambda t} + \vec P e^{\lambda t},
\qquad \begin{cases}
(\vec K, \lambda) \ \text{eigenpair of} \ \mat A,\\
\ \vec (\mat A - \lambda \mat I) \vec P = \vec K.
\end{cases}
\end{align*}

## Finding $\vec X_p$

- Method of undetermined coefficients (exactly like for second order systems)
- Variation of parameters

:::::

::::: {.col}

### Variation of parameters

\begin{align*}
\vec X_p
&= u_1(t) \vec X_1 + \dots + u_n(t) \vec X_n\\
&= \underbrace{\begin{pmatrix}
\vec X_1 & \dots & \vec X_n
\end{pmatrix}}_{\mat \Phi(t)}
\underbrace{
\begin{pmatrix}
u_1(t)\\
\vdots\\
u_n(t)
\end{pmatrix}
}_{\vec U(t)}
\end{align*}

We find $\vec U(t)$ so that
\begin{align*}
\vec X_p' = \mat A \vec X_p + \vec F(t).
\end{align*}
:::::

# Variation of parameters

\begin{align*}
\vec X_p = \mat \Phi(t) \vec U(t),
\quad \vec U(t) \defeq (u_1(t), \dots, u_n(t))^T
\end{align*}

Substituting into
$\vec X_p' = \mat A \vec X_p + \vec F(t)$,
we obtain
\begin{align*}
\vec X_p = \mat \Phi(t) \int \mat \Phi^{-1}(t) \mat F(t) \dd t.
\end{align*}

# Variation of parameters example

![](/static/images/1686633550.png)

# Variation of parameters part II

![](/static/images/1686633621.png)
![](/static/images/1686633631.png)

# IVP

![](/static/images/1686633646.png)

# Exercises

<pdf-reader src="/static/documents/zill-8.3.pdf" width="100%" height="900" />

# Euler's method

\begin{align*}
\begin{cases}
y' &= f(x, y)\\
y(x_0) &= y_0\\
\end{cases}
\end{align*}

By Taylor,
\begin{align*}
y(x + h)
&= y(x) + y'(x) h + \bigo(h^2)\\
&= y(x) + h f(x, y) + \bigo(h^2)
\end{align*}

::: {.info title="Euler's method"}
\begin{align*}
x_{k + 1} &\defeq x_k + h\\
\widehat y_{k + 1} &\defeq \widehat y_k + h f(x_k, \widehat y_k)
\end{align*}
:::

# Improving Euler

\begin{align*}
y(x + h)
&= y(x) + h y'(x) + \frac {h^2} 2 y''(x) + \bigo(h^3)\\
&= y(x) + h f(x, y) + \frac {h^2} 2 \left[\partial_x f(x, y) + \partial_y f(x, y) f(x, y)\right] + \bigo(h^3)
\end{align*}

\begin{align*}
y(x) + &h\left(w_1 f(x, y) + w_2 f(x + \alpha h, y + \beta h k)\right)\\
&= y(x) + h \left(w_1 f(x, y) + w_2 f(x, y) + w_2 \alpha h \partial_x f(x, y) + w_2 \beta h k \partial_y f(x, y)\right) + O(h^3)\\
&= y(x) + h (w_1 + w_2) f(x, y)
+ h^2 \left(w_2 \alpha \partial_x f(x, y) + w_2 \beta k \partial_y f(x, y) \right)
+ O(h^3)
\end{align*}

# RK-4

![](/static/images/1686701950.png)
