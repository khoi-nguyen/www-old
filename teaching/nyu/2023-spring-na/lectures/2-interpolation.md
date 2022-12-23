---
title: "Chapter 2: Interpolation and Approximation"
output: revealjs
private: true
...

# Interpolation {.split}

::: {.block title="The interpolation problem"}
Given $\{(x_i, u_i) \in \R^2 : 0 \leq i \leq n\}$,
can we find a polynomial $\widehat u$ of degree $n$ such that
$$\widehat u (x_i) = u_i$$
for each $i = 0, \dots, n$?
:::

::: example
Find the linear function $\widehat u$ that goes through
$$(x_1, u_1), \quad (x_2, u_2).$$
:::

# The Vandermonde matrix {.split}

$$\widehat u(x) = \alpha_0 + \alpha_1 x + \dots \alpha_n x^n$$

The system $\widehat u(x_i) = u_i$ takes the following matrix form

\begin{align}
\underbrace{
\begin{pmatrix}
  1 & x_0 & \dots & x_0^n\\
  1 & x_1 & \dots & x_1^n\\
  \vdots & \vdots & & \vdots\\
  1 & x_n & \dots & x_n^n\\
\end{pmatrix}
}_{\text{Vandermonde matrix}}
\begin{pmatrix}
\alpha_0 \\ \alpha_1 \\ \vdots \\ \alpha_n
\end{pmatrix}
=
\begin{pmatrix}
u_0 \\ u_1 \\ \vdots \\ u_n
\end{pmatrix}
\end{align}

::: proposition
If the points $x_0, \dots, x_n$ are **distinct**,
the Vandermonde matrix is invertible
and the system above has a **unique** solution.
:::

# The Vandermonde matrix with another base {.split}

Note that we could have taken another basis of $P_n$:
$$\widehat u(x) = \alpha_0 \varphi_0(x) + \alpha_1 \varphi_1(x) + \dots \alpha_n \varphi_n(x).$$

The system associated with our interpolation problem becomes

\begin{align}
\begin{pmatrix}
  \varphi_0(x_0) & \varphi_1(x_0) & \dots & \varphi_n(x_0)\\
  \varphi_0(x_1) & \varphi_1(x_1) & \dots & \varphi_n(x_1)\\
  \vdots & \vdots & & \vdots\\
  \varphi_0(x_n) & \varphi_1(x_n) & \dots & \varphi_n(x_n)\\
\end{pmatrix}
\begin{pmatrix}
\alpha_0 \\ \alpha_1 \\ \vdots \\ \alpha_n
\end{pmatrix}
=
\begin{pmatrix}
u_0 \\ u_1 \\ \vdots \\ u_n
\end{pmatrix}
\end{align}

::: question
Can we chose $\varphi_i$ so that the above matrix is easily invertible?
:::

We will try to have $\varphi_i(x_j) = \delta_{ij}$ (identity matrix).

# Lagrange interpolation formula {.split}

Define
$$\phi_i(x) = \prod_{\substack{j = 0\\ j \neq i}} (x - x_j),
\quad i = 0, \dots, n.$$

We easily check that $\phi_i(x_j) = 0$ when $i \neq j$.
As $\phi_i(x_j)$

::: {.definition title="Lagrange polynomials"}
$$\varphi_i(x) = \frac{
\prod_{j \neq i} (x - x_j)
}{
\prod_{j \neq i} (x_i - x_j)
}$$
:::
