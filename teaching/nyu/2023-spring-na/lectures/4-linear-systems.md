---
title: Solution of linear systems of equations
output: revealjs
notes: |
  - 22/02: LU decomposition, and forward/backward substitution
...

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

Remember that the interpolating equations take a triangular form when using the Gregory-Newton basis.

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

# Recalls 25/02 {.row}

::::: {.col}

## LU decomposition

A row operation on $\mat A = \mat I \mat A$ can be performed on $\mat I$ instead.

Gaussian elimination can be used to get the inverse of a matrix in $\bigo(n^3)$ flops.

LU Decomposition
:   Partial Gaussian elimination until you get an upper-triangular matrix $U$.
    The $L$ matrix records the inverse row operations to recreate the matrix $A$.


:::::

::::: {.col}

## Midterm

- Date: 6 March 2023
- 15% of your final grade
- Chapter $1$, $2$, $3$ + LU decomposition
- Without notes or calculator
- [Spring 2023 midterm info](/teaching/nyu/2023-spring-na/midterm)

## Announcements

- Office hour(s) in person this week on Thursday
- Monte-Carlo homework due on Friday
- French sentence of the day: "Vous êtes sûr(s) que vous parlez français?"

:::::

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
        U[r, i:] -= U[i, i:] * ratio
    end
end
~~~
:::

::: proposition
The complexity of the $LU$ algorithm is $\bigo(\frac 2 3 n^3)$
:::

![](/static/images/1677026712.png){width=100%}

# Complexity of forward substitution {.split}

~~~ julia
function forward_substitution(L, b)
    x = zeros(n)
    for i in 1:n
        x[i] = (b[i] - sum(L[i,1:i-1] .* x[1:i-1])) / L[i, i]
    end
    return x
end
~~~

::: proposition
The complexity of the back/forward substitution algorithm is $n^2$.
:::

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

# Motivations {.split}

- When we attempt to input a matrix $\mat A$ in Julia, we'll actually have a perturbed matrix.
  $\mat A + \mat {\Delta A}$. How far off are we from the original matrix?

- How do we define the relative error on a **vector** $\vec x$ or $\vec b$?

- Instead of solving a system $\mat A \vec x = \vec b$, we actually solve
  $$(\mat A + \mat{\Delta A}) \vec x = \vec b + \vec {\Delta b}.$$
  Can we estimate the perturbation to the solution of the original system?

- We shall see some iterative algorithms
  $$\vec x_{k + 1} = \mat M \vec x_k = \mat M^k x_0.$$
  Will this algorithm **converge**? 
  What does it even mean?

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

::: {.proposition title="Consistency, submultiplicativity"}
Let $A \in \R^{m \times n}$ and $B \in \R^{n \times p}$.

$$\|AB\|_p \leq \|A\|_p \|B\|_p.$$
:::

We shall require all our norms to be consistent from this point on.

# Diagonalization {.split}

Let $\mat A \in \R^{n \times n}$.
Let's recall that if $\vec x \neq 0$ and $\lambda \in \C$ is such that
\begin{align}
\mat A \vec x = \lambda \vec x,
\end{align}
we say that

- $\lambda$ is an **eigenvalue** of $A$
- $\vec x$ is an **eigenvector** of $A$ associated with $\lambda$.
- $\mat A$ is **diagonalizable** if $\mat A = \mat P^{-1} \mat D \mat P$,
  for some invertible matrix $\mat P$ and a diagonal matrix $\mat D$.
- In general, $A$ is "almost" diagonalizable (Jordan form)

The eigenvalues are the roots of $\chi_{\mat A}(\lambda) = \det(\mat A - \lambda \mat I)$.

$$\spectrum \mat A = \{\lambda \in \C : \chi_{\mat A}(\lambda) = 0\}$$

::: theorem
Let $\mat A \in \R^{n \times n}$ be a **symmetric** matrix.
There is an orthogonal matrix $\mat Q \in \R^{n \times n}$ and a diagonal matrix $\mat D \in \R^{n \times n}$ such that
\begin{align}
\mat A = \mat Q^T \mat D \mat Q
\end{align}
:::

# Spectral radius {.split}

Calculating $\mat A^k$ is much easier for a diagonalizable matrix,
as
\begin{align}
\mat A^k = (\mat P^{-1} \mat D \mat P) (\mat P^{-1} \mat D \mat P) \dots (\mat P^{-1} \mat D \mat P)
= \mat P^{-1} \mat D^k \mat P.
\end{align}

::: {.definition title="Spectral radius"}
\begin{align}
\rho(\mat A) = \max_{\lambda \in \spectrum \mat A} \abs \lambda
\end{align}
:::

::: {.proposition title="Oldenburger's theorem"}
- $\norm {\mat A^k} \xrightarrow {k \to +\infty} 0 \iff \rho(A) < 1$.
- $\norm {\mat A^k} \xrightarrow {k \to +\infty} +\infty \iff \rho(A) > 1$.
:::

