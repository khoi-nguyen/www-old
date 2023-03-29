---
title: "Chapter 4: Solution of linear systems of equations"
output: revealjs
notes: |
  - 22/02: LU decomposition, and forward/backward substitution
  - 27/02: complexity for LU, Cholesky, norms and spectrum (9-19)
  - 01/03: condition number, Richardson, convergence (20-30)
  - 03/03: stopping criterion, splitting, Jacobi (31-38)
  - 08/03: midterm, Gauss-seidel, relaxation method (until 46)
  - 20/03: Richardson, steepest descend, conjugate gradients
...

# Systems associated with triangular matrices {.split}

::: example
\begin{align*}
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
\end{align*}
:::

# Gregory-Newton {.split}

Remember that the interpolating equations take a triangular form when using the Gregory-Newton basis.

::: example
Find the polynomial of degree $2$ going
through $(0, 1)$, $(1, 5)$, $(2, 11)$.
:::

$$\widehat u(x) = \alpha_0 + \alpha_1 x + \alpha_2 x (x - 1)$$

\begin{align*}
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
\end{align*}

# Forward and backward substitution

::::: col

\begin{align*}
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
\end{align*}

\begin{align*}
x_1 &= \frac {b_1} {l_{1, 1}}\\
x_2 &= \frac {b_2 - l_{2, 1} x_1} {l_{2, 2}}\\
x_i &= \frac {b_i - \sum_{j = 1}^{i - 1} l_{i, j} x_j} {l_{i, i}}
\end{align*}

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
\begin{align*}
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
\end{align*}
:::

::: question
What is the inverse of
\begin{align*}
\begin{pmatrix}
1 & 0 & 0\\
-4 & 1 & 0\\
0 & 0 & 1\\
\end{pmatrix}?
\end{align*}
:::

# LU decomposition: Gaussian algorithm [@vaes22, p. 82] {.split}

::: example
Write
\begin{align*}
A = \begin{pmatrix}
1 & 1 & 1\\
1 & -2 & 3\\
2 & 3 & 1
\end{pmatrix}
\end{align*}
as a product of a lower triangular matrix $L$
with an upper triangular matrix $U$.
:::

# Example: solving a system after a LU decomposition {.split}

::: example
\begin{align*}
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
\end{align*}
:::

# Exercise: solving a system after a LU decomposition {.split}

::: {.exercise}
Use a LU decomposition to solve the following system:
\begin{align*}
\begin{cases}
2x_1 - x_2 + 3x_3 &= 4\\
4x_1 + 2x_2 + x_3 &= 7\\
-6x_1 - x_2 + 2 x_3 &= -5
\end{cases}
\end{align*}
:::

# Recalls 25/02

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
If $\mat A$ is symmetric and positive definite,
then there exists a lower-triangular matrix $\mat C \in \R^{n \times n}$ such that
$$\mat A = \mat C \mat C^T.$$
:::

::: {.remark title="Link between Cholesky and LU"}
\begin{align*}
\mat C = \mat L \sqrt {\mat D},
\end{align*}
where $\mat D$ is a diagonal matrix whose entries are the same as $\mat A = \mat L \mat U$.
:::

In Julia, you can use `cholesky` from `LinearAlgebra`.

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

\begin{align*}
\|x\|_p &= \sqrt[p] {\sum_{i = 1}^n |x_i|^p}\\
\|x\|_{\infty} &= \max \{ |x_1|, \dots, |x_n| \}
\end{align*}

The default norm will be the Euclidean $(p = 2)$ one, i.e.
\begin{align*}
\|x\| = \|x\|_2.
\end{align*}

In Julia, the **vector** norm of a vector can be calculated via
`norm(A, p::Real=2)`{.julia} from `LinearAlgebra`.

![](/static/images/1677059423.png){width=100%}

# Matrix norms [@vaes22, p. 168] {.split}

::: {.definition title="Operator norm"}
Let $A \in \R^{m \times n}$.
We define
\begin{align*}
\|A\|_{\alpha, \beta} = \sup_{\|x\|_\beta \leq 1} \|A x\|_\alpha
\end{align*}
:::

::: {.definition title="p-norm"}
Let $A \in \R^{m \times n}$ and $p \in [1, +\infty]$.
\begin{align*}
\|A\|_{p} = \sup_{\|x\|_p \leq 1} \|A x\|_p.
\end{align*}

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
\begin{align*}
\mat A \vec x = \lambda \vec x,
\end{align*}
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
\begin{align*}
\mat A = \mat Q^T \mat D \mat Q
\end{align*}
:::

# Spectral radius {.split}

Calculating $\mat A^k$ is much easier for a diagonalizable matrix,
as
\begin{align*}
\mat A^k = (\mat P^{-1} \mat D \mat P) (\mat P^{-1} \mat D \mat P) \dots (\mat P^{-1} \mat D \mat P)
= \mat P^{-1} \mat D^k \mat P.
\end{align*}

::: {.definition title="Spectral radius"}
\begin{align*}
\rho(\mat A) = \max_{\lambda \in \spectrum \mat A} \abs \lambda
\end{align*}
:::

::: {.proposition title="Oldenburger's theorem"}
- $\norm {\mat A^k} \xrightarrow {k \to +\infty} 0 \iff \rho(A) < 1$.
- $\norm {\mat A^k} \xrightarrow {k \to +\infty} +\infty \iff \rho(A) > 1$.
:::

::: {.theorem title="Gelfand's formula"}
Let $\mat A \in \R^{n \times n}$.
For any matrix norm,
\begin{align*}
\lim_{k \to +\infty} \norm {\mat A^k}^{\frac 1 k} = \rho(\mat A).
\end{align*}
:::

Proof: [@vaes22, p. 174]

# Recalls 01/03

::::: {.col}

### Linear systems

- LU decomposition $\frac 2 3 n^3 + \bigo(n^2)$
- Cholesky decomposition $\frac 1 3 n^3 + \bigo(n^2)$
- Forward/backward substitution: $n^2$

### Powers of matrices

\begin{align*}
\mat A \sim
\begin{pmatrix}
\lambda_1 & \star & 0 & 0 & \dots & 0 & 0 & 0\\
0 & \lambda_2 & \star & 0 & \dots & 0 & 0 & 0\\
0 & 0 & \lambda_3 & \star & \dots & 0 & 0 & 0\\
\vdots & \vdots & \vdots & \vdots & & \vdots & \vdots & \vdots\\
0 & 0 & 0 & 0 & \dots & 0 & \lambda_{n - 2} & \star & 0\\
0 & 0 & 0 & 0 & \dots & 0 & 0 & \lambda_{n - 1} & \star\\
0 & 0 & 0 & 0 & \dots & 0 & 0 & 0 & \lambda_n\\
\end{pmatrix}
\end{align*}

- $\norm {A^k} \to 0 \iff \rho(A) < 1$
- $\rho(A) \leq \norm {A}_p$
- In particular, $\norm {A}_p < 1 \implies \norm {A^k} \to 0$
:::::

::::: {.col}

### Midterm

- Next Monday (6/3 or 3/6 or / 3 6)
- Chapter 1, 2, 3 + LU

