---
title: "Revisions"
output: revealjs
split: true
notes: |
...

# Exercise: Cholesky decomposition

![](/static/images/1682507879.png)

# Cholesky part II

![](/static/images/1682508069.png)

# QR factorization

![](/static/images/1682508142.png)

# Splittings

![](/static/images/1682508660.png)

# Splittings part 2

![](/static/images/1682509441.png)

# Eigenvalues

![](/static/images/1682508913.png)

# Nonlinear system

![](/static/images/1682509279.png)

# Generalized Banach fixed point theorem

We consider a splitting
$\mat A = \mat M - \mat N$ such that
$\rho(\mat M^{-1} \mat N) < 1$,
which yields the iteration
\begin{align*}
\vec x^{(k + 1)} = \mat M^{-1} \mat N \vec x^{(k)}
\end{align*}

Show that the iteration satisfies
\begin{align*}
\norm {\vec x^{(k + 1)} - \vec x^{(k)}}
\leq L^k \norm {\vec x^{(1)} - \vec x^{(0)}},
\quad
\sum_{k = 0}^{+\infty} L_k < +\infty.
\end{align*}

Hence, prove that the iteration converges towards a unique fixed point.

# Pagerank

::::: col
![](/static/images/1683113504.png)
:::::

::::: col
- Find the transition matrix (without damping)
- Find the transition matrix with a damping factor $\epsilon = 0.5$
- Find the PageRank vector with $\epsilon = 0.5$.
:::::

# Newton-Raphson

![](/static/images/1683114990.png)
![](/static/images/1683115102.png)
![](/static/images/1683115155.png)
![](/static/images/1683115372.png)

# Newton-Raphson: solutions {.nosplit}

<iframe src="https://personal.math.ubc.ca/~anstee/math104/104newton-solution.pdf" width="900" height="600">
</iframe>
