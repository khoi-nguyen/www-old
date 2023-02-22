---
title: Solution of linear systems of equations
output: revealjs
notes: |
  - 22/02: LU decomposition, and forward/backward substitution
...

# Norms [@vaes22, p. 164] {.split}

A norm is a **distance** on a vector space that behaves well with the vector space structure.

::: {.definition title="Norm"}
A norm on a vector space $X$ is a function $\| \cdot \| V \to \R$ such that

Positivity
:   $$x \in V \setminus \{0\} \implies \|x\| > 0$$

Homogeneity
:   $$c \in \R, x \in V \implies \| c x \| = |c| \|x\|$$

Triangular inequality
:   $$x, y \in V \implies \|x + y\| \leq \|x\| + \|y\|$$
:::

$$d(x, y) = \|x - y\|$$

Norms are interesting because they define a good notion of convergence
on finite dimensional vector spaces:

$$x_n \xrightarrow{n \to +\infty} x \Longleftrightarrow \lim_{n \to +\infty} \|x_n - x\| = 0.$$

# Vector norms [@vaes22, p. 168] {.split}

\begin{align}
\|x\|_p &= \sqrt[p] {\sum_{i = 1}^n |x_i|^p}\\
\|x\|_{\infty} &= \max \{ |x_1|, \dots, |x_n| \}
\end{align}

The default norm will be the Euclidean $(p = 2)$ one, i.e.
\begin{align}
\|x\| = \|x\|_2.
\end{align}

In Julia, the **vector** norm of a vector can be calculated via
`norm(A, p::Real=2)`{.julia} from `LinearAlgebra`.

![](/static/images/1677059423.png){width=100%}

# Matrix norms [@vaes22, p. 168] {.split}

::: {.definition title="Operator norm"}
Let $A \in \R^{m \times n}$.
We define
\begin{align}
\|A\|_{\alpha, \beta} = \sup_{\|x\|_\beta \leq 1} \|A x\|_\alpha
\end{align}
:::

::: {.definition title="p-norm"}
Let $A \in \R^{m \times n}$ and $p \in [1, +\infty]$.
\begin{align}
\|A\|_{p} = \sup_{\|x\|_p \leq 1} \|A x\|_p.
\end{align}

As usual, we shall write $\|A\| = \|A\|_2.$.
:::

In Julia, you can use `opnorm(A::AbstractMatrix, p::Real=2)`{.julia} from `LinearAlgebra`.

::: {.proposition title="Submultiplicativity"}
Let $A \in \R^{m \times n}$ and $B \in \R^{n \times p}$.

$$\|AB\|_p \leq \|A\|_p \|B\|_p.$$
:::

If $A$ is diagonalizable, then $\|A\|_{2} = \lambda_{\max}$

# Motivations {.split}

When we want to solve $A x = b$,
round-off errors will make us solve the perturbed system
$$(A + \Delta A) x = b + \Delta b$$
instead, which will lead us to $x + \Delta x$ as a solution,
with $x$ being the true solution to the original system.

::: question
How can we estimate the **relative error** $\frac {\|\Delta x\|} {\|x\|}$
in terms of the relative errors
$\frac {\|\Delta A\|} {\|A\|}$, $\frac {\|\Delta b\|} {\|b\|}$?
:::

Note that we needed norms to have a notion of error.

# Condition number of a matrix [@vaes22, p. 80] {.split}

::: definition
$$\kappa_p(A) = \|A\|_p \|A^{-1}\|_p$$

As usual, we let $\kappa(A) = \kappa_2(A)$.
:::

#### Properties

- $\kappa(A) \geq 1$
- $\kappa(I) = 1$
- $\kappa(\lambda A) = \kappa(A)$ (relative errors!)
- The bigger the number is, the more it is **sensitive to round-off errors**.
- In Julia, you can use
  `cond(M, p)`{.julia} or `cond(M)`{.julia} (by default, `p = 2`{.julia})
  from the standard library `LinearAlgebra`.

# Perturbation of the right hand side [@vaes22, p. 78] {.split}

::: proposition
Let $x + \Delta x$ denote the solution to the perturbed equation
$$A(x + \Delta x) = b + \Delta b.$$
The following inequality holds
$$
\frac {\|\Delta x\|} {\|x\|} \leq \kappa(A) \frac {\|\Delta b\|} {\|b\|}.
$$
:::

# Perturbation of the matrix [@vaes22, p. 79] {.split}

::: proposition
Let $x + \Delta x$ denote the solution to the perturbed equation
$$(A + \Delta A)(x + \Delta x) = b.$$
If $A$ is invertible and $\Delta A < \frac 1 2 \|A^{-1}\|^{-1}$, then
$$
\frac {\|\Delta x\|} {\|x\|} \leq 2 \kappa(A) \frac {\|\Delta A\|} {\|A\|}
$$
:::

# Example (condition number) [@vaes22, p. 80] {.split}

::: example
Consider the system with the perturbed matrix
$$
(A + \Delta A) \begin{pmatrix}x_1 \\ x_2\end{pmatrix},
\qquad
A = \begin{pmatrix}1 & 0 \\ 0 & 0.01\end{pmatrix},
\quad
\Delta A = \begin{pmatrix}0 & 0\\ 0 & \epsilon\end{pmatrix},
$$
where $0 < \epsilon \ll 0.01$.
:::

# Systems associated with triangular matrices {.split}