### Announcements

- French sentence of the day: je refuse de répondre conformément aux droits qui me sont conférés par le cinquième amendement.
- Office hours
- Monte-Carlo homework due on Friday

### Monte-Carlo hints

- Don't forget you need to multiply your volume by $2^d$
- Easiest way to calculate the standard deviation
  $$\sigma \approx \sqrt {\frac {p (1 - p)} N}$$
  where $N$ is the sample size and $p$ is an estimation of the probability of being in the hyperball.
- Alternatively, you can use `std` from `Statistics` to calculate the standard deviation
  of $\chi(X_i)$
- Use the `ribbon` option of the `plot` function to plot the confidence interval.

:::::

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
(A + \Delta A) \begin{pmatrix}x_1 \\ x_2\end{pmatrix}
= \begin{pmatrix}0 \\ 0.01\end{pmatrix},
\quad
A = \begin{pmatrix}1 & 0 \\ 0 & 0.01\end{pmatrix},
\quad
\Delta A = \begin{pmatrix}0 & 0\\ 0 & \epsilon\end{pmatrix},
$$
where $0 < \epsilon \ll 0.01$.
:::

# Interlude: discretizing PDES {.split}

\begin{align*}
\frac {\d^2 u} {\d x^2}(x_i)
&\approx \frac 1 h \left(\frac {u(x_{i + 1}) - u(x_{i})} h - \frac {u(x_{i}) - u(x_{i - 1})} h\right)\\
&\approx \frac {u(x_{i + 1}) + u(x_{i - 1}) - 2 u(x_i)} {h^2}
\end{align*}

It follows that in dimension $2$,
$\nabla^2 u(x_i, y_j)$ can be approximated by
\begin{align*}
\frac 1 {h^2} \left(
u(x_{i + 1}, y_j) + u(x_{i - 1}, y_j)
+ u(x_i, y_{j + 1}) + u(x_i, y_{j - 1}) - 4 u(x_i, y_j)
\right)
\end{align*}

Let's attempt to write $(\nabla^2 u)_{ij} = g_{ij}$ as a linear system.

# A first iterative method: Richardson's method [@vaes22, p. 94] {.split}

::: {.algorithm title="Richardson's method"}
\begin{align*}
\vec x^{(k + 1)} = \vec x^{(k)} + \omega (\vec b - \mat A \vec x^{(k)})
\end{align*}
:::

::: proposition
Assume $\omega \neq 0$.
If $(\vec x^{(k)})_k$ converges in the iteration above,
then it converges towards the solution of
\begin{align*}
\mat A \vec x = \vec b.
\end{align*}
:::

::: question
- What value of $\omega$ should we choose?
- What is a good stopping criterion?
:::

# Richardson iteration: example {.split}

::: {.algorithm title="Richardson's method"}
\begin{align*}
\vec x^{(k + 1)} = \vec x^{(k)} + \omega (\vec b - \mat A \vec x^{(k)})
\end{align*}
:::

::: example
Suppose we want to solve the following system.

\begin{align*}
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
\end{align*}
:::

~~~ {.julia .jupyter}
using LinearAlgebra
x = zeros(3)
b = [2, 1, 4]
A = [2 1 0; 0 2 1; 1 0 3]
count = 0
while norm(A * x - b) / norm(b) > 0.01
    x = x + 0.3 * (b - A * x)
    count += 1
end
x, count
~~~

# Richardson iteration: convergence {.split}

::: {.algorithm title="Richardson's method"}
\begin{align*}
\vec x^{(k + 1)} = \vec x^{(k)} + \omega (\vec b - \mat A \vec x^{(k)})
\end{align*}
:::

::: proposition
The Richardson iteration converges to the real solution for every choice of $\vec x^{(0)}$ if and only if
\begin{align*}
\max_{\lambda \in \spectrum A} \abs {1 - \omega \lambda} < 1
\end{align*}
:::

# Link to optimisation [@vaes22, p. 95] {.split}

When $\mat A$ is symmetric and positive definite,
solving $\mat A \vec x = \vec b$ is equivalent to minimizing
\begin{align*}
f(\vec x) = \frac 1 2 \vec x^T \mat A \vec x - \vec b^T \vec x
\end{align*}
as $\nabla f = \mat A \vec x - \vec b$.

The Richardson update can be written
\begin{align*}
\vec x^{(k + 1)} = \vec x^{(k)} - \omega \nabla f(\vec x^{(k)})
\end{align*}

We are moving in the direction where $f$ decreases the most.
We shall encounter this idea again later.

# 3 March 2023

::::: {.col}

## Richardson's method

\begin{align*}
\underbrace{\vec x^{(k + 1)}}_{\to \vec x}
= \underbrace{\vec x^{(k)}}_{\to \vec x}
+ \omega (\underbrace{\vec b - \mat A \vec x^{(k)}}_{\to \vec 0})
\end{align*}

- System is equivalent to minimizing
  $f(\vec x) = \frac 1 2 \vec x^T \mat A \vec x - \vec b^T \vec x$:
\begin{align*}
\vec x^{(k + 1)} = \vec x^{(k)} - \omega \nabla f
\end{align*}
  It follows that the update goes in the direction where the descent is steepest.

- The error satisfies
\begin{align*}
\vec x^{(k)} - \vec x = (\mat I - \omega A)^k (\vec x^{(0)} - \vec x),
\end{align*}
  which means converges when $\rho(\mat I - \omega A) < 1$.

- Speed of convergence is associated with the spectral radius.

- Cost of one iteration: $\bigo(n^2)$ (mostly because of $\mat A \vec x$)

:::::

::::: {.col}

## Condition number

\begin{align*}
\kappa(\mat A) = \norm {\mat A} \norm {\mat A^{-1}}
\end{align*}

Note that if $\mat A = \mat Q^{-1} \mat D \mat Q$ is symmetric and positive definite, then
\begin{align*}
\kappa(\mat A) = \kappa(\mat D) = \frac {\lambda_{\max}} {\lambda_{\min}}.
\end{align*}

## Announcements

- French sentence of the day: *L'exercice est trivial et est laissé au correcteur en exercice de routine*
  (useful for the midterm). Also, *la solution de cet exercice se trouve sur l'ordinateur portable de Hunter Biden* (at least I'll know I've taught you something).

:::::

# Richardson: symmetric positive definite case {.split}

The spectral radius associated with the Richardson iteration is

\begin{align*}
\rho(I - \omega A) = \max_{\lambda \in \spectrum \mat A} \abs{1 - \omega \lambda}
\end{align*}

The smaller $\rho$ is, the faster the convergence.

::: proposition
Let $\mat A$ be a symmetric positive matrix.
The Richardson iteration converges for every choice of $\vec x^{(0)}$
if $0 < \omega < \frac 2 {\lambda_{\max}}$.
Moreover, the spectral radius is minimized if
\begin{align*}
\omega = \frac 2 {\lambda_{\max} + \lambda_{\min}},
\qquad
\rho(\mat I - \omega A) = \frac {\kappa(A) - 1} {\kappa(A) + 1}.
\end{align*}
:::

