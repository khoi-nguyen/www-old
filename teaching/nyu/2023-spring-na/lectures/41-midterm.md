---
title: Midterm
output: revealjs
...

# Gregory-Newton {.split}

::: question
Using *Gregory-Newton interpolation*, show that
\begin{align*}
S(n) = \sum_{i = 1}^n i^3 = \frac {n^4} 4 + \frac {n^3} 2 + O(n^2)
\end{align*}
:::

# Trapezoidal rule {.split}

::: question
Hence, use the *trapezoidal rule* with the nodes
$$x_i = \frac i n, \quad i = 0, \dots, n, \qquad h = \frac 1 n,$$
to approximate $\int_0^1 x^3 \dd x$.
Calling your approximation $\widehat I_n$,
Show that
\begin{align*}
  \widehat I_n = \frac 1 4 + O(n^{-2})
\end{align*}
:::

# Gram-Schmidt {.split}

\begin{align*}
\int_{-1}^1 \frac {x^n} {\sqrt {1 - x^2}} \dd x
= \begin{cases}
0 & \quad \text{ if } n = 1, 3, 5\\
\pi & \quad \text{ if } n = 0\\
\pi/2 & \quad \text{ if } n = 2\\
3 \pi / 8 & \quad \text{ if } n = 4
\end{cases}
\end{align*}


::: question
Applying the *Gram-Schmidt algorithm* to $1$, $x$, $x^2$
with respect to $\ip{\cdot, \cdot}_C$ or otherwise,
get an explicit formula for $\varphi_0$, $\varphi_1$, $\varphi_2$.
:::

# Gram-Schmidt {.split}

::: question
Compare the roots of $\varphi_0, \varphi_1, \varphi_2$ to that of the *Chebyshev polynomials*.
What do you notice?
Hence, use your observation to find $\varphi_3$, a polynomial of degree $3$ that is orthogonal to $\varphi_0, \dots, \varphi_2$.
:::

# Quadrature {.split}

::: question
Let us consider the *Gauss-Chebyshev quadrature rule*
\begin{align*}
\int_{-1}^1 \frac {u(x)} {\sqrt{1 - x^2}} \dd x
\approx w_0 u(x_0) + w_1 u(x_1) + w_2 u(x_2)
\end{align*}
and assume its *degree of precision* is $5$.
Use that quadrature rule to show that
\begin{align*}
q(x) = (x - x_0) (x - x_1) (x - x_2)
\end{align*}
satisfies $\ip {q, x^n}_C = 0$ for $n = 0, \dots, 2$.

Hence deduce that $q = K \varphi_3$ and hence find the values $x_0$, $x_1$ and $x_2$.
:::

# Weights of the quadrature rule {.split}

::: question
Consider a polynomial $u$ of degree $2$.
By applying the *Gauss-Chebyshev quadrature*
to its expression in the *Lagrange basis* $l_i$, $i = 0, 1, 2$ (which needs not be calculated),
show that
\begin{align*}
w_i = \int_{-1}^1 \frac {l_i(x)} {\sqrt {1 - x^2}} \dd x,
\qquad i = 0, 1, 2
\end{align*}
where $l_i$ is the *Lagrange polynomial* associated with $x_i$.
:::

# Positivity of the weights {.split}

::: {.info title="Gauss-Chebyshev"}
\begin{align*}
\int_{-1}^1 \frac {u(x)} {\sqrt{1 - x^2}} \dd x
\approx w_0 u(x_0) + w_1 u(x_1) + w_2 u(x_2)
\end{align*}
:::

::: question
Consider a polynomial $u$ of degree $2$.
By applying the *Gauss-Chebyshev quadrature*
to its expression in the *Lagrange basis* $l_i$, $i = 0, 1, 2$,
show that
\begin{align*}
w_i = \int_{-1}^1 \frac {l_i(x)} {\sqrt {1 - x^2}} \dd x,
\qquad i = 0, 1, 2
\end{align*}
where $l_i$ is the *Lagrange polynomial* associated with $x_i$.
:::

# Bound {.split}

::: question
Using the properties of the Chebyshev polynomials,
show that
\begin{align*}
\int_{-1}^1 \frac {q^2(x)} {\sqrt{1 - x^2}} \dd x \leq \frac \pi {16}.
\end{align*}
:::

::: info
\begin{align}
p(x) = 2^{-n + 1} T_n(x) \text{ is monic and } |p(x)| \leq 2^{-n + 1}
\end{align}
:::

