---
title: "Chapter 6: Numerical computation of eigenvalues"
output: revealjs
split: true
notes: |
  - 05/04: Random browsing, stochastic matrices, PageRank and eigenvalues (1-11)
  - 12/04: Eigenvalues, power iteration and essential convergence (12-22)
  - 14/04: Inverse iteration, Rayleigh quotient, QR decomposition (23-33)
  - 17/04: QR factorisation, Ritz vectors
  - 19/04: End of chapter
...

# Introduction: random browsing

::: {.info name="Assumptions"}
- Each page has the same probability to be the start page.
- There is **at most one** link from one page to any other.
- On each page, each link has the **same probability** of being clicked.
- If there are no links, the next page can be any page with equal probability.
:::

::: text-center
![](https://pi.math.cornell.edu/~mec/Winter2009/RalucaRemus/Lecture3/Images/graf1.PNG){width=80%}
:::

# Ranking webpages

::: {.example name="Notation"}
- The pages will be denoted by $1, \dots, n$
- $X_k$: position after $k$ random clicks
:::

::: {.idea title="PageRank algorithm"}
- For small $k$, $\P(X_k = i)$ depends too much on $X_0$.
- A good way to measure the popularity of page $i$ would be
\begin{align*}
\boxed{
p_i \defeq \lim_{k \to +\infty} \P(X_k = i)
}
\end{align*}
:::

# Rank and PageRank

::: {.definition title="Rank of order k"}
\begin{align*}
\vec p^{(k)} &\defeq \begin{pmatrix}
\P(X_k = 1)\\
\P(X_k = 2)\\
\vdots\\
\P(X_k = n - 1)\\
\P(X_k = n)\\
\end{pmatrix}
\end{align*}
:::

::: {.definition title="PageRank vector"}
If the limit exists,
we call
\begin{align*}
\vec p^\star
\defeq
\lim_{k \to +\infty} \vec p^{(k)}
\end{align*}
the **PageRank** vector associated with the graph.
:::

# Transition matrix

::: {.definition title="Transition Matrix"}
Let $\mat T$ be the matrix defined by
\begin{align*}
T_{ij} &\defeq \P(X_{k + 1} = i \if X_k = j)
\end{align*}
:::

::: text-center
![](https://pi.math.cornell.edu/~mec/Winter2009/RalucaRemus/Lecture3/Images/graf2.PNG){width=80%}
:::

# Properties of the transition matrix

\begin{align*}
T_{ij} &\defeq \P(X_{k + 1} = i \if X_k = j)
\end{align*}

\begin{align*}
\norm {\mat T}_1 \defeq \max_{j = 1, \dots, n} \sum_{i = 1}^n \abs {T_{ij}}
\end{align*}

::: proposition
- $\mat T$ is **left-stochastic**, i.e.
\begin{align*}
\sum_{i = 1}^n T_{ij} = 1.
\end{align*}.
  for every $j \in \{1, \dots, n\}$.
- $1$ is an eigenvalue of $\mat T$.
- $\norm {\mat T}_1 = 1$.
- $\rho(\mat T) = 1$.
:::

# PageRank and eigenvectors

::: proposition
\begin{align*}
\vec p^{(k + 1)} = \mat T \vec p^{(k)}
\end{align*}
:::

\begin{align*}
\underbrace{\P(X_{k + 1} = i)}_{p^{(k + 1)}_i}
= \sum_{j = 1}^n.
\underbrace{\P(X_{k + 1} = i | X_k = j)}_{T_{ij}}
\underbrace{\P(X_k = j)}_{p^{(k)}_j}
\end{align*}

::: corollary
The PageRank vector $\vec r^\star$
satisfies
\begin{align*}
\vec p^\star = \mat T \vec p^\star,
\end{align*}
:::

# Weaknesses of "naive" PageRank

![](https://www.cs.cornell.edu/~rafael/networks-html/images/Figure15-1.png){width=100%}

![](https://www.cs.cornell.edu/~rafael/networks-html/images/Figure15-2.png){width=100%}

# Damping

::: {.info title="Additional assumption"}
- There's a probability $0 < \epsilon < 1$ that
  the anonymous gets "bored" and decides to go to a completely random page.
:::

::: question
What does the matrix $\mat T$ become?
:::

# Improved PageRank

::: theorem
If $\mat T$ is a **positive** left-stochastic matrix,
then there is a unique positive vector $\vec x^\star$ such that
\begin{align*}
\norm {\vec p^\star}_1
\quad \text{and} \quad
\vec p^\star = \mat T \vec p^\star.
\end{align*}
:::

::: corollary
Using a positive damping factor,
the PageRank vector is unique.
:::

# PageRank implementation

~~~ julia
function transition_matrix(A, ϵ)
    # To do yourself
end

function page_rank(A, ϵ, N):
    T = transition_matrix(A, ϵ)
    n = size(A)[1]
    x = ones(n) / n
    for i in 1:N
        x = T * x
    end
    return x
end
~~~

# 12 April 2023

::::: {.col}

### PageRank

Assume $X_k$ is the position of a random browser after $k$ changes of pages.
We are interested in
\begin{align*}
\vec p^{(k)} \defeq
\begin{pmatrix}
\P(X_k = 1)\\
\vdots\\
\P(X_k = n)
\end{pmatrix}
\end{align*}
for large $k \in \N$.

\begin{align*}
\mat T &\defeq
\begin{pmatrix}
\P(X_{k + 1} = 1 \if X_k = 1)
& \dots &
\P(X_{k + 1} = 1 \if X_k = n)\\
\vdots & \vdots & \vdots\\
\P(X_{k + 1} = n \if X_k = 1)
& \dots &
\P(X_{k + 1} = n \if X_k = n)\\
\end{pmatrix}
\end{align*}

\begin{align*}
\boxed{
\vec p^{(k + 1)} = \mat T \vec p^{(k)}.
}
\end{align*}

Being interested in $\vec p^{(k)}$ for large $k \in \N$
means we are interested in the **convergence** of the **iteration** above.

:::::
::::: {.col}

### Abstract problem behind PageRank

::: {.theorem title="PageRank"}
Assume $\vec T$ is **positive**.
The iteration
\begin{align*}
\vec p^{(k + 1)} = \mat T \vec p^{(k)}.
\end{align*}
converges towards the **eigenpair** $(\vec p^\star, 1)$.
The vector $\vec p^\star$ is called the **PageRank** vector.
:::

As $\rho(T) = 1$,
we have shown that in the above case,
an iteration can help us find
the eigenvector associated with the dominant eigenvalue.

::: idea
Write $\mat A \vec x = \lambda \vec x$
as a fixed point iteration.
:::

### Announcements

- Homework grades on Brightspace.
- Homework: **exercise 6.1** on PageRank due **24 April 2023**
- [Data set](https://snap.stanford.edu/data/enwiki-2013.html)

:::::

# Motivations and assumptions

::: question
How to calculate the eigenvalues of a matrix?
:::

::: {.info title="Assumptions"}
- $\mat A$ is **diagonalizable**
- $\lambda_1 \geq \dots \geq \lambda_n$ are its eigenvalues (in **decreasing** order).
- $\vec v_1, \dots, \vec v_n$ are the normalized **eigenvectors** associated with $\lambda_1, \dots, \lambda_n$.
:::

# Naive method

::: algorithm
#. Calculate the coefficients of
\begin{align*}
p_{\mat A}(\lambda) \defeq \det(\mat A - \lambda \mat I)
\end{align*}

#. Finding the roots of $p_{\mat A}$.
:::

::: remark
Calculating $\det(\mat A)$ is $\bigo(n!)$.
:::

~~~ {.julia .jupyter}
import LinearAlgebra
A = rand(2000, 2000)
LinearAlgebra.eigen(A)
~~~

# Iterations

- The PageRank algorithm shows that an **iterative algorithm** might be a successful approach.
- Remember that iterations will converge to **fixed points**.

Assume $\lambda > 0$.

\begin{align*}
\mat A \vec x = \lambda \vec x
\iff
\vec x = \frac 1 \lambda \mat A \vec x.
\end{align*}

A simple fixed point iteration would be
\begin{align*}
\vec x_{n + 1} = \frac 1 \lambda \mat A \vec x_n,
\end{align*}
but it requires us to know $\lambda$.
Ensuring that each $x_k$ has norm $1$,
$\lambda \approx \norm {\mat A \vec x_k}$
we get the following iteration:

::: {.algorithm title="Power iteration"}
\begin{align*}
\vec x_{n + 1} \defeq \frac {\mat A \vec x_n} {\norm {\mat A \vec x_n}}.
\end{align*}
:::

# Remark on the Banach fixed point theorem

So far, all our iterations (Jacobi, Gauss-Seidel, relaxation, Newton-Raphson, etc.)
relied on the **Banach fixed point theorem**.

::: question
Can we apply it to
\begin{align*}
\vec F(\vec x) = \frac 1 \lambda \mat A \vec x?
\end{align*}
:::

Unfortunately,
\begin{align*}
\norm {\vec J_{\vec F}(\vec x_\star)} = \frac 1 {\abs \lambda} \norm {\vec A} \geq 1.
\end{align*}
If $A$ is **diagonalizable**,
then it is exactly one,
so the theorem **does not apply**.
In fact, the iteration
\begin{align*}
\vec x_{n + 1} \defeq \frac {\mat A \vec x_n} {\norm {\mat A \vec x_n}}.
\end{align*}
does not even always converge
when we start with the solution:
\begin{align*}
\mat A \defeq
\begin{pmatrix}
-1 & 0\\
0 & -1.
\end{pmatrix},
\quad
\vec x_0 = \begin{pmatrix}1 \\ 0\end{pmatrix}
\end{align*}

# Power iteration [@vaes22, p. 145]

\begin{align*}
\vec x_0 = \alpha_1 \vec v_1 + \dots + \alpha_n \vec v_n.
\end{align*}

::: proposition
Let $\vec x_0 \in \R^n$.
\begin{align*}
\mat A^k \vec x_0
= \lambda_1^k \alpha_1 \vec v_1 + \dots + \lambda_n^k \alpha_n \vec v_n.
\end{align*}
:::

::: remark
Iterating amplifies the coefficient associated with the dominant eigenvalue.
\begin{align*}
\mat A^k \vec x_0
= \lambda_1^k \left(
\alpha_1 \vec v_1
+ \alpha_2 \left(\frac {\lambda_2} {\lambda_1}\right)^k \vec v_2
+ \dots
+ \alpha_n \left(\frac {\lambda_n} {\lambda_1}\right)^k \vec v_n
\right).
\end{align*}
:::

# Power iteration: Julia code

::: {.algorithm title="Power iteration"}
\begin{align*}
\vec x_{k + 1} &\defeq \frac {\mat A \vec x_k} {\norm {\mat A \vec x_k}}\\
\lambda &\approx \ip {\vec x_k, \mat A \vec x_k}
\end{align*}
:::

~~~ {.julia .jupyter}
function power_iteration(A, x, n)
    for i in 1:n
        x = A * x
        x = x / √(x'x)
    end
    return x, x'A*x
end
~~~

# Angle between two vectors

\begin{align*}
\ip {\vec x, \vec y}
= \norm x \norm y \cos \theta.
\end{align*}

::: {.definition title="Angle between two vectors"}
We define the **acute** angle between two vectors via
\begin{align*}
\angle (\vec x, \vec y)
\defeq \arccos\left(
\frac {\abs {\ip{\vec x, \vec y}}} {\norm {\vec x} \norm {\vec y}}
\right)
\end{align*}
:::

::: proposition
- $\angle (\vec x, \vec y) \geq 0$
- $\angle (\vec x, \vec y) = \angle (\vec y, \vec x)$
- $\angle (\vec x, \vec y) = 0 \iff \vec x = \lambda \vec y$
- $\angle (\vec x, \vec y) = \frac \pi 2 \iff \ip{x, y} = 0$
- $\angle (\alpha \vec x, \beta \vec y) = \angle (\vec x, \vec y)$ when $\alpha, \beta \neq 0$.
:::

# Convergence of the power iteration [@vaes22, p. 145]

::: {.proposition title="Essential convergence of the power iteration"}
Suppose that $\mat A$ is diagonalizable^[
In fact, we can just assume that $A$ has a dominant eigenvalue,
and prove the result using the Jordan decomposition.
] and that $\abs {\lambda_1} > \abs{\lambda_2}$.
If
\begin{align*}
\vec x_0 = \underbrace{\alpha_1}_{\neq 0} \vec v_1 + \dots + \alpha_n \vec v_n,
\end{align*}
then the sequence $(\vec x_k)_{k \in \N}$ generated by the power iteration satisfies
\begin{align*}
\lim_{k \to +\infty} \angle (\vec x_k, \vec v_1) = 0.
\end{align*}
:::

::: {.definition title="Essential convergence"}
We shall say that $(\vec x_k)_{k \in \N}$ converges **essentially** to $\vec v_1$ if
\begin{align*}
\lim_{k \to +\infty} \angle (\vec x_k, \vec v_1) = 0.
\end{align*}
:::

# Example of the power iteration

::: example
\begin{align*}
\mat A \defeq \begin{pmatrix} 1 & 0\\ 0 & -2 \end{pmatrix}
\end{align*}
:::

# Essential convergence: exercise

::: exercise
Let $(\vec x_k)_k \subset R^n$.
The following conditions are equivalent:

- $\angle (\vec x_k, \vec x_\star)$ converges to $0$;
- There exists a sequence $(r_k)_k \subset \R$ such that $r_k \vec x_k$ converges to $\vec x_\star$.
- The projector $\mat P_{\vec x_k}$ converges to $\mat P_{\vec x_\star}$.
:::

::: info
\begin{align*}
\mat P_{\vec v}(\vec x) = \frac {\ip{x, v}} {\norm {\vec v}^2} \vec v
= \underbrace{\frac 1 {\norm{\vec v}^2} \vec v \vec v^T}_{\mat P_{\vec v}} \vec x
\end{align*}
:::

# 14 April 2023

::::: {.col}

### Power Iteration

\begin{align*}
\vec x_{k + 1}
= \underbrace{\frac {\mat A \vec x_k} {\norm {\mat A \vec x_k}}}_{\vec F(\vec x_k)}
= \frac {\mat A^{k + 1} \vec x_0} {\norm {\mat A^{k + 1} \vec x_0}}
\end{align*}

- $\vec F$ is **not** a contraction
- The best we can hope for is **essential convergence**.
- Applying $\mat A$ amplifies the dominant eigenvector.

~~~ julia
function power_iteration(A, x, n)
    for i in 1:n
        x = A * x
        x = x / √(x'x)
    end
    return x, x'A*x
end
~~~

:::::

::::: {.col}

### PageRank

Find the dominant eigenvector of

\begin{align*}
\mat T &\defeq
\begin{pmatrix}
\P(X_{k + 1} = 1 \if X_k = 1)
& \dots &
\P(X_{k + 1} = 1 \if X_k = n)\\
\vdots & \vdots & \vdots\\
\P(X_{k + 1} = n \if X_k = 1)
& \dots &
\P(X_{k + 1} = n \if X_k = n)\\
\end{pmatrix}
\end{align*}

via the **power iteration**.

### Today

::: question
How can we find other eigenpairs?
:::

### Announcements

- Homework: **exercise 6.1** on PageRank due **24 April 2023**
- [PageRank Data set](https://snap.stanford.edu/data/enwiki-2013.html)^[The link
  doesn't work in the lecture notes.]
- French word of the day: nycthémère (a 24 hour period)

:::::

# Inverse iteration [@vaes22, p. 147]

::: proposition
Let $\mu \notin \spectrum \mat A$.
The following claims are equivalent:

- $(\vec x, \lambda)$ is an eigenpair of $\mat A$.
- $(\vec x, \frac 1 {\lambda - \mu})$ is an eigenpair of $\mat B(\mu) \defeq (\mat A - \mu \mat I)^{-1}$
:::

::: remark
If $\mu \approx \lambda$, the power iteration applied to $\mat B(\mu)$
will yield the $\mat A$-eigenvector associated with $(\lambda)$.
:::

# Finding an arbitrary eigenpair [@vaes22, p. 147]

Assume we are interested in finding

\begin{align*}
\mat A \vec x_\star = \lambda \vec x_\star.
\end{align*}

::: {.algorithm title="Inverse iteration"}
#. Choose $\mu$ close but not equal to $\lambda$.
#. Apply the power iteration to $(\mat A - \mu \mat I)^{-1}$.
:::

::: remark
The iteration
\begin{align*}
\vec x_{n + 1} \defeq (\mat A - \mu \vec I)^{-1} \vec x_n
\end{align*}
is equivalent to solving
\begin{align*}
(\mat A - \mu \vec I) \vec x_{n + 1} = \vec x_n
\end{align*}
for $\vec x_{n + 1}$.
:::

# Implementation of inverse iteration [@vaes22, p. 147]

::: info
Solving the system $\mat A \vec x = \vec b$
can be done efficiently via `x = A \ b`{.julia}
instead of `x = A^(-1) * b`{.julia}.
:::

::: idea
Apply the power iteration to $(\mat A - \mu \mat I)^{-1}$
:::

~~~ {.julia .jupyter}
using LinearAlgebra

function inverse_iteration(A, x, μ, n)
    for i in 1:n
        x = (A - μ * I) \ x
        x = x / √(x'x)
    end
    return x, x'A*x
end
~~~

# Exercise 6.7 [@vaes22, p. 161]

::: exercise
Consider the matrix
\begin{align*}
\mat M \defeq
\begin{pmatrix}
    0 & 1 & 2 & 0 \\
    1 & 0 & 1 & 0 \\
    2 & 1 & 0 & 2 \\
    0 & 0 & 2 & 0
\end{pmatrix}
\end{align*}

- Find the dominant eigenvalue of $\mat M$ by using the power iteration.
- Find the eigenvalue of $\mat M$ closest to 1 by using the inverse iteration.
- Find the other two eigenvalues of $\mat M$ by using a method of your choice.
:::

# Railey quotient iteration [@vaes22, p. 148]

Remember that the convergence speed is determined
by the ratio of the two most dominant eigevalue.

In particular, the closer $\mu$ is to $\lambda$,
the faster the inverse iteration converges.

::: idea
To increase the convergence speed,
we update $\mu$ by our approximation of the eigenvalue.
:::

~~~ {.julia .jupyter}
using LinearAlgebra

function inverse_iteration(A, x, μ, n)
    for i in 1:n
        x = (A - μ * I) \ x
        x = x / √(x'x)
        # Update the value of μ
        μ = x'A*x
    end
    return x, x'A*x
end
~~~

# Railey quotient iteration: implementation [@vaes22, p. 148]

::::: {.col}
~~~ {.julia .jupyter}
using LinearAlgebra

function inverse_iteration(A, x, μ, n)
    for i in 1:n
        x = (A - μ * I) \ x
        x = x / √(x'x)
    end
    return x, x'A*x
end
~~~
:::::

::::: {.col}
~~~ {.julia .jupyter}
using LinearAlgebra

function railey_quotient(A, x, n)
    μ(x) = x'A*x / x'x
    for i in 1:n
        x = (A - μ(x) * I) \ x
        x = x / √(x'x)
    end
    return x, μ(x)
end
~~~
:::::

# Towards subspace iterations

::: proposition
Assume $\mat A$ is symmetric.
If $\vec v_1$ and $\vec v_2$ are two eigenvalues associated with two different eigenvalues $\lambda_1$, $\lambda_2$,
then
\begin{align*}
\ip {\vec v_1, \vec v_2} = 0.
\end{align*}
:::

::: proposition
Assume that $x_0$ is orthogonal to the first eigenvector.
The power iteration
\begin{align*}
\vec x_k \xrightarrow{k \to +\infty} \vec v_2.
\end{align*}
:::

# Subspace iteration [@vaes22, p. 148]

::::: {.col}

### Power iteration

\begin{align*}
\vec y_k \defeq \vec A \vec x_k
\end{align*}

\begin{align*}
\vec x_{k + 1} \defeq \frac {\vec x_k} {\norm {\vec x_k}}
\end{align*}
:::::

::::: {.col}

### Subspace iteration

\begin{align*}
\mat Y_k \defeq \vec A \mat X_k
\end{align*}

\begin{align*}
\mat X_{k + 1} \defeq \text{orthonormalize the columns of} \ \mat Y_k
\end{align*}
:::::

# Reduced QR decomposition [@vaes22, p. 149]

::: {.proposition title="QR factorization"}
A matrix $\mat Y \in \R^{n \times p}$ can be written as a product
\begin{align*}
\mat Y = \mat Q \mat R,
\qquad
\end{align*}
where $\mat Q \in \R^{n \times p}$ has **orthonormal columns**
and $\mat R \in \R^{p \times p}$ is **upper-triangular**.
Moreover, if we require that the diagonal elements of $\mat R$ be positive,
this decomposition is unique.
:::

::: remark
If we denote by $\vec y_j$ and $\vec q_j$ the $j$-th columns of $\mat Y$ and $\mat Q$,
we have
\begin{align*}
\begin{rcases}
\vec y_1 &= r_{11} \vec q_1,\\
\vec y_2 &= r_{12} \vec q_1 + r_{22} \vec q_2\\
&\vdots
\end{rcases} \implies
\vec y_j = \sum_{i = 1}^i r_{ij} \vec q_i
\end{align*}

In particular,
\begin{align*}
\ip {\vec q_i, \vec y_j} = r_{ij}.
\end{align*}
:::

# QR decomposition: example

::: example
Find the $\mat Q \mat R$ decomposition of
\begin{align*}
\mat Y \defeq
\begin{pmatrix}
3 & 1\\
6 & 2\\
0 & 2
\end{pmatrix}.
\end{align*}
:::

::: {.idea title="QR factorization"}
- We use **Gram-Schmidt** for $\mat Q$.
- The entries of $\mat R$ are given by:
\begin{align*}
r_{ij} \defeq \ip {\vec q_i, \vec y_j}
\end{align*}
:::

# 17 April 2023

::::: {.col}

### Power iteration

\begin{align*}
\vec x_{k + 1} = \frac {\mat A \vec x_k} {\norm {\mat A \vec x_k}}
\qquad
\text{convergence:}\,
\bigo\left(\abs{\frac {\lambda_2}{\lambda_1}}^k\right)
\end{align*}

~~~ julia
for i in 1:n
    x = A * x
    x = x / √(x'x)
end
~~~

We now assume $\mat A$ to be **symmetric**.

With two vectors $\mat X_0 = \begin{bmatrix}\vec x^{(1)}_0 & \vec x^{(2)}_0\end{bmatrix}$,
it makes sense to consider

\begin{align*}
\mat X_{n + 1} \defeq
\text{orthnormalize}\, \mat A \vec X_n.
\end{align*}

The orthogonalisation can be justified as such:

::: proposition
The power iteration converges to $\vec v_1$
if and only if $\ip {\vec x_0, \vec v_1} = 0$.
:::

:::::

::::: {.col}

### QR decomposition

\begin{align*}
\underbrace{\mat Y}_{\R^{n \times p}} \defeq
\underbrace{\begin{bmatrix}
\vec q_1 & \vec q_2 & \dots & \vec q_p
\end{bmatrix}}_{\mat Q \in \R^{n \times p} \, \text{(orthonormal)}}
\underbrace{\begin{pmatrix}
r_{11} & r_{12} & r_{13} & \dots\\
0 & r_{22} & r_{23} & \dots\\
0 & 0 & r_{33} & \dots\\
\vdots & \vdots & \vdots & \dots
\end{pmatrix}}_{\mat R \in \R^{p \times p} \, \text{upper}-\Delta}
\end{align*}

~~~ julia
using LinearAlgebra
Q, R = qr(A)
~~~

### Announcements

- French word of the day: pédoncule (stalk bearing a flower), pédonculé

:::::

# Why orthonormalize?

My explanation was quite bad last time, so let's try again.

::: proposition
The power iteration converges to $\vec v_1$
if and only if $\ip {\vec x_0, \vec v_1} = 0$.
:::

::: info
- We normalize to avoid round-off errors;
- Orthogonolising
:::

# Full vs Reduced $\mat Q \mat R$ Factorization

We have in fact seen the **reduced** $\mat Q \mat R$ factorization,
with $p < n$.

\begin{align*}
\underbrace{\mat Y}_{\R^{n \times p}} \defeq
\underbrace{\begin{bmatrix}
\vec q_1 & \vec q_2 & \dots & \vec q_p
\end{bmatrix}}_{\mat Q \in \R^{n \times p} \, \text{(orthonormal)}}
\underbrace{\begin{pmatrix}
r_{11} & r_{12} & r_{13} & \dots\\
0 & r_{22} & r_{23} & \dots\\
0 & 0 & r_{33} & \dots\\
\vdots & \vdots & \vdots & \dots
\end{pmatrix}}_{\mat R \in \R^{p \times p} \, \text{upper}-\Delta}
\end{align*}

We could carry on the Gram-Schmidt iteration
to obtain the **full** factorization.

\begin{align*}
\underbrace{\mat Y}_{\R^{n \times p}} \defeq
\underbrace{\begin{bmatrix}
\vec q_1 & \vec q_2 & \dots & \vec q_p & \dots & \vec q_n
\end{bmatrix}}_{\mat Q' \in \R^{n \times n} \, \text{(orthonormal)}}
\underbrace{\begin{pmatrix}
r_{11} & r_{12} & r_{13} & \dots\\
0 & r_{22} & r_{23} & \dots\\
0 & 0 & r_{33} & \dots\\
\vdots & \vdots & \vdots & \dots\\
0 & 0 & 0 & \dots\\
\vdots & \vdots & \vdots & \dots\\
0 & 0 & 0 & \dots
\end{pmatrix}}_{\mat R' \in \R^{n \times p} \, \text{upper}-\Delta}
\end{align*}

Full factorisation: $\mat Q'^T \mat Q' = \mat Q' \mat Q'^T = \mat I$.

# $\mat Q \mat R$ to solve equations

The $\mat Q' \mat R'$ decomposition can be used instead of the $\mat L \mat U$ decomposition
to solve systems.
\begin{align*}
\mat Q' \mat R' \vec x = \vec b
\iff \boxed {\mat R' \vec x = \mat Q'^T \vec b}.
\end{align*}

::: info
- $\mat Q' \mat R'$ requires more flops than $\mat L \mat U$.
- More **numerically stable** for *overdetermined* system
:::

# $\mat Q \mat R$ for *overdetermined* systems

As $\mat Q$ is a orthogonal, it doesn't affect $\norm {\placeholder}_2$.
Consequently, we have.

\begin{align*}
\norm {\mat A \vec x - \vec b}^2
= \norm {\mat R' \vec x - \mat Q'^T \vec b}^2
\end{align*}

Writing $\mat Q'^T \vec b = \begin{pmatrix}\vec c_1 \\ \vec c_2\end{pmatrix}$,
we get

\begin{align*}
\norm {\mat A \vec x - \vec b}^2
= \norm {\mat R \vec x - \vec c_1}^2 + \norm {\vec c_2}^2_2,
\end{align*}
which means that the approximation is given by the solution of
\begin{align*}
\mat R \vec x = \vec c_1.
\end{align*}

Compare the conditioning with the *normal equations*:
\begin{align*}
\mat A^T \mat A \vec x = \mat A^T \vec b
\end{align*}

# Simultaneous iteration: algorithm [@vaes22, p. 150]

Let's go back to eigenvalues.

\begin{align*}
\mat Y_k &\defeq \vec A \mat X_k\\
\mat X_{k + 1} &\defeq \text{orthonormalize the columns of} \ \mat Y_k
\end{align*}

In other words,

\begin{align*}
\vec A \mat X_k &= \mat Q_k \mat R_k
\qquad (\mat Q \mat R \,\text{factorization})\\
\mat X_{k + 1} &\defeq \mat Q_k.
\end{align*}

::: remark
We don't even use the matrix $\mat R$.
Could I not have told you to just use **Gram-Schmidt**?
Why do I have to make everything so complicated?
:::

# Simultaneous iteration: Julia implementation

~~~ {.julia .jupyter}
using LinearAlgebra
function subspace_iteration(A, X, n)
    for i in 1:n
        Q, R = qr(A * X)
        X = Q[:, 1 : size(A)[2]]
    end
    return X
end
~~~

# The $\mat Q \mat R$ algorithm [@vaes22, p. 152]

::: {.idea title="QR algorithm"}
To find **all eigenpairs**,
we could apply the subspace iteration with $\mat X_0 \defeq \mat I$.
:::

Assume $\mat X_0, \mat Q_0 \defeq \mat I$.
\begin{align*}
\mat A \mat Q_0
&= \mat Q_1 \mat R_1
\quad &\implies \quad
\mat X_1 \defeq \mat Q_0 \mat Q_1\\
\mat A \mat Q_0 \mat Q_1
&= \mat Q_1 \mat R_1 \mat Q_1
= \mat Q_1 \mat Q_2 \mat R_2
\quad &\implies \quad
\mat X_2 \defeq \mat Q_0 \mat Q_1 \mat Q_2\\
\mat A \mat Q_0 \mat Q_1 \mat Q_2
&= \mat Q_1 \mat Q_2 \mat R_2 \mat Q_2
= \mat Q_1 \mat Q_2 \mat Q_3 \mat R_3
\quad &\implies \quad
\mat X_3 \defeq \mat Q_0 \mat Q_1 \mat Q_2 \mat Q_3
\end{align*}

# The $\mat Q \mat R$ algorithm: iteration [@vaes22, p. 152]

The iteration
\begin{align*}
\begin{cases}
\mat A = \mat Q_1 \mat R_1\\
\mat R_k \mat Q_k = \mat Q_{k + 1} \mat R_{k + 1}
\end{cases}
\end{align*}
defines a family of matrices $\mat Q_k$, $\mat R_k$.

From there,
we can
\begin{align*}
\begin{cases}
\mat X_0 &\defeq \mat I\\
\mat X_k &\defeq \mat Q_1 \dots \mat Q_k
\end{cases}
\end{align*}

# The $\mat Q \mat R$ algorithm: Julia implementation

~~~ {.julia .jupyter}
using LinearAlgebra
function qr_algorithm(A, n)
    X, Q, R = I, I, A
    for i in 1:n
        Q, R = qr(R * Q)
        X *= Q
    end
    return X, R * Q
end

D = diagm([4, 3, 2, 1])
S = rand(4, 4)
A = S * D * S^-1
X, D = qr_algorithm(A, 50)
D
~~~

# Ritz vectors

::: idea
Let $\mathcal U \subset \R^n$.
We'll try to find an **approximate** eigenvector $\vec v \in \mathcal U$,
\begin{align*}
\mat A \vec v \approx \lambda \vec v
\end{align*}

We call $\vec v$ a **Ritz vector** of $\mat A$ relative to $\mat U$.
:::

::: definition
The vector $\vec v$ is a **Ritz vector** of $\mat A$ relative to $\mathcal U$
associated with $\lambda$
if
\begin{align*}
\proj_{\mathcal U} (\mat A \vec v) = \lambda \vec v,
\qquad \vec v \in \mathcal U.
\end{align*}
:::

::: proposition
If $\mat A \mathcal U \subset \mathcal U$, then
Ritz vectors are eigenvectors.
:::

# 19 April 2023

::::: {.col}

### Simultaneous iteration

- **Step 1**: Left-multiply by $\mat A$

- **Step 2**: Apply Gram-Schmidt

~~~ julia
for i in 1:n
    X, _ = qr(A * X)
end
~~~

### $\mat Q \mat R$ algorithm

- Simultaneous iteration with $\mat X_0 \defeq \mat I$.
- Apply $\mat Q \mat R$ only on the last two terms

~~~ julia
Q, R = I, A
for i in 1:n
    O, R = qr(R* Q)
    X *= Q
end
~~~

:::::

::::: {.col}

### Ritz vectors

Given $\mathcal U \subset \R^n$,
a **Ritz vector** is an eigenvector of the restriction of $A$ on $\mathcal U$,

\begin{align*}
\proj_{\mathcal{U}} \mat A \vec x = \lambda \vec x.
\end{align*}


### Announcements

- PageRank homework due on Monday
- You have to implement the **damped** version
- You may use the Arnoldi instead of the power iteration (extra credits, faster)

:::::

# Projection

Let $\vec u_1, \dots, \vec u_p$ be an orthonormal basis of $\mathcal U$.

\begin{align*}
\mat U : \R^p \to \mathcal U,
\qquad
\mat U
\defeq
\begin{pmatrix}
\vec u_1 & \dots & \vec u_n
\end{pmatrix}
\end{align*}

::: proposition
- $\mat U^t$ is the left-inverse of $\mat U$.
- The projection onto $\mat U$ is given by the matrix $\mat U \mat U^t$
:::

# Characterisation of Ritz vectors

Let $\vec u_1, \dots, \vec u_p$ be an orthonormal basis of $\mathcal U$.

\begin{align*}
\mat U : \R^p \to \mathcal U,
\qquad
\mat U
\defeq
\begin{pmatrix}
\vec u_1 & \dots & \vec u_n
\end{pmatrix}
\end{align*}

::: proposition
- $\mat U \mat U^t = \proj_{\mathcal U}$
- $\mat U^t \mat U = \mat I$
:::

::: proposition
The following conditions are equivalent:

- $\mathcal v \in \mathcal U$ is a Ritz vector relative to $\mathcal U$.
- $\mathcal x \defeq \mat U^t \vec v$ is an eigenvector of $\mat U^t \mat A \mat U$.
:::

::: remark
In practice, $p \ll n$ so $\mat U^t \mat A \mat U$ is a small symmetric matrix.
:::

# Estimation of the Ritz values

We'll use $\widehat \lambda$ for Ritz values.

::: theorem
Let $\mat A$ be a full rank symmetric matrix
and $\mat U \subset R^n$ a $p$-dimensional subspace.

There is a subset $\lambda_1, \dots, \lambda_p \in \spectrum \mat A$ which satisfies
\begin{align*}
\max_{j \in \{1, \dots, p\}} \abs{\lambda_j - \widehat{\lambda}_j}
\leq \norm{ (\mat I - \mat P_{\mathcal U} ) \mat A \mat P_{\mathcal U} }_2
\end{align*}
:::

# Lanczos/Arnoldi iteration [@vaes22, p. 158]

::: {.info title="Lo que hemos visto hasta ahora"}
- Ritz vectors are eigenvectors approximations
- Ritz vectors are eigenvectors when $\mathcal U$ is invariant under $\mat A$.
- Ritz vectors of $\mat A$ are eigenvectors of $\mat U^T \mat A \mat U$,
:::

::: algorithm
Step 1
:   We choose

\begin{align*}
\mathcal U \defeq \span\{\vec x_0, \mat A \vec x_0, \dots, \mat A^k \vec x_0\}
\end{align*}

Step 2
:   Find an orthonormal basis of $\mathcal U$.

Step 3
:   Calculate $\mat U^T \mat A \mat U$.

Step 4
:   Find the eigenvectors of $\mat H \defeq \mat U^T \mat A \mat U$.

Step 5
:   Start over with $\vec x_0$ being the largest Ritz vector
:::

# Krylov space

We introduce our choice of $\mathcal U$ given an initial guess $\vec x_0$.

::: {.definition title="Krylov spaces"}
\begin{align*}
\mathcal K_{k + 1}(\mat A, \vec x_0)
\defeq
\span \{ \vec x_0, \mat A \vec x_0, \dots, \mat A^k \vec x_0 \}
\end{align*}
:::

::: info
**Krylov spaces** are useful because they are "almost" invariant under $\mat A$.
Keep in mind that an invariant subspace yields **exact eigenvectors**.
:::

# Step 2: Gram-Schmidt

Create an orthonormal basis of
\begin{align*}
\mathcal U \defeq \span\{\vec x_0, \mat A \vec x_0, \dots, \mat A^{p - 1} \vec x_0\}
\end{align*}

~~~ julia
U = u / √(u'u)
for j in 1:p - 1
    u = A * u

    # Gram-Schmidt
    for i in 1:j
        u -= u'U[:,i] * U[:,i]
    end
    u /= √(u'u)

    # Add it to the matrix U
    U = [U u]
end
~~~

# Hessenberg property

::: proposition
The matrix $\mat H = \mat U^T \mat A \mat U$,
satisfies
\begin{align*}
\mat H_{ij} \defeq 0
\qquad \text{if } i > j + 1.
\end{align*}
:::

\begin{align*}
H_{ij} = \ip{ \vec u_i, A \vec u_j }
\end{align*}

# Step 3: Calculate $\mat H = \mat U^T \mat A \mat U$ {.nosplit}

Note that
\begin{align*}
H_{ij} = \ip{ \vec u_i, A \vec u_j }
\end{align*}

::: row
::::: {.col}

### Gram-Schmidt

~~~ julia
U = u / √(u'u)
for j in 1:p - 1
    u = A * u

    # Gram-Schmidt
    for i in 1:j
        u -= u'U[:,i] * U[:,i]
    end
    u /= √(u'u)

    # Add it to the matrix U
    U = [U u]
end
~~~
:::::

::::: {.col}

### Gram-Schmidt with $\mat H$ calculation (Arnoldi)

~~~ julia
U = u / √(u'u)
H = zeros(p)
for j in 1:p
    u = A * u

    # Gram-Schmidt
    for i in 1:j
        H[i, j] = u'U[:,i]
        u -= H[i, j] * U[:,i]
    end
    H[j + 1, j] = √(u'u)
    u /= H[j + 1, j]

    U = [U u]
end
~~~
:::::

:::

# Restarted Arnoldi iteration [@vaes22, p. 157]

~~~ julia
p = 10

u = # Initial guess
for k in 1:N
    # Calculate H and U
    U = u / √(u'u)
    H = zeros(p)
    for j in 1:p
        u = A * u

        # Gram-Schmidt
        for i in 1:j
            H[i, j] = u'U[:,i]
            u -= H[i, j] * U[:,i]
        end
        H[j + 1, j] = √(u'u)
        u /= H[j + 1, j]

        U = [U u]
    end

    # Largest Ritz vector
    u = eigen(H).vectors[:,end]
end
~~~

# When $\mat A$ is symmetric

::: proposition
If $\mat A$ is symmetric,
the matrix $\mat H = \mat U^T \mat A \mat U$
is tridiagonal and symmetric.
:::

::: info
In particular, a full Gram-Schmidt algorithm is not necessary.
:::

# Lanczos iteration [@vaes22, p. 158]

::: exercise

Adapt the previous algorithm (given below)
to the fact that $\mat H$ is tridiagonal and symmetric.

~~~ julia
p = 10

u = # Initial guess
for k in 1:N
    # Calculate H and U
    U = u / √(u'u)
    H = zeros(p)
    for j in 1:p
        u = A * u

        # Gram-Schmidt, TODO: to simplify
        for i in 1:j
            H[i, j] = u'U[:,i]
            u -= H[i, j] * U[:,i]
        end
        H[j + 1, j] = √(u'u)
        u /= H[j + 1, j]

        U = [U u]
    end

    # Largest Ritz vector
    u = eigen(H).vectors[:,end]
end
~~~

:::

# Bibliography