~~~ {.tex .tikz .fragment scale=1.5}
\draw (-0.5, 0) -- (5.0, 0);
\draw[very thick,green,double=black,double distance=1pt] (1.5, 0) -- (4, 0);
\fill (0, 0) circle (0.05) node[above] {$0$};
\fill (1.5, 0) circle (0.05) node[above] {$\lambda_\min$};
\fill (2.75, 0) circle (0.05) node[above] {$\frac {\lambda_{\min} + \lambda_\max} 2$};
\fill (4, 0) circle (0.05) node[above] {$\lambda_\max$};

\draw (-0.5, -2) -- (5.0, -2);
\draw[very thick,green,double=black,double distance=1pt] (1, -2) -- (2, -2);
\fill (0, -2) circle (0.05) node[below] {$0$};
\fill (1, -2) circle (0.05) node[below] {$\omega \lambda_\min$};
\fill (1.5, -2) circle (0.05) node[above] {$1$};
\fill (2, -2) circle (0.05) node[below] {$\omega \lambda_\max$};

\draw [->, dashed] (4, 0) -- node[right]{$\times \omega$} (2, -2);
\draw [->, dashed] (1.5, 0) -- node[left]{$\times \omega$} (1, -2);
\draw [->, dashed] (2.75, 0) -- node[left]{$\times \omega$} (1.5, -2);
~~~

# Monitoring the convergence [@vaes22, p. 100] {.split}

::: proposition
\begin{align*}
\frac {\norm{\vec x^{(k)} - \vec x}} {\norm {\vec x}}
\leq \kappa(\mat A)
\frac {\norm{\mat A \vec x^{(k)} - \vec {b}}} {\norm {\vec b}}
\end{align*}
:::

# Stopping criterion [@vaes22, p. 101] {.split}

::: question
When should we stop iterating?
:::

#. Stop when $\norm {\mat A \vec x^{(k)} - \vec b} \leq \epsilon$
#. Stop when
\begin{align*}
\frac {\norm {\mat A \vec x^{(k)} - \vec b}} {\norm {\mat A \vec x^{(0)} - \vec b}} \leq \epsilon
\end{align*}
#. Stop when
\begin{align*}
\frac {\norm {\mat A \vec x^{(k)} - \vec b}} {\norm {\vec b}} \leq \epsilon
\end{align*}

# Iterative methods: splitting [@vaes22, p. 92] {.split}

When we're dealing with very large systems $\mat A \vec x = \vec b$,
we may be ready to get an approximate solution
if this means a lower complexity.

To this end, we'll split the matrix
\begin{align*}
\mat A = \mat M - \mat N.
\end{align*}
so that our unknown can appear **twice**.
\begin{align*}
\mat A \vec x = \vec b
\iff \mat M x = \mat N x + \vec b
\end{align*}

This naturally defines an iteration
\begin{align*}
\boxed{\mat M \vec x^{(k + 1)} = \mat N \vec x^{(k)} + \vec b}.
\end{align*}

These iterations will generally be $\bigo(n^2)$ in the worst case,
as $\mat M$ will be chosen to make sure the above system can be solved efficiently.

# Convergence of the splitting method [@vaes22, p. 93] {.split}

::: proposition
Assume that $$\mat A = \mat M - \mat N,$$
where both $\mat A$ and $\mat M$ are invertible square matrices.

The iteration $$\vec x^{(k + 1)} = \mat M^{-1} (\mat N \vec x^{(k)} + \vec b)$$ converges
to the unique solution of $\mat A \vec x = \vec b$ for every choice of $\vec x^{(0)}$
if and only if $\rho(\mat M^{-1} \mat N) < 1$.

Moreover, for each $\epsilon > 0$, there exists $K > 0$ such that
\begin{align*}
\norm {\vec x^{(k)} - \vec x}
\leq \left(\rho(\mat M^{-1} \mat N) + \epsilon\right)^k
\norm {\vec x^{(0)} - \vec x}
\end{align*}
for every $k \geq K$.
:::

# Richardson's method [@vaes22, p. 94] {.split}

::: {.algorithm title="Richardson's method"}
Splitting
:   $$A = \underbrace{\frac 1 \omega \mat I}_{\mat M}
    - \underbrace{\left(\frac 1 \omega \mat I - \mat A\right)}_{\mat N}$$

Iteration
:   $$\vec x^{(k + 1)} = \vec x^{(k)} + \omega ( \vec b - \mat A \vec x^{(k)} )$$

Spectral radius
:   $$\rho(\mat M^{-1} N) = \max_{\lambda \in \spectrum A} \abs {1 - \omega \lambda}$$

Convergence (positive definite)
:   $$0 < \omega < \frac 2 {\lambda_{\max}}$$

Choice of $\omega$ for symmetric and positive definite $\mat A$
:   $$\omega = \frac 2 {\lambda_{\max} + \lambda_{\min}}
    \quad \rho = \frac {\kappa(A) - 1} {\kappa(A) + 1}$$
:::

# Jacobi's method [@vaes22, p. 95] {.split}

First, let's write $\mat A = \mat D - \mat N$,
where $\mat D$ is a diagonal matrix whose entries are that of $\mat A$.

\begin{align*}
\mat D \vec x_{k + 1} = \mat N \vec x_k + \vec b.
\end{align*}

This leads to the equations:
\begin{align*}
x^{(k + 1)}_i = \frac 1 {a_{ii}} \left(-\sum_{\substack{j = 1\\ j \neq i}}^n a_{ij} x^{(k)}_j + b_i\right)
\end{align*}

The components of $\vec x^{(k + 1)}$ can be calculated independently!

# 8 March 2023

::: col

### Splittings

Write $\mat A = \mat M - \mat N$.
\begin{align*}
\mat A \vec x = \vec b
\iff \mat M \vec x = \mat N \vec x + \vec b
\end{align*}

An iteration can be defined via
\begin{align*}
\mat M \vec x^{(k + 1)} = \mat N \vec x^{(k)} + \vec b
\end{align*}
and the error satisfies
\begin{align*}
\vec x^{(k)} - \vec x_\star = (\mat M^{-1} \mat N)^k (\vec x^{(0)} - \vec x_\star).
\end{align*}

::: {.info title="What is a good splitting?"}
- Solving for $\vec x^{(k + 1)}$ is easy
- $\rho(\mat M^{-1} N) < 1$.
:::
:::

::: col

### Jacobi's splitting

\begin{align*}
\mat A = \mat D - (\mat D - \mat A),
\qquad
\mat D = \begin{pmatrix}
a_{11} & 0 & 0 & \dots & 0\\
0 & a_{22} & 0 & \dots & 0\\
\vdots & \vdots & \vdots & \vdots & \vdots\\
0 & 0 & 0 & \dots & a_{nn}
\end{pmatrix}
\end{align*}

### Announcements

- Midterms were marked **out of 40**.
- Grades available on Brightspace.
  Congratulations on your work so far, everyone has A/A-.
- We'll go through question $3$ today.
- Today is **International Women's day**.
:::

# Convergence for diagonally dominant matrices [@vaes22, p. 96] {.split}