::: example
\begin{align}
\begin{pmatrix}
1 & 2 & 3\\
0 & 4 & 5\\
0 & 0 & 6
\end{pmatrix}
\begin{pmatrix}
x \\ y \\ z
\end{pmatrix}
=
\begin{pmatrix}
14 \\ 23 \\ 18
\end{pmatrix}
\end{align}
:::

# Gregory-Newton {.split}

Remember that interpolating equations take a triangular form when using the Gregory-Newton basis.

::: example
Find the polynomial of degree $2$ going
through $(0, 1)$, $(1, 5)$, $(2, 11)$.
:::

$$\widehat u(x) = \alpha_0 + \alpha_1 x + \alpha_2 x (x - 1)$$

\begin{align}
\begin{pmatrix}
1 & 0 & 0\\
1 & 1 & 0\\
1 & 2 & 2
\end{pmatrix}
\begin{pmatrix}
\alpha_0 \\ \alpha_1 \\ \alpha_2
\end{pmatrix}
=
\begin{pmatrix}
1 \\ 5 \\ 11
\end{pmatrix}
\end{align}

# Forward and backward substitution {.row}

::::: col

\begin{align}
\underbrace{
\begin{pmatrix}
l_{1,1} & 0 & 0 & \dots & 0\\
l_{2,1} & l_{2,2} & 0 & \dots & 0\\
l_{3,1} & l_{3,2} & l_{3,3} & \dots & 0\\
\vdots & \vdots & \vdots & \vdots & \vdots\\
l_{n,1} & l_{n,2} & l_{n,3} & \dots & l_{n,n}
\end{pmatrix}
}_{L}
\begin{pmatrix}
x_1 \\ x_2 \\ x_3 \\ \vdots \\ x_n
\end{pmatrix}
=
\begin{pmatrix}
b_1 \\ b_2 \\ b_3 \\ \vdots \\ b_n
\end{pmatrix}
\end{align}

\begin{align}
x_1 &= \frac {b_1} {l_{1, 1}}\\
x_2 &= \frac {b_2 - l_{2, 1} x_1} {l_{2, 2}}\\
x_i &= \frac {b_i - \sum_{j = 1}^{i - 1} l_{i, j} x_j} {l_{i, i}}
\end{align}

~~~ julia
function forward_substitution(L, b)
    x = zeros(n)
    for i in 1:n
        x[i] = (b[i] - sum(L[i,1:i-1] .* x[1:i-1])) / L[i, i]
    end
    return x
end
~~~

:::::

::::: col
::: exercise
Write a code in Julia that solves $Ux = b$,
where $U$ is *upper*-triangular.
:::

::: proposition
The complexity of the back/forward substitution algorithm is $n^2$.
:::

:::::

# Row operations {.split}

::: remark
Instead of performing a row operation on $A$,
we can perform it on the identity matrix $I$
and multiply it on the left.
:::

::: example
Calculate and interpret
\begin{align}
\begin{pmatrix}
1 & 0 & 0\\
-4 & 1 & 0\\
0 & 0 & 1\\
\end{pmatrix}
\begin{pmatrix}
1 & 2 & 3\\
4 & 5 & 6\\
7 & 8 & 9\\
\end{pmatrix}
\end{align}
:::

::: question
What is the inverse of
\begin{align}
\begin{pmatrix}
1 & 0 & 0\\
-4 & 1 & 0\\
0 & 0 & 1\\
\end{pmatrix}?
\end{align}
:::

# LU decomposition: Gaussian algorithm [@vaes22, p. 82] {.split}

::: example
Write
\begin{align}
A = \begin{pmatrix}
1 & 1 & 1\\
1 & -2 & 3\\
2 & 3 & 1
\end{pmatrix}
\end{align}
as a product of a lower triangular matrix $L$
with an upper triangular matrix $U$.
:::

# Example: solving a system after a LU decomposition {.split}

::: example
\begin{align}
\begin{pmatrix}
1 & 1 & 1\\
1 & -2 & 3\\
2 & 3 & 1
\end{pmatrix}
\begin{pmatrix}
x \\ y \\ z
\end{pmatrix}
=
\begin{pmatrix}
4 \\ -6 \\ 7
\end{pmatrix}
\end{align}
:::

# Exercise: solving a system after a LU decomposition {.split}

::: {.exercise}
Use a LU decomposition to solve the following system:
\begin{align}
\begin{cases}
2x_1 - x_2 + 3x_3 &= 4\\
4x_1 + 2x_2 + x_3 &= 7\\
-6x_1 - x_2 + 2 x_3 &= -5
\end{cases}
\end{align}
:::

# LU decomposition in Julia [@vaes22, p. 85] {.split}

::: {.algorithm title="LU decomposition"}
~~~ julia
L = [i == j ? 1.0 : 0.0 for i in 1:n, j in 1:n]
U = copy(A)
for i in 1:n-1
    for r in i+1:n
        U[i, i] == 0 && error("Pivotal entry is zero!")
        ratio = U[r, i] / U[i, i]
        L[r, i] = ratio
        U[r, i:end] -= U[i, i:end] * ratio
    end
end
~~~
:::

![](/static/images/1677026712.png){width=100%}

# Cholesky decomposition [@vaes22, p. 89] {.split}

::: {.proposition title="Cholesky factorisation"}
If $A$ is symmetric and positive definite,
then there exists a lower-triangular matrix $C \in \R^{n \times n}$ such that
$$A = C C^T.$$
:::

# Example {.split}

::: example
Find the Cholesky decomposition of
$$\begin{pmatrix}
4 & 12 & -16\\
12 & 37 & -43\\
-16 & -43 & 98
\end{pmatrix}$$
:::

# Bibliography
