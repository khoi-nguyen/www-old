---
title: "Chapter 3: Numerical Integration"
output: revealjs
notes: |
  - 13/02: Newton-Cotes method, composite trapezium rule (1-13)
  - 15/02: Composite Simpson rule, Romberg (14-22)
...

# International Day of Women and Girls in Science (11/02) {.row}

::::: {.col}
![](/static/images/1676240183.png){height=100%}
:::::

::::: {.col}
<iframe src="https://en.wikipedia.org/wiki/Timeline_of_women%27s_education" height=800 width="100%">
</iframe>
:::::

# Numerical integration {.row}

::::: {.col}
- We will assume without loss of generality that we're working on $[-1, 1]$.
  $$\int_a^b u(x) \dd x = \frac {b - a} 2 \int_{-1}^1 u\left(\frac {b - a} 2 + t \frac {b - a} 2\right) \dd t$$
- A few facts from last chapter to keep in mind:

  Lagrange polynomials
  : $$\widehat u(x) = \sum_{i = 0}^n u_i \varphi(x), \quad
  \varphi_i(x) = \prod_{j \neq i} \frac {x - x_j} {x_i - x_j}$$

  Interpolation error
  :  $$\widehat u(x) - u(x) = \frac{u^{(n + 1)}(\xi)} {(n + 1)!} (x - x_0) \dots (x - x_n)$$
:::::

::::: {.col}

### Annoucements