::: definition
A matrix $\mat A$ is row or column diagonally dominant if its entries satisfy
\begin{align*}
\abs {a_{ii}} \geq \sum_{\substack{j = 1\\ j \neq i}}^n \abs {a_{ij}}
\qquad \text{or} \qquad
\abs {a_{jj}} \geq \sum_{\substack{i = 1\\ i \neq j}}^n \abs {a_{ij}}
\end{align*}
for $i = 1, \dots, n$.
:::

::: proposition
If $\mat A$ is strictly row or column diagonally dominant,
then the Jacobi iteration converges for all choices of $\vec x^{(0)}$.
:::

# Jacobi's method with Julia

::::: {.col}

~~~ {.julia .jupyter}
using LinearAlgebra
function jacobi(A, b, x, ϵ)
    n = length(x)
    N = [(i == j) ? 0 : -A[i, j] for i in 1:n, j in 1:n]
    while norm(A * x - b) / norm(b) > ϵ
        x_prev = copy(x)
        for i in 1:n
            x[i] = (N[i,:]' * x_prev + b[i]) / A[i, i]
        end
    end
    return x
end

A = [10 -1 2 0; -1 11 -1 3; 2 -1 10 -1; 0 3 -1 8]
b = [6, 25, -11, 15]
x = zeros(4)
jacobi(A, b, x, 0.01)
~~~

:::::

::::: {.col}

The line

~~~ julia
x[i] = (N[i,:]' * x_prev + b[i]) / A[i, i]
~~~

is particularly interesting for two reasons:

- As the calculation for `x[1]`{.julia} and `x[2]`{.julia} don't depend on each other,
  they can be calculated in **parallel**.
- We could not have done `x[i] = (N[i,:]' * x + b[i]) / A[i, i]`{.julia}. Why?

:::::

# Gauss-Seidel [@vaes22, p. 96] {.split}

\begin{align*}
\mat A = \mat L + \mat D + \mat U,
\end{align*}

where

- $\mat L$ is the **lower triangular** part of $\mat A$,
  with the diagonal excluded.
- $\mat D$ is the **diagonal** matrix such that its diagonal entries are exactly that of $\mat A$.
- $\mat U$ is the **upper triangular** part of $\mat A$,
  with the diagonal excluded.


::: {.algorithm title="Gauss-Seidel"}
We consider the split
\begin{align*}
\mat A = \underbrace{\mat L + \mat D}_{\mat M} - \underbrace{(-\mat U)}_{\mat N}
\end{align*}
:::


# Gauss-Seidel iteration [@vaes22, p. 96] {.split}

The iteration takes the following form:
\begin{align*}
(\mat L + \mat D) \vec x^{(k + 1)} = -\mat U \vec x^{(k)} + \vec b,
\end{align*}
which could equivalently be written
\begin{align*}
\left\{
\begin{aligned}
& a_{11} x^{(\textcolor{red}{k+1})}_1 + a_{12} x^{(k)}_2 + a_{13} x^{(k)}_3 + \dotsb + a_{1n} x^{(k)}_n = b_1 \\
& a_{21} x^{(\textcolor{red}{k+1})}_1 + a_{22} x^{(\textcolor{red}{k+1})}_2 + a_{23} x^{(k)}_3 + \dotsb + a_{2n} x^{(k)}_n = b_2 \\
& a_{32} x^{(\textcolor{red}{k+1})}_1 + a_{32} x^{(\textcolor{red}{k+1})}_2 + a_{33} x^{(\textcolor{red}{k+1})}_3 + \dotsb + a_{3n} x^{(k)}_n = b_3 \\
& \vdots \\
& a_{n1} x^{(\textcolor{red}{k+1})}_1 + a_{n2} x^{(\textcolor{red}{k+1})}_2 + a_{n3} x^{(\textcolor{red}{k+1})}_3 + \dotsb + a_{nn} x^{(\textcolor{red}{k+1})}_n = b_n.
\end{aligned}
\right .
\end{align*}

# Gauss-Seidel implementation [@vaes22, p. 96]

::::: {.col}

~~~ {.julia .jupyter}
using LinearAlgebra
function jacobi(A, b, x, ϵ)
    n = length(x)
    N = [(i == j) ? 0 : -A[i, j] for i in 1:n, j in 1:n]
    while norm(A * x - b) / norm(b) > ϵ
        x_prev = copy(x)
        for i in 1:n
            x[i] = (N[i,:]' * x_prev + b[i]) / A[i, i]
        end
    end
    return x
end

A = [10 -1 2 0; -1 11 -1 3; 2 -1 10 -1; 0 3 -1 8]
b = [6, 25, -11, 15]
x = zeros(4)
jacobi(A, b, x, 0.01)
~~~

:::::

::::: {.col}

~~~ {.julia .jupyter}
using LinearAlgebra
function gauss_seidel(A, b, x, ϵ)
    n = length(x)
    N = [(i == j) ? 0 : -A[i, j] for i in 1:n, j in 1:n]
    while norm(A * x - b) / norm(b) > ϵ
        for i in 1:n
            x[i] = (N[i,:]' * x + b[i]) / A[i, i]
        end
    end
    return x
end

A = [10 -1 2 0; -1 11 -1 3; 2 -1 10 -1; 0 3 -1 8]
b = [6, 25, -11, 15]
x = zeros(4)
gauss_seidel(A, b, x, 0.01)
~~~

::: check
- Do you understand the difference between Gauss-Seidel and Jacobi?
- Which one is better for parallelism? Why?
- Which one is easier to implement? Why?
:::

:::::

# Convergence for Gauss-Seidel [@vaes22, p. 96] {.split}

::: {.exampleblock title="Gauss-Seidel iteration"}
\begin{align*}
(\mat L + \mat D) \vec x^{(k + 1)} = -\mat U \vec x^{(k)} + \vec b,
\end{align*}
:::

::: proposition
If $\mat A$ is strictly diagonally dominant or symmetric positive definite,
then the Gauss-Seidel iteration converges.
:::

::: proof
- Imitate the Jacobi case for diagonally dominant matrices
- Adapt [@vaes22, Corollary 4.13 p. 98] when $A$ is symmetric
:::

# Splittings methods {.split}

\begin{align*}
\mat A = \mat L + \mat D + \mat U
\end{align*}

Method                 $\mat M$                           $\mat N$                                      Convergence
-------                ---------                          ---------                                     ------------
Richardson             $\frac 1 \omega \mat I$            $\frac 1 \omega \mat I - \mat A$              Symmetric positive definite
Jacobi                 $\mat D$                           $-\mat L - \mat U$                            Diagonally dominant
Gauss-Seidel           $\mat L + \mat D$                  $-\mat U$                                     Diagonally dominant, symmetric positive definite
Relaxation             $\frac {\mat D} \omega + \mat L$   $\frac {1 - \omega} \omega \mat D - \mat U$   Diagonally dominant, symmetric positive definite

# 20 March 2023

::::: {.col}

### Iterative methods

::: idea
- PDEs lead to very large systems but sparse matrices
- LU, Cholesky, etc. are not suitable because they are $O(n^3)$
- We want a computationaly cheap way to improve an approximate solution
:::

\begin{align*}
\mat A \vec x = \vec b
\iff \mat M \vec x = \mat N \vec x + \vec b,
\qquad \mat A = \mat M - \mat N
\end{align*}

\begin{align*}
&\text{iteration}:\quad
&\boxed{\mat M \vec x^{(k + 1)} = \mat N \vec x^{(k)} + \vec b}\\
&\text{error}:\quad
&\boxed{\vec x^{(k)} - \vec x_\star = (\mat M^{-1} \mat N)^k (\vec x^{(0)} - \vec x_\star)}
\end{align*}

An iteration is good if

- The system $\mat M \vec x = \vec y$ is **easy to solve**
- $(\mat M^{-1} \mat N)^k \xrightarrow {k \to +\infty} 0$,
  which is equivalent to $\rho(\mat M^{-1} \mat N) < 1$.
:::::

::::: {.col}

### Classical splittings

\begin{align*}
\mat A = \mat L + \mat D + \mat U,
\end{align*}

- $\mat L$ is the strictly **lower triangular** part of $A$
- $\mat D$ is the **diagonal** part of $A$
- $\mat U$ is the strictly **upper triangular** part of $A$.

Method                 $\mat M$                             Convergence
-------                ---------                            -------------
Richardson             $\frac 1 \omega \mat I$              Symmetric + positive definite
Jacobi                 $\mat D$                             Strictly diagonally dominant
Gauss-Seidel           $\mat L + \mat D$                    In both the above
Relaxation             $\mat L + \frac {\mat D} \omega$     Generalizes G-S for speed

### Announcements

- Last week on Chapter $4$
- Homework: Exercise 4.25 due **next Monday**
- *French sentence of the day*: L'instructeur fait du bon travail^[Alternatively,
  ChatGPT suggests the following joke: "*Quelle est la différence entre une poubelle et un professeur ?*".
  The punch line is however too inappropriate to be on this slide.]
- Today: Steepest descent method, conjugate gradients

:::::

# Quadratic form associated with a system {.split}

From now on,
$\mat A$ will always be **symmetric** and **positive definite**.

::: {.definition title="Quadratic form associated with a system"}
\begin{align*}
f(\vec x) = \frac 1 2 \vec x^T \mat A \vec x - \vec b^T \vec x.
\end{align*}
:::

::: proposition
The gradient of $f$ is given by
\begin{align*}
\nabla f(\vec x) = \mat A \vec x - \vec b.
\end{align*}

In particular, $f$ has a unique *critical value* $\vec x_\star$,
which is a **minimum**.
:::

# Reading contour plots

::::: {.col}
~~~ {.julia .plot width=100%}
A = [2.0 1.0; 1.0 2.0]
sol = [2.0; 3.0]
b = A * sol
f(x, y) = 1/2 * [x, y]' * A * [x, y] - b' * [x, y]
contour(-4:0.01:8, -1:0.01:7, f, levels=20, color=:turbo, lw=1, fill=true, aspect_ratio=1)
~~~
:::::

::::: {.col .fragment}
- Gradient is **perpendicular** to the contour lines
- Its magnitude is larger when the lines are close together

::: check
- Estimate where the minimum of the function is
- Could you estimate the gradient at every point?
:::
:::::

# Back to Richardson's method {.split}

\begin{align*}
f(\vec x) = \frac 1 2 \vec x^T \mat A \vec x - \vec b^T \vec x.
\end{align*}

::: {.algorithm title="Richardson's method"}
\begin{align*}
\vec x^{(k + 1)}
= \vec x^{(k)} - \omega (\underbrace{\mat A \vec x^{(k)} - \vec b}_{\nabla f(\vec x^{(k)})}),
\end{align*}
:::

~~~ {.julia .plot width=90%}
A = [2.0 1.0; 1.0 2.0]
sol = [2.0; 3.0]
b = A * sol
f(x, y) = 1/2 * [x, y]' * A * [x, y] - b' * [x, y]
contour(-4:0.01:8, -1:0.01:7, f, levels=60, color=:turbo, lw=1, aspect_ratio=1)
x = [5, 4]
r = 0.1*(A*x - b)
scatter!([x[1]], [x[2]], label=L"x^{(k)}")
quiver!([x[1]], [x[2]], quiver=r, label=L"\nabla f(x^{(k)})")
x = x - r
scatter!([x[1]], [x[2]], label=L"x^{(k + 1)}")
scatter!([sol[1]], [sol[2]], label="Solution")
title!("One iteration of Richardson's method")
~~~

# Richardson visualized

::::: {.col}

~~~ {.julia .plot width=75%}
A = [2.0 1.0; 1.0 2.0]
sol = [2.0; 3.0]
b = A * sol
f(x, y) = 1/2 * [x, y]' * A * [x, y] - b' * [x, y]
N = 7
data = zeros(N, 2)
for i in 2:N
  data[i, :] = data[i - 1,:] - 0.65 * (A * data[i - 1,:] - b)
end
contour(-4:0.01:8, -1:0.01:7, f, levels=20, color=:turbo, lw=1, fill=true, aspect_ratio=1)
plot!(data[:, 1], data[:, 2], label="")
scatter!(data[:, 1], data[:, 2], label="Richardson's iteration")
scatter!([2], [3], label="Solution")
title!(L"Richardson's method with $\omega = 0.65$")
~~~
~~~ {.julia .plot width=75%}
A = [2.0 1.0; 1.0 2.0]
sol = [2.0; 3.0]
b = A * sol
f(x, y) = 1/2 * [x, y]' * A * [x, y] - b' * [x, y]
N = 7
data = zeros(N, 2)
for i in 2:N
  data[i, :] = data[i - 1,:] - 0.1 * (A * data[i - 1,:] - b)
end
contour(-4:0.01:8, -1:0.01:7, f, levels=20, color=:turbo, lw=1, fill=true, aspect_ratio=1)
plot!(data[:, 1], data[:, 2], label="")
scatter!(data[:, 1], data[:, 2], label="Richardson's iteration")
scatter!([2], [3], label="Solution")
title!(L"Richardson's method with $\omega = 0.1$")
~~~

:::::

::::: {.col}

::: {.algorithm title="Richardson's iteration"}
\begin{align*}
\vec x^{(k + 1)}
= \vec x^{(k)} - \omega \nabla f (\vec x^{(k)}).
\end{align*}
:::

::: question
- What do you observe?
- How could you improve Richardson's method?
:::

:::::

# Choice of $\omega$ and condition number {.split}

::: {.recall title="Convergence of Richardson's method"}
\begin{align*}
\vec x^{(k)} - \vec x_\star = (\mat I - \omega \mat A)^k (\vec x^{(0)} - \vec x_\star)
\end{align*}

The spectral radius $\rho$ of $\mat I - \omega \mat A$ is minimal when
\begin{align*}
\omega = \frac 2 {\lambda_{\max} + \lambda_{\min}},
\qquad
\rho(\mat I - \omega A) = \frac {\kappa(A) - 1} {\kappa(A) + 1}.
\end{align*}
:::

~~~ {.tex .tikz scale=1.5}
\draw (-0.5, 0) -- (5.0, 0) node[below] {spect(A)};
\draw[very thick,green,double=black,double distance=1pt] (1.5, 0) -- (4, 0);
\fill (0, 0) circle (0.05) node[above] {$0$};
\fill (1.5, 0) circle (0.05) node[above] {$\lambda_\min$};
\fill (2.75, 0) circle (0.05) node[above] {$\frac {\lambda_{\min} + \lambda_\max} 2$};
\fill (4, 0) circle (0.05) node[above] {$\lambda_\max$};

\draw (-0.5, -2) -- (5.0, -2) node[below] {spect(\omega A)};
\draw[very thick,green,double=black,double distance=1pt] (1, -2) -- (2, -2);
\fill (0, -2) circle (0.05) node[below] {$0$};
\fill (1, -2) circle (0.05) node[below] {$\omega \lambda_\min$};
\fill (1.5, -2) circle (0.05) node[above] {$1$};
\fill (2, -2) circle (0.05) node[below] {$\omega \lambda_\max$};

\draw [->, dashed] (4, 0) -- node[right]{$\times \omega$} (2, -2);
\draw [->, dashed] (1.5, 0) -- node[left]{$\times \omega$} (1, -2);
\draw [->, dashed] (2.75, 0) -- node[left]{$\times \omega$} (1.5, -2);
~~~

::: question
How would you calculate $\lambda_{\max}$ and $\lambda_{\min}$ in practice?
:::

# Improvement over Richardson's iteration: steepest descent

::::: {.col}

~~~ {.julia .plot width=100%}
A = [2.0 1.0; 1.0 2.0]
sol = [2.0; 3.0]
b = A * sol
f(x, y) = 1/2 * [x, y]' * A * [x, y] - b' * [x, y]
r(x) = A * x - b
N = 7
data = zeros(N, 2)
for i in 2:N
  x = data[i - 1, :]
  omega = r(x)'r(x) / (r(x)'A*r(x))
  data[i, :] = x - omega * r(x)
end
contour(-4:0.01:8, -1:0.01:7, f, levels=20, color=:turbo, lw=1, fill=true, aspect_ratio=1)
plot!(data[:, 1], data[:, 2], label="")
scatter!(data[:, 1], data[:, 2], label="Steepest descent")
scatter!([2], [3], label="Solution")
~~~

:::::

::::: {.col}
::: idea
What if, every time we chose a direction,
we find the point in this direction which **minimizes** $f$?
:::

Mathematically, we choose $\vec x^{(k + 1)}$ so that
\begin{align*}
f(\vec x^{(k + 1)}) = \min_{\omega \in \R} f(\vec x^{(k)} - \omega \nabla f(\vec x^{(k)}))
\end{align*}

In other words, we choose $\omega$ [@vaes22, p. 102] by solving
\begin{align*}
\boxed{
  \frac {\dd} {\dd \omega} f(\vec x^{(k)} - \omega \nabla f(\vec x^{(k)})) = 0.
}
\end{align*}
:::::

# Exercise (recitation) {.split}

::: exercise
Find $\omega \in \R$ such that
\begin{align*}
\frac {\dd} {\dd \omega} f(\vec x^{(k)} - \omega \nabla f(\vec x^{(k)})) = 0.
\end{align*}

Deduce that if $\vec x^{(k + 1)} = \vec x^{(k)} - \omega \nabla f(\vec x^{(k)})$, then
\begin{align*}
\ip {\nabla f(\vec x^{(k + 1)}), \nabla f(\vec x^{(k)})} = 0.
\end{align*}
:::

# Steepest descent: animation

~~~ {.yaml .widget name="geogebra"}
url: https://www.geogebra.org/m/TYBdQDeB
height: 900
width: 1400
~~~

# Scalar product associated with SPD matrices {.split}

::: {.definition title="Scalar product associated with a matrix"}
Given a symmetric positive definite matrix $\mat M$,
we define
\begin{align*}
\ip{\vec x, \vec y}_{\mat M}
\defeq \vec x^T \mat M \vec y
\end{align*}

We also let $\norm {\vec x}_{\mat M} = \sqrt {\ip{\vec x, \vec x}_{\mat M}}$.
:::

::: proposition
#. $\ip{\placeholder, \placeholder} = \ip{\placeholder, \placeholder}_{\mat I}$
#. $\ip{\vec x, \vec y}_{\mat M} = \ip{\mat M \vec x, \vec y} = \ip{\vec x, \mat M \vec y}$.
#. if $\vec e_1, \dots, \vec e_n$ is an orthonormal basis^[with respect to the usual Euclidean scalar product.] of eigenvectors
   associated with the eigenvalues $\lambda_1, \dots, \lambda_n$, then
\begin{align*}
\begin{cases}
\vec x = \sum_{i = 1}^n x_i \vec e_i\\
\vec y = \sum_{i = 1}^n y_i \vec e_i
\end{cases}
\implies
\ip{\vec x, \vec y}_{\mat M} = \sum_{i = 1}^n \lambda_i x_i y_i.
\end{align*}
:::

# Orthogonal projection {.split}

~~~ {.tex .tikz scale="1.7"}
\draw (-3.5, 0) -- (3.5, 0);
\fill (-2, 0) circle (0.05) node[below] {$\boldsymbol{x}^{(k)}$};
\fill (2, 2) circle (0.05) node[above] {$\boldsymbol{x}_\star$};
\fill (2, 0) circle (0.05) node[below] {$\boldsymbol{x}^{(k + 1)}$};
\node at ( 3.75, 0) {$\boldsymbol d$};
\draw[blue,very thick,->] (-2, 0) -- node[midway,above,sloped] {$\boldsymbol x_\star - \boldsymbol x^{(k)}$} (2, 2);
\draw[red,very thick,->] (-2, 0) -- node[midway,below] {$\frac {\langle\boldsymbol x_\star - \boldsymbol x^{(k)}, \boldsymbol d \rangle_{\boldsymbol A}} {\|\boldsymbol d\|^2_{\boldsymbol A}} \boldsymbol d$} (2, 0);
~~~

::: {.proposition title="Orthogonal projection"}
The vector on $\vec x^{(k)} + \span \{\vec d\}$ closest to $\vec x_\star$
in the sense of the $\norm{\placeholder}_{\mat M}$ norm is
\begin{align*}
\underbrace{
\vec x^{(k + 1)} \defeq
\vec x^{(k)} +
\frac {\ip{\vec x_\star - \vec x^{(k)}, \vec d}_{\mat M}} {\norm {\vec d}^2_{\mat M}}
\vec d.
}_{\text{minimizes}\ \norm{\placeholder - \vec x_\star}_{\mat M} \text{ on } \vec x^{(k)} + \span\{\vec d\}}
\end{align*}
:::

# Choice of $\mat M$ and $\vec d$ {.split}

\begin{align*}
\underbrace{
\vec x^{(k + 1)} \defeq
\vec x^{(k)} +
\frac {\ip{\vec x_\star - \vec x^{(k)}, \vec d}_{\mat M}} {\norm {\vec d}^2_{\mat M}}
\vec d.
}_{\text{minimizes}\ \norm{\placeholder - \vec x_\star}_{\mat M} \text{ on } \vec x^{(k)} + \span\{\vec d\}}
\end{align*}

::: {.info title="Choice of matrix and direction"}
- $\mat A \vec x_\star = \vec b$, so we need not know $\vec x_\star$
\begin{align*}
\vec x^{(k + 1)} \defeq \vec x^{(k)} +
\frac {\ip{\vec b - \mat A \vec x^{(k)}, \vec d}} {\norm {\vec d}^2_{\mat A}}
\vec d.
\end{align*}
- Moreover we have
\begin{align}
\frac 1 2 \left(\norm{\vec x - \vec x_\star}^2_{\mat A} - \norm {\vec x_\star}^2_{\mat A}\right)
= \underbrace{
\frac 1 2 \vec x^T \mat A \vec x - \vec b^T \vec x
}_{\text{Richardson's}\ f(\vec x)}
\end{align}
- Like before, we choose the direction where $f$ locally decreases the most
\begin{align}
\vec d = \nabla f(\vec x^{(k)}) = \mat A \vec x^{(k)} - \vec b
\end{align}
:::

# Steepest descent method: code [@vaes22, p. 104] {.split}

::: {.algorithm title="Steepest descent"}
\begin{align*}
\vec x^{(k + 1)} \defeq
\vec x^{(k)}
- \frac {\norm {\nabla f(\vec x^{(k)})}^2} {\norm {\nabla f(\vec x^{(k)})}^2_{\mat A}}
\nabla f(\vec x^{(k)}),
\quad \nabla f(\vec x) = \mat A \vec x - \vec b.
\end{align*}
:::

~~~ {.julia .jupyter}
function steepest_descent(A, x, b, ϵ)
    ∇f(x) = A * x - b
    while ∇f(x)'∇f(x) ≥ ϵ * b'b
        x -= ∇f(x)'∇f(x) / (∇f(x)'A*∇f(x)) * ∇f(x)
    end
    return x
end

A = [2.0 1.0; 1.0 2.0]
sol = [2.0; 3.0]
b = A * sol
steepest_descent(A, [0, 0], b, 10^-3)
~~~

::: check
What's changed compared to *Richardson's method*?
:::

# Steepest descent: convergence [@vaes22, p. 103] {.split}

::: {.recall title="Convergence of Richardson's method"}
If $\omega = \left(\frac {\lambda_{\max} + \lambda_{\min}} 2\right)^{-1}$, then
\begin{align*}
\norm {\vec x^{(k)} - \vec x_\star}
\leq
C
\left(\frac {\kappa(\mat A) - 1} {\kappa(\mat A) + 1}\right)^k
\norm {\vec x^{(0)} - \vec x_\star}
\end{align*}
:::

::: {.theorem title="Convergence of the steepest descent"}
\begin{align*}
\norm {\vec x^{(k)} - \vec x_\star}_{\mat A}
\leq
\left(\frac {\kappa(\mat A) - 1} {\kappa(\mat A) + 1}\right)^k
\norm {\vec x^{(0)} - \vec x_\star}_{\mat A}
\end{align*}
:::

For the proof, see [@vaes22, p. 104].

::: check
- When is convergence *slow*? When is convergence *fast*?
- How does it compare to *Richardson's method*?
:::

# Steepest descent: exercise [@vaes22, p. 115]

::::: {.col}
![](/static/images/1678653892.png){width=100%}
:::::

::::: {.col}
~~~ {.julia .jupyter}
using Plots
A = [3 1; 1 3]
b = [1, 1]
f(x, y) = 1/2 * [x, y]'*A*[x, y] - b'*[x, y]
# contour(x_range, y_range, function)
contour(-3:0.01:3, -3:0.01:3, f, color=:turbo, fill=true)
~~~
:::::

# Issue with steepest descent

::::: {.col}

~~~ {.julia .plot width=100%}
using LinearAlgebra
A = [2.0 1.0; 1.0 2.0]
sol = [2.0; 3.0]
b = A * sol
f(x, y) = 1/2 * [x, y]' * A * [x, y] - b' * [x, y]
N = 7
data = zeros(N, 2)
data[1, :] = [3, 0]
for i in 2:N
  x = data[i - 1, :]
  omega = norm(A * x - b)^2 / (transpose(A * x - b) * A * (A * x - b))
  data[i, :] = x - omega * (A * x - b)
end
contour(-4:0.01:8, -1:0.01:7, f, levels=20, color=:turbo, lw=1, fill=true, aspect_ratio=1)
plot!(data[:, 1], data[:, 2], label="")
scatter!(data[:, 1], data[:, 2], label="Steepest descent")
scatter!([2], [3], label="Solution")
title!("Steepest descent")
~~~

::: question
- What do you notice about the direction of the different steps?
- Can you see why this is problematic?
:::

:::::

::::: {.col .fragment}

~~~ {.julia .plot width=100%}
A = [2.0 1.0; 1.0 2.0]
sol = [2.0; 3.0]
b = A * sol
f(x, y) = 1/2 * [x, y]'*A*[x, y] - b'*[x, y]
r(x) = A * x - b
N = 3
data = zeros(N, 2)
let x = [3, 0]
    data[1, :] = x
    d = r(x)
    for i in 2:N
        x = x - (d'r(x) / (d'A*d)) * d
        data[i, :] = x
        d = r(x) - (d'A*r(x) / (d'A*d)) * d
    end
end
contour(-4:0.01:8, -1:0.01:7, f, levels=20, color=:turbo, lw=1, fill=true, aspect_ratio=1)
plot!(data[:, 1], data[:, 2], label="")
scatter!(data[:, 1], data[:, 2], label="Conjugate gradients")
scatter!([2], [3], label="Solution")
title!("Conjugate gradients")

~~~

::: check
What's changed? What's the same?
:::

:::::

# Towards the conjugate gradients method

\begin{align*}
\vec x^{(1)}
&\defeq \argmin_{\vec x^{(0)} + \span\{\nabla f(\vec x^{(0)})\}} f
&= \argmin_{\vec x^{(0)} + \span\{\nabla f(\vec x^{(0)})\}} \norm{\placeholder - \vec x_\star}_{\mat A}
\end{align*}

::::: row
::::: {.col}

#### Steepest descent
   
\begin{align*}
\vec x^{(2)} &\defeq \argmin_{\vec x^{(1)} + \span\{\nabla f(\vec x^{(1)})\}} \norm{\placeholder - \vec x_\star}_{\mat A}\\
\quad &\vdots\\
\vec x^{(k + 1)} &\defeq \argmin_{\vec x^{(k)} + \span\{\nabla f(\vec x^{(k)})\}} \norm{\placeholder - \vec x_\star}_{\mat A}
\end{align*}

:::::
::::: {.col}

#### Conjugate gradients

\begin{align*}
\vec x^{(2)} &\defeq \argmin_{\vec x^{(0)} + \span\{\nabla f(\vec x^{(0)}), \nabla f(\vec x^{(1)})\}} \norm{\placeholder - \vec x_\star}_{\mat A}\\
\quad &\vdots\\
\vec x^{(k + 1)} &\defeq \argmin_{\vec x^{(0)} + \span\{\nabla f(\vec x^{(0)}), \dots, \nabla f(\vec x^{(k)})\}} \norm{\placeholder - \vec x_\star}_{\mat A}
\end{align*}

:::::
:::::

# Orthogonal projection {.split}

\begin{align*}
\vec x^{(k + 1)} &\defeq \argmin_{\vec x^{(0)} + \span\{\nabla f(\vec x^{(0)}), \dots, \nabla f(\vec x^{(k)})\}} \norm{\placeholder - \vec x_\star}_{\mat A}
\end{align*}

::: proposition
Let $\vec d_0, \dots, \vec d_k$ be an $\mat A$-orthogonal^[To avoid confusion with the usual scalar product,
we shall also say the vectors are **conjugate**.] basis of 
\begin{align*}
\span\{\nabla f(\vec x^{(0)}), \dots, \nabla f(\vec x^{(k)})\}.
\end{align*}

\begin{align*}
\vec x^{(k + 1)} = \vec x^{(0)} + \sum_{i = 0}^{k}
\frac {\ip{\vec x_\star - \vec x^{(0)}, \vec d_i}_{\mat A}} {\ip{\vec d_i, \vec d_i}_{\mat A}}
\vec d_i.
\end{align*}

In particular, $\vec x^{(n)} = \vec x_\star$ (in exact arithmetic).
:::

::: check
- Can we calculate $\vec x^{(k + 1)}$ without knowing $\vec x_\star$?
- How do you transform that into an iteration?
- How would you define the vectors $\vec d_0, \dots, \vec d_k$?
:::

# Conjugate gradients [@vaes22, p. 108] {.split}

\begin{align*}
\vec x^{(k + 1)} = \vec x^{(0)} + \sum_{i = 0}^{k}
\frac {\ip{\vec x_\star - \vec x^{(0)}, \vec d_i}_{\mat A}} {\ip{\vec d_i, \vec d_i}_{\mat A}}
\vec d_i.
\end{align*}

::: {.algorithm title="Conjugate gradients, first version"}
\begin{align*}
\vec d_k &\defeq \nabla f(\vec x^{(k)}) -
\sum_{i = 0}^{k - 1} \frac {\ip{\nabla f(\vec x^{(k)}), \vec d_i}_{\mat A}} {\ip{\vec d_i, \vec d_i}_{\mat A}}
\vec d_i\\
\vec x^{(k + 1)} &\defeq \vec x^{(k)} +
\frac {\ip{\vec x_\star - \vec x^{(k)}, \vec d_k}_{\mat A}} {\ip {\vec d_k, \vec d_k}_{\mat A}}
\vec d_k
\end{align*}
:::

::: {.remark title="Cost of calculating the conjugate directions"}
Calculating $\vec d_k$ seems to involve increasingly more flops
as $k$ increases.
:::

# Conjugate gradients, version 2 [@vaes22, p. 108] {.split}

\begin{align*}
\vec d_k &\defeq \nabla f(\vec x^{(k)}) -
\sum_{i = 0}^{k - 1} \frac {\ip{\nabla f(\vec x^{(k)}), \vec d_i}_{\mat A}} {\ip{\vec d_i, \vec d_i}_{\mat A}}
\vec d_i
\end{align*}

::: proposition
\begin{align*}
\ip{\nabla f(\vec x^{(k)}), \vec d_i}_{\mat A} = 0,
\qquad i = 0, \dots, k - 2.
\end{align*}
:::

::: {.algorithm title="Conjugate gradients"}
\begin{align*}
\vec d_k &\defeq \nabla f(\vec x^{(k)}) -
\frac {\ip{\nabla f(\vec x^{(k)}), \vec d_{k - 1}}_{\mat A}} {\ip{\vec d_{k - 1}, \vec d_{k - 1}}_{\mat A}}
\vec d_{k - 1}\\
\vec x^{(k + 1)} &\defeq \vec x^{(k)} +
\frac {\ip{\vec x_\star - \vec x^{(k)}, \vec d_k}_{\mat A}} {\ip {\vec d_k, \vec d_k}_{\mat A}}
\vec d_k
\end{align*}
:::

# Conjugate gradients: code [@vaes22, p. 110]

::::: {.col}

\begin{align*}
\vec d_k &\defeq \nabla f(\vec x^{(k)}) -
\frac {\ip{\nabla f(\vec x^{(k)}), \vec d_{k - 1}}_{\mat A}} {\ip{\vec d_{k - 1}, \vec d_{k - 1}}_{\mat A}}
\vec d_{k - 1}\\
\vec x^{(k + 1)} &\defeq \vec x^{(k)} +
\frac {\ip{\vec x_\star - \vec x^{(k)}, \vec d_k}_{\mat A}} {\ip {\vec d_k, \vec d_k}_{\mat A}}
\vec d_k
\end{align*}

~~~ {.julia .jupyter}
function conjugate_gradients(A, x, b, ϵ)
    ∇f(x) = A * x - b
    let d = ∇f(x)
        while ∇f(x)'∇f(x) ≥ ϵ * b'b
            x -= ∇f(x)'d / (d'A*d) * d
            d = ∇f(x) - ∇f(x)'A*d / (d'A*d) * d
        end
    end
    return x
