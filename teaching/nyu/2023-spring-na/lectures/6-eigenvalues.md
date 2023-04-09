---
title: "Chapter 6: Numerical computation of eigenvalues"
output: revealjs
split: true
notes: |
  - 05/04: Random browsing, stochastic matrices, PageRank and eigenvalues (1-11)
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
\begin{align*}
\angle (\vec x, \vec y)
\defeq \arccos\left(
\frac {\abs {\ip{\vec x, \vec y}}} {\norm {\vec x} \norm {\vec y}}
\right)
\end{align*}
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

# Inverse iteration

::: proposition
Let $\mu \notin \spectrum \mat A$.
\begin{align*}
\mat A \vec x = \lambda \vec x
\iff
(\mat A - \mu \mat I)^{-1} \vec x
= \frac 1 {\lambda - \mu} \vec x.
\end{align*}
:::

::: remark
Note that if $\mu \approx \lambda$,
then the *power iteration* applied to $(\mat A - \mu \mat I)^{-1}$
will provide an estimation of the vector $\vec x$ that satisfies
\begin{align*}
(\mat A - \mu \mat I)^{-1} \vec x
= \frac 1 {\lambda - \mu} \vec x,
\end{align*}
which is the eigenvector of $\mat A$ associated with $\lambda$.
:::

# Implementation of inverse iteration [@vaes22, p. 147]

::: info
Solving the system $\mat A \vec x = \vec b$
can be done efficiently via `x = A \ b`{.julia}
instead of `x = A^(-1) * b`{.julia}.
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

# Railey quotient iteration [@vaes22, p. 148]

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

# QR decomposition with Julia

~~~ {.julia .jupyter}
using LinearAlgebra
Y = [3 1; 6 2; 0 2]
Q, R = qr(A)
~~~

# Simultaneous iteration: algorithm [@vaes22, p. 150]

\begin{align*}
\mat Y_k &\defeq \vec A \mat X_k\\
\mat X_{k + 1} &\defeq \text{orthonormalize the columns of} \ \mat Y_k
\end{align*}

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

# Bibliography