::: {.theorem title="Gelfand's formula"}
Let $\mat A \in \R^{n \times n}$.
For any matrix norm,
\begin{align}
\lim_{k \to +\infty} \norm {\mat A^k}^{\frac 1 k} = \rho(\mat A).
\end{align}
:::

Proof: [@vaes22, p. 174]

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

# Iterative methods: splitting [@vaes22, p. 92] {.split}

When we're dealing with very large systems $\mat A \vec x = \vec b$,
we may be ready to get an approximate solution
if this means a lower complexity.

To this end, we'll split the matrix
\begin{align}
\mat A = \mat M - \mat N.
\end{align}
so that our unknown can appear **twice**.
\begin{align}
\mat A \vec x = \vec b
\iff \mat M x = \mat N x + \vec b
\end{align}

This naturally defines an iteration
\begin{align}
\boxed{\mat M \vec x_{k + 1} = \mat N \vec x_k + \vec b}.
\end{align}

These iterations will generally be $\bigo(n^2)$ in the worst case,
as $\mat M$ will be chosen to make sure the above system can be solved efficiently.

# Iteration and fixed point problem [@vaes22, p. 92] {.split}

::: proposition
Assume that $$\mat A = \mat M - \mat N,$$
where both $\mat A$ and $\mat M$ are invertible square matrices.

The following are equivalent:

#. $\vec x$ is a solution of $\mat A \vec x = \vec b$
#. $\vec x$ is a **fixed point** of $\vec f(\vec x) = \mat M^{-1}(\mat N \vec x + \vec b)$.
:::

# Banach fixed point theorem {.split}

::: theorem
Assume that $\vec f$ satisfies
\begin{align}
\norm {\vec f^k(\vec x) - \vec f^k(\vec y)}
\leq L_k \norm {\vec x - \vec y},
\quad \sum_{k = 0}^{+\infty} L_k < +\infty.
\end{align}
Then the iteration
\begin{align}
\vec x_{k} = \vec f^{k}(\vec x_0),
\quad k > 0
\end{align}
converges towards the unique fixed point $\vec x_\star$
for any initial input $\vec x_0$.
:::

# Convergence of the splitting method [@vaes22, p. 93] {.split}

::: proposition
Assume that $$\mat A = \mat M - \mat N,$$
where both $\mat A$ and $\mat M$ are invertible square matrices.

The iteration $$\vec x_{k + 1} = \mat M^{-1} (\mat N \vec x_k + \vec b)$$ converges
to the unique solution of $\mat A \vec x = \vec b$ for every choice of $\vec x_0$
if and only if $\rho(\mat M^{-1} \mat N) < 1$.
:::

# Richardson's method [@vaes22, p. 94] {.split}


::: {.algorithm title="Richardson's method"}
Splitting
:   $$A = \underbrace{\frac 1 \omega \mat I}_{\mat M}
    - \underbrace{\left(\frac 1 \omega \mat I - \mat A\right)}_{\mat N}$$

Iteration
:   $$\vec x_{k + 1} = \vec x_k + \omega ( \vec b - \mat A \vec x_k )$$

Spectral radius
:   $$\rho(\mat M^{-1} N) = \max_{\lambda \in \spectrum A} \abs {1 - \omega \lambda}$$

Convergence
:   $$0 < \omega < \frac 2 {\lambda_\max}$$

Choice of $\omega$ for symmetric and positive definite $\mat A$
:   $$\omega = \frac 2 {\lambda_\max + \lambda_\min}
    \quad \rho = \frac {\kappa(A) - 1} {\kappa(A) + 1}$$
:::

# Richardson iteration: example {.split}

\begin{align}
\vec x_{k + 1} = \vec x_k + \omega (\vec b - \mat A \vec x_k)
\end{align}

::: example
Suppose we want to solve the following system.

\begin{align}
\begin{pmatrix}
2 & 1 & 0\\
0 & 2 & 1\\
1 & 0 & 3
\end{pmatrix}
\begin{pmatrix}
x_1 \\ x_2 \\ x_3
\end{pmatrix}
=
\begin{pmatrix}
2 \\ 1 \\ 4
\end{pmatrix}
\end{align}
:::

~~~ julia
x = [0, 0, 0]
b = [2, 1, 4]
A = [2 1 0; 0 2 1; 1 0 3]
for i in 1:100
    x = x + 0.2 * (b - A * x)
end
~~~

# Link to optimisation [@vaes22, p. 95] {.split}

When $\mat A$ is symmetric and positive definite,
solving $\mat A \vec x = \vec b$ is equivalent to minimizing
\begin{align}
f(\vec x) = \frac 1 2 \vec x^T \mat A \vec x - \vec b^T \vec x
\end{align}
as $\nabla f = \mat A \vec x - \vec b$.

The Richardson update can be written
\begin{align}
\vec x_{k + 1} = \vec x - \omega \nabla f(\vec x_k)
\end{align}

We are moving in the direction where $f$ decreases the most.
We shall encounter this idea again later.

# Bibliography