end

A = [2.0 1.0; 1.0 2.0]
sol = [2.0; 3.0]
b = A * sol
conjugate_gradients(A, [0, 0], b, 10^-3)
~~~

:::::

::::: {.col}

::: {.recall title="Steepest Descent (code)"}
~~~ julia
function steepest_descent(A, x, b, ϵ)
    ∇f(x) = A * x - b
    while ∇f(x)'∇f(x) ≥ ϵ * b'b
        x -= ∇f(x)'∇f(x) / (∇f(x)'A*∇f(x)) * ∇f(x)
    end
    return x
end
~~~
:::

::: check
- What's changed in the code compared to the **steepest descent**?
- What's the same?
:::

:::::

# Conjugate gradients: convergence [@vaes22, p. 111] {.split}

::: {.info title="Convergence for the steepest descent"}
\begin{align*}
\norm {\vec x^{(k)} - \vec x_\star}_{\mat A}
\leq
\left(\frac {\kappa(\mat A) - 1} {\kappa(\mat A) + 1}\right)^k
\norm {\vec x^{(0)} - \vec x_\star}_{\mat A}
\end{align*}
:::

::: {.theorem title="Convergence of the conjugate gradients algorithm"}
\begin{align*}
\norm {\vec x^{(k)} - \vec x_\star}_{\mat A}
\leq
2
\left(\frac {\sqrt{\kappa(\mat A)} - 1} {\sqrt{\kappa(\mat A)} + 1}\right)^{k + 1}
\norm {\vec x^{(0)} - \vec x_\star}_{\mat A}
\end{align*}
:::

For the proof, see [@vaes22, pp. 110-112].

::: check
- What's the smallest possible value for $\kappa(A)$?
- Which algorithm converges faster?
:::

# Bibliography