- Office hours: just send me an email
- Homework on interpolation: due tonight
- Next homework: Exercise 3.6, due next monday
- French sentence of the day: "Je fais grève aujourd'hui" (I'm on strike today).
  Can be used when you don't want to answer your lecturer's questions.
- Homework 1 and 2 will be marked before Monday the 20th (sorry!)s
:::::

# Closed Newton-Cotes method [@vaes22, p. 55] {.split}

Let $-1 = x_0 < x_1 < \dots < x_{n - 1} < x_n = 1$ be equidistant points
and let us try to estimate the integral of 
$$u : \{x_0, \dots, x_n\} \to \R.$$

::: {.exampleblock title="Newton-Cotes method"}
Step 1
: Construct the interpolating polynomial $\widehat u$
  going through $(x_i, u(x_i))$, with $i = 0, \dots, n$.

Step 2
: Calculate $$\int_{-1}^1 \widehat u(x) \dd x.$$
:::

# Closed Newton-Cotes [@vaes22, p. 55] {.row}

::::: {.col}
~~~ {.julia .plot}
using Polynomials
x = LinRange(-1, 1, 1000)
X = LinRange(-1, 1, 2)
f(x) = x^3 + 2
p = Polynomials.fit(X, f.(X))
plot(x, f.(x), label=L"x^3 + 2", framestyle=:origin)
plot!(x, p.(x), label=L"\widehat u(x)")
~~~
:::::

::::: {.col}
~~~ {.julia .plot}
using Polynomials
x = LinRange(-1, 1, 1000)
X = LinRange(-1, 1, 3)
f(x) = sin(x)
p = Polynomials.fit(X, f.(X))
plot(x, f.(x), label=L"\sin x", framestyle=:origin)
plot!(x, p.(x), label=L"\widehat u(x)")
~~~
:::::

# Closed Newton-Cotes: weights [@vaes22, p. 55] {.split}

::: proposition
The Newton-Cotes approximation of the integral is given by
$$\sum_{i = 0}^n u(x_i) \underbrace{\int_{-1}^1 \varphi_i(x) \dd x}_{w_i},$$
where $\varphi_0, \dots, \varphi_n$ are the Lagrange polynomials associated with $x_0, \dots x_n$.
Moreover, it is **exact** for polynomials of degree less than or equal to $n$.
:::

# Finding the weights [@vaes22, p. 55] {.row}

::::: {.col}
$$\boxed{w_i = \int_{-1}^1 \varphi_i(x) \dd x}$$

~~~ julia
using SymPy
@vars x
n = 2
nodes = [-1 + Rational(2 * i, n) for i in 0:n]

function lagrange(nodes, xi)
    num = prod(x - n for n in nodes if n != xi)
    den = prod(xi - n for n in nodes if n != xi)
    return num / den
end

[integrate(lagrange(nodes, xi), (x, -1, 1)) for xi in nodes]
~~~
:::::

::::: {.col}

$n$      Name                          Formula
-----    ------                        --------
$1$      Trapezoidal rule              $$u(-1) + u(1)$$
$2$      Simpson's rule                $$\frac 1 3 u(-1) + \frac 4 3 u(0) + \frac 1 3 u(1)$$
$3$      Simpson's $\frac 3 8$ rule    $$\frac 1 4 u(-1) + \frac 3 4 u(-1/3) + \frac 3 4 u(1/3) + \frac 1 4 u(1)$$
$4$      Bode's rule                   $$\frac 7 {45} u(-1) + \frac {32} {45} u\left(-\frac 1 2\right) + \frac {12} {45} u(0)\\ + \dots$$

:::::

# Finding the weights II [@vaes22, p. 55] {.split}

Another way to find the weights is to solve the system

$$\sum_{i = 0} w_i x_i^p = \int_{-1}^1 x^p \dd x$$

\begin{align}
\underbrace{
\begin{pmatrix}
1 & 1 & \dots & 1 & 1\\
x_0 & x_1 & \dots & x_{n - 1} & x_n\\
\vdots & \vdots & & \vdots & \vdots\\
x_0^{n - 1} & x_1^{n - 1} & \dots & x_{n - 1}^{n - 1} & x_n^{n - 1}\\
x_0^n & x_1^n & \dots & x_{n - 1}^n & x_n^n
\end{pmatrix}
}_A
\underbrace{
\begin{pmatrix}
w_0 \\ w_1 \\ \vdots \\ w_{n - 1} \\ w_n
\end{pmatrix}
}_w
=
\underbrace{
\begin{pmatrix}
\int_{-1}^1 1 \dd x \\
\int_{-1}^1 x \dd x \\
\vdots \\
\int_{-1}^1 x^{n - 1} \dd x \\
\int_{-1}^1 x^n \dd x
\end{pmatrix}
}_b
\end{align}

~~~ julia
using SymPy
@vars x
n = 2
nodes = [-1 + Rational(2*i, n) for i in 0:n]
b = [integrate(x^p, (x, -1, 1)) for p in 0:n]
A = [x^p for p in 0:n, x in nodes]
A^-1 * b
~~~

# Degree of precision [@vaes22, p. 57] {.split}

::: definition
The degree of precision of an integration method
is the largest integer $d$ such that
all polynomials of degree less than or equal to $d$ are integrated exactly via this method.
:::

::::: {.col}

$n$      Name                          Formula
-----    ------                        --------
$1$      Trapezoidal rule              $$u(-1) + u(1)$$
$2$      Simpson's rule                $$\frac 1 3 u(-1) + \frac 4 3 u(0) + \frac 1 3 u(1)$$
$3$      Simpson's $\frac 3 8$ rule    $$\frac 1 4 u(-1) + \frac 3 4 u(-1/3) + \frac 3 4 u(1/3) + \frac 1 4 u(1)$$
$4$      Bode's rule                   $$\frac 7 {45} u(-1) + \frac {32} {45} u\left(-\frac 1 2\right) + \frac {12} {45} u(0)\\ + \dots$$

:::::

# Interpolation is not enough [@vaes22, p. 56]

Remember that the Newton-Cotes method would not integrate the Runge function correctly,
as the interpolating polynomial does not converge uniformly towards it.

Moreover, for larger values of $n$, the weights become negative (round-off errors).

![](/static/images/1675249748.png){height=800}

# Composite methods [@vaes22, p. 57] {.split}

We'll use **piecewise interpolation** [@vaes22, p.39] to ensure uniform convergence
towards the function as the number of nodes goes to infinity.

::: {.exampleblock title="Composite methods"}
#. We start with equidistant nodes $a = x_0 < x_1 < \dots < x_{n - 1} < x_n = b$
#. We apply the Newton-Cotes method to the intervals $[x_0, x_k]$, $[x_k, x_{2k}]$, $[x_{2 k}, x_{3 k}]$, $\dots$
#. Sum the results
$$\widehat I_a^b = \widehat I_{x_0}^{x_k} + \widehat I_{x_k}^{x_{2k}} + \dots + \widehat I_{x_{n - k}}^{x^k}$$
:::

# Composite trapezoidal rule [@vaes22, p. 58] {.split}

::: {.exampleblock title="Composite Trapezium rule"}
Let $a = x_0 < x_1 < \dots < x_{n - 1} < x_n = b$ be a collection
of equally distant nodes with $h = x_{i + 1} - x_i$.

Given $u: \{x_0, \dots, x_n\} \to \R$, the composite trapezium rule
is given by
$$\widehat I_h = \frac h 2 (u(x_0) + 2 u(x_1) + 2 u(x_2) + \dots + 2 u(x_{n - 1}) + u(x_n))$$
:::

~~~ julia
function composite_trapezium(u, a, b, n)
    x = LinRange(a, b, n + 1)
    y = u.(x)
    h = x[2] - x[1]
    return h/2 * sum([y[1]; 2 * y[2:end - 1]; y[end])
end
~~~

# Integration error for the composite trapezoidal rule [@vaes22, p. 58] {.split}

::: theorem
Let $a = x_0 < x_1 < \dots < x_{n - 1} < x_n = b$ be a collection
of equally distant nodes with $h = x_{i + 1} - x_i$.
The quantity
$$\widehat I_h = \frac h 2 (u(x_0) + 2 u(x_1) + 2 u(x_2) + \dots + 2 u(x_{n - 1}) + u(x_n))$$
satisfies
$$\left|\int_a^b u(x) \dd x - \widehat I_h\right| \leq
\frac {b - a} {12} \left(\sup_{[a, b]} |u''|\right) h^2$$
:::

# 15 February (or February 15) {.row}

::::: {.col}

### Composite Newton-Cotes

- Start with an equidistant division $$a = x_0 < x_1 < \dots < x_{n - 1} < x_n = b.$$
  We'll write $h = x_{i + 1} - x_i$.
- Piecewise interpolation of $u$ with a polynomial of degree $k$
  on $[x_0, x_k]$, $[x_k, x_{2k}]$, $\dots$, $[x_{n - k}, x_n]$
  to get $\widehat u$
- Integrate $\widehat u$:
  $$\int_a^b u(x) \dd x \approx \overbrace{\int_a^b \widehat u(x) \dd x}^{\widehat I_h}.$$

### Trapezoidal rule with Julia

~~~ julia
function composite_trapezium(u, a, b, n)
    x = LinRange(a, b, n + 1)
    y = u.(x)
    h = x[2] - x[1]
    return h/2 * sum([y[1]; 2 * y[2:end - 1]; y[end])
end
~~~

:::::

::::: {.col}

### Trapezoidal rule $(k = 2)$

- Weights have ratio $1:1$
- Composite rule gives twice the weight to nodes that belong to two trapezia
  $$\widehat I_h = \frac h 2 (u(x_0) + 2 u(x_1) + 2 u(x_2) + \dots + 2 u(x_{n - 1}) + u(x_n))$$
- Error associated with the trapezoidal rule is $O(h^2)$:
  $$\left|\int_a^b u(x) \dd x - \widehat I_h\right| \leq
  \frac {b - a} {12} \left(\sup_{[a, b]} |u''|\right) h^2$$

#### French sentence of the day

- "Je veux parler à votre supérieur" (I want to speak to your manager)

#### Announcements

- Homework on Gauss-Hermite due on Monday

:::::

# Composite Simpson rule [@vaes22, p. 59] {.split}

::: {.block title="Non-composite Simpson rule"}
$$\int_{-1}^1 u(x) \dd x \approx \frac 1 3 u(-1) + \frac 4 3 u(0) + \frac 1 3 u(1)$$
:::

::: {.block title="Composite Simpson rule"}
\begin{align}
\widehat I_h = \frac h 3 ( u(x_0) + & 4 u(x_1) + 2 u(x_2) \\
+ & 4 u(x_3) + 2 u(x_4) + \dots \\
+ & 4 u(x_{n - 1}) + u(x_n) )
\end{align}
:::

~~~ julia
function composite_simpson(u, a, b, n)
    x = LinRange(a, b, n + 1)
    y = u.(x)
    h = x[2] - x[1]
    return h/2 * sum([y[1]; y[end]; 4 y[2:2:end-1]; 2 y[3:2:end-2])
end
~~~

# Integration error for the composite Simpson rule [@vaes22, p. 59] {.split}

::: theorem
Let $a = x_0 < x_1 < \dots < x_{n - 1} < x_n = b$ be a collection
of equally distant nodes with $h = x_{i + 1} - x_i$.
The quantity
$$\widehat I_h = \frac h 3 \left( u(x_0) + 4 u(x_1) + 2 u(x_2) + \dots + 4 u(x_{n - 1}) + u(x_n)\right)$$
satisfies
$$\left|\int_a^b u(x) \dd x - \widehat I_h\right| \leq
\frac {b - a} {180} \left( \sup_{[a,b]} \left|u^{(4)}\right| \right) h^4$$
:::

# A posteriori estimation of the error [@vaes22, p. 60] {.split}

Without explicitely knowing the value $I$ of the integral,
we can estimate the error via

$$|I - \widehat I_h| \approx \frac 1 {15} |\widehat I_h - \widehat I_{2h}|$$

![](/static/images/1676285317.png){width=100%}

# Richardson extrapolation [@vaes22, p. 62] {.split}

Using a Taylor expansion,

\begin{align}
J(h) &= J(0) + J'(0) h + O(h^2)\\
J\left(\frac h 2\right) &= J(0) + J'(0) \frac h 2 + O(h^2).
\end{align}

Let us consider $J_1(h/2) = \alpha J(h) + \beta J(h/2)$.

# Elimination of the quadratic error term [@vaes22, p. 62] {.split}

We can reapply the procedure to eliminate the quadratic term.

\begin{align}
J_1(h / 4) &= J(0) - J^{(2)}(0) \frac {h^2} {16} + O(h^3)\\
J_1(h / 2) &= J(0) - J^{(2)}(0) \frac {h^2} 4 + O(h^3)\\
\end{align}

# Generalisation [@vaes22, p. 64] {.split}

![](/static/images/1676465786.png)

$$\boxed{J_i(h/2^i) = \frac {
2^i J_{i - 1}(h/2^i) - J_{i - 1}(h/2^{i - 1})
}{2^i - 1}}$$

# When only even powers contribute [@vaes22, p. 64] {.split}

$$J(h) = J(0) + \frac {J''(0)} 2 h^2 + \frac {J^{(4)}} {4!} h^4 + O(h^6)$$

![](/static/images/1676451388.png)

$$\boxed{J_i(h/2^i) = \frac {
2^{2i} J_{i - 1}(h/2^i) - J_{i - 1}(h/2^{i - 1})
}{2^{2i} - 1}}$$

# Romberg's method [@vaes22, p. 64] {.split}

::: {.exampleblock title="Romberg's method"}
Apply Richardson's extrapolation to the trapezium rule
$$J(h) = \frac h 3 \left( u(x_0) + 4 u(x_1) + 2 u(x_2) + \dots + 4 u(x_{n - 1}) + u(x_n)\right)$$
:::

Note: $J$ only has an expansion in even powers.

# With non-equidistant nodes [@vaes22, p. 65] {.split}

$$\sum_{i = 0}^n w_i x_i^d = \int_{-1}^1 x^d \dd x$$

- Previously, the $x_i$ were fixed, so we could only change the $n + 1$ weights.
  This allowed to integrate $1$, $x$, $\dots$, $x^n$ exactly.
- If the $x_i$ are unknowns, this adds $n + 1$ additional degrees of freedom,
  allowing exact integration of $1$, $x$, $\dots$, $x^{2n + 1}$.

::: {.block title="Gauss-Legendre quadrature"}
Find $w_0$, $\dots$, $w_n$, $x_0$, $\dots$, $x_n$ such that
$$\sum_{i = 0}^n w_i x_i^d = \int_{-1}^1 x^d \dd x$$
for $d = 0, 1, \dots, 2n + 1$.
:::

# Example: Gauss-Legendre when two nodes ($n = 1$) [@vaes22, p. 66] {.split}

::: {.block title="Gauss-Legendre quadrature"}
Find $w_0$, $w_1$, $x_0$, $x_1$ such that
$$\sum_{i = 0}^n w_i x_i^d = \int_{-1}^1 x^d \dd x$$
for $d = 0, 1, \dots, 3$.
:::

# Orthogonality property with Gauss-Legendre {.split}

::: question
How can we find the nodes in Gauss-Legendre integration?
:::

It turns out $(x - x_0) \dots (x - x_n)$ satisfies an interesting property...

::: proposition
Let $w_0$, $\dots$, $w_n$, $x_0$, $\dots$, $x_n$ be such that
$$\sum_{i = 0}^n w_i x_i^d = \int_{-1}^1 x^d \dd x, \quad d = 0, 1, \dots, 2n + 1.$$

The polynomial $q(x) = (x - x_0) (x - x_1) \dots (x - x_n)$
is the unique polynomial of degree $n + 1$ (up to a multiplicative constant) such that

$$\int_{-1}^1 q(x) x^d = 0, \quad d = 0, 1, \dots, n.$$
:::


# Scalar product and Gram-Schmidt {.split}

$$\langle f, g \rangle = \int_{-1}^{1} f(x) g(x) \dd x$$

- Two functions $f, g$ are **orthogonal** if $\langle f, g \rangle = 0.$
- $||f|| = \sqrt {\int_{-1}^1 f^2(x) \dd x}$
- A family of orthogonal vectors is **orthonormal** if every element has norm $1$.

::: {.block title="Gram-Schmidt orthonormalisation"}

- Normalize the first vector $$e_1 = \frac {u_1} {||u_1||}$$
- To find the second vector
  $$e_2 = \frac {u_2 - \langle u_2, e_1 \rangle e_1} {||u_2 - \langle u_2, e_1 \rangle e_1||}$$
- To find the third
  $$e_3 = \frac {u_3 - \langle u_3, e_1 \rangle e_1 - \langle u_3, e_2 \rangle e_2} {||u_3 - \langle u_3, e_1 \rangle e_1 - \langle u_3, e_2 \rangle e_2||}$$

:::


# Legendre polynomials {.split}

::: definition
The family Legendre polynomials is the orthonormal sequence $(P_n)_n$ of polynomials
such that $P_n$ is of degree $n$ for each $n \in \N$.
:::

In the classical definition, Legendre polynomials are normalized differently.
As we'll only focus on their roots, this will not matter.

~~~ julia
using SymPy
@vars x
n = 3
base = []
for d in 0:n
  v = x^d

  # Make v orthogonal to the elements of 'base'
  for e in base
    v -= integrate(v * e, (x, -1, 1)) * e
  end
  # Normalize
  v = v / √(integrate(v * v, (x, -1, 1)))

  # Add it to 'base'
  push!(base, simplify(v))
end
base
~~~

# Gauss-Legendre quadrature [@vaes22, pp. 66-67] {.split}

::: theorem
The following equations hold
$$\sum_{i = 0}^n w_i x_i^d = \int_{-1}^1 x^d \dd x,
\quad d = 0, 1, \dots, 2n + 1$$
if and only if the following conditions hold:

- $x_0, \dots, x_n$ are the roots of $L_{n + 1}$.
- the weights are given by
  $$w_i = \int_{-1}^1 \prod_{j \neq i} \frac {x - x_j} {x_i - x_j} \dd x.$$

In addition, all the weights are positive.
:::

# Generalization to higher dimension [@vaes22, p. 68] {.split}

Assume that we have a Gauss-Legendre rule with precision $k$, i.e.

$$
\int_{-1}^1 u(x) \dd x - \sum_{i = 0}^n w_i u(x_i) = O(h^k)
$$

Gauss-Legendre integration can easily be generalized in higher dimension,
with the same precision.
For example, in dimension $2$, we have

$$
\int_{-1}^1 \int_{-1}^1 u(x, y) \dd y \dd x
- \sum_{i = 0}^n \sum_{j = 0}^n w_i w_j u(x_i, y_i) = O(h^k).
$$

# Curse of dimensionality [@vaes22, p. 68] {.split}

\begin{align}
\int_{-1}^1 \dots \int_{-1}^1 &u(x_1, \dots, x_d) \dd x_d \dots \dd x_1\\
&- \sum_{i_1 = 1}^{n} \dots \sum_{i_d = 1}^n w_{i_1} \dots w_{i_d}
u(x_{i_1}, \dots, x_{i_d}) = O(h^k)
\end{align}

This estimate could be misleading
and leave the impression that higher dimensional is just
as good as its one-dimensional counterpart.
If $N$ is the number of $d$-dimensional nodes,

$$h = \frac 2 n = \frac 2 {\sqrt[d] N} = 2 N^{- \frac 1 d}$$

so that $O(h^k)$ is actually $O(N^{- \frac k d})$.

As $d$ grows, the convergence gets slower and slower.
Integration in dimension $d \gg 1$ is an active research area.

# Probabilistic methods [@vaes22, p. 68] {.split}

::: text-center
![](https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Pi_30K.gif/220px-Pi_30K.gif){width=40%}
:::

::: proposition
Let $X_n \sim \mathcal U(0, 1)$ be a sequence of independent uniformly distributed random variables.
If $u$ is integrable over $[0, 1]$, then
$$\frac 1 N \sum_{n = 1}^N u(X_n) \xrightarrow{\text{a.s.}} \int_0^1 u(x) \dd x$$
:::

~~~ julia
montecarlo(u, N) = 1 / N * sum(u.(rand(N)))
~~~

# Variance of the Monte-Carlo estimator [@vaes22, p. 69] {.split}

::: proposition
Let $X_n \sim \mathcal U(0, 1)$ be a sequence of independent uniformly distributed random variables.
If $u$ is square integrable over $[0, 1]$, then
the estimator
$$\widehat I_N = \frac 1 N \sum_{n = 1}^N u(X_n) \quad \text{of} \quad I = \int_0^1 u(x) \dd x$$
satisfies
$$\V(\widehat I_N) = \frac {1} N \int_0^1 |u(x) - I|^2 \dd x.$$
:::

::: remark
The standard deviation behaves like $O(N^{-\frac 1 2})$,
which is worse than the $1$-dimensional trapezium rule ($O(N^{-2})$).
However, Monte-Carlo does not suffer the curse of dimensionality
as the convergence is still $O(N^{-\frac 1 2})$ in higher dimensions.
:::

# Confidence interval {.split}

::: {.proposition title="Chebyshev's inequality"}
Let $X$ be an integrable random variable with finite variance $\sigma^2$
and with mean $\mu$.
Then for every $k > 0$, we have

$$\P(|X - \mu| \geq k \sigma) \leq \frac 1 {k^2}.$$
:::

::: proposition
Let $X_n \sim \mathcal U(0, 1)$ be a sequence of independent uniformly distributed random variables.
If $u$ is square integrable over $[0, 1]$, then
the estimator
$$\widehat I_N = \frac 1 N \sum_{n = 1}^N u(X_n) \quad \text{of} \quad I = \int_0^1 u(x) \dd x$$
satisfies
$$\P\left(\left|\widehat I_N - I\right| \leq \sqrt {\frac {\sigma^2} {N \alpha}}\right) \geq 1 - \alpha$$
:::


# Bibliography
