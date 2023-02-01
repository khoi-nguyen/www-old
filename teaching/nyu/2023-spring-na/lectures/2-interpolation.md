---
title: "Chapter 2: Interpolation and Approximation"
output: revealjs
notes: |
  - 30/01: Lagrange and equidistant Gregory-Newton interpolation (slides 1-14)
...

# Chapter 1 summary {.row}

::::: {.col}
- Floats are stored in binary with **finite precision**
- Computers can represent a finite subset of rational numbers
- Floats are denser around $0$ and are less dense as we get away from it.
- Machine $\epsilon$, useful to measure **relative** distance.
- Machine operations ($\widehat +, \widehat \times$):
  - Perform the exact operation
  - Pick the closest number in floating format
:::::

::::: {.col}
~~~ {.julia .plot}
p = -4:0.01:4
x = 2.0.^p
y = @. nextfloat(x) - x
plot(x, y, label=L"\Delta(x)")
title!("Distance to the successor")
xticks!(floor.(2.0.^(0:4)))
xlabel!(L"x")
yticks!(
  2.0.^(0:4).*eps(Float64),
  [latexstring(string(2^i) * "\\epsilon_{\\mathbb{F}}") for i in 0:4]
)
~~~
:::::

# Homework

::: question
Explain why `Float32(sqrt(6))^2 - 6` is not zero in Julia.
:::

::: info
- Have a look at $1.19$, $1.21$ for inspiration.
- Hand in as `.ipynb` file by email
- Due next Monday
:::

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

::: {.definition title="Lagrange polynomials"}
$$\varphi_i(x) = \frac{
\prod_{j \neq i} (x - x_j)
}{
\prod_{j \neq i} (x_i - x_j)
}$$
:::

::: {.proposition .fragment}
$$\varphi_i(x_j) = \delta_{ij} = \begin{cases}
1 & \text{if } i = j\\
0 & \text{otherwise}.
\end{cases}$$
:::

::: {.proposition .fragment}
The polynomial

$$\widehat u(x) = u_0 \varphi_0(x) + u_1 \varphi_1(x) + \dots + u_n \varphi_n(x)$$

goes through $(x_0, u_0)$, $(x_1, u_1)$, \dots, $(x_n, u_n)$.
:::

# Lagrange interpolation [@vaes22, pp. 27-28] {.split}

$$\varphi_i(x) = \frac{
\prod_{j \neq i} (x - x_j)
}{
\prod_{j \neq i} (x_i - x_j)
}$$
$$\widehat u(x) = u_0 \varphi_0(x) + u_1 \varphi_1(x) + \dots + u_n \varphi_n(x)$$

- Evaluating $\widehat u$ is costly when $n$ is large
- All the basis functions change when adding an interpolation node
- Numerically unstable because of cancellation between large terms
  see figure next slide).

# Lagrange polynomials [@vaes22, p. 28] {.split}

![](/static/images/1674991770.png)

# Gregory-Newton interpolation [@vaes22, p. 28] {.split}

This time, we'll work with **equidistant nodes**,
which we assume to be $0$, $1$, $\dots$, $n$,
as they provide a useful analogy with the Taylor formula.

Again, let's look for an interpolating polynomial $p$,
which can be written

$$p(x) = p(0) + p'(0) x + \frac {p''(0)} 2 x^2 + \dots + \frac {p^{(n)}(0)} {n!} x^n.$$

An idea would be approximate $p'(0) \approx \frac {p(1) - p(0)} {1}$.

# Forward difference $\Delta$ and falling powers [@vaes22, pp. 28-29] {.split}

::: {.definition title="Forward difference operator"}
$$\Delta f(x) = f(x + 1) - f(x)$$
:::

::: {.definition .fragment title="Falling power"}
$$x^{\underline k} = x (x - 1) (x - 2) \dots (x - k + 1)$$
:::

::: {.proposition .fragment title="Difference of falling power"}
$$\Delta x^{\underline k} = k x^{\underline{k - 1}}$$
:::

# Newton series [@vaes22, p. 29] {.split}

$$\boxed{
p(x) = p(0) + \Delta p(0) x^{\underline 1}
+ \frac {\Delta^2 p(0)} {2!} x^{\underline 2}
+ \dots
+ \frac {\Delta^n p(0)} {n!} x^{\underline n}
}$$

- The right-hand side only requires knowledge of $p(0), p(1), \dots p(n)$.

# Example [@vaes22, p. 29] {.split}

::: example
Find a closed expression of
$$S(n) = \sum_{i = 0}^n i^2$$
:::

# Lagrange vs Gregory-Newton [@vaes22, p. 29] {.split}

- When adding one interpolation node, only one coefficient needs be recalculated
- GN is more numerically stable, as the basis functions do not take very large values
- Efficient evaluation
$$p(x) = \alpha_0 + x\left(
\alpha_1 + (x - 1) \left(
\alpha_2 + (x - 2) \left(\dots\right)
\right)
\right)$$

# Summary {.row}

::::: {.col}

## Lagrange

$$\widehat u(x)
= \sum_{i = 0}^n u_i
\underbrace{\frac {\prod_{j \neq i} (x - x_j)} {\prod_{j \neq i} (x_i - x_j)}}_{
\substack{
1 \text{ when } x = x_i,\\
0 \text{ when } x = x_j \neq x_i
}
}$$

- Evaluating $\widehat u$ is costly
- Lagrange polynomials change when adding nodes
- Numerically unstable because of cancellation between large terms

:::::

::::: {.col}

## Gregory-Newton

$$\widehat u(x) = \sum_{i = 0}^n \frac 1 {i!}
\underbrace{\Delta^i u(0)}_{\text{depends only on } \left. u \right|_{\N}} x^{\underline i}$$

- Good for incremental interpolation
- Numerically more stable
- Efficient evaluation possible via Horner's method

:::::

# Divided differences [@vaes22, p. 30] {.split}

\begin{align}
[u_i] &= u_i\\
[u_i, u_j] &= \frac {u_j - u_i} {x_j - x_i}\\
[u_0, u_1, \dots, u_d] &= \frac {[u_1, \dots, u_d] - [u_0, \dots, u_{d - 1}]} {x_d - x_0}
\end{align}

::: proposition
Assume that $\sigma$ is a permutation of $\{0, \dots n\}$.
We have

$$[u_{\sigma(0)}, u_{\sigma(1)}, \dots, u_{\sigma(n)}]
= [u_0, u_1, \dots, u_n].$$
:::

Proof: Exercise $2.4$, [@vaes22, p. 48].

# Rewriting Gregory-Newton with divided differences

$$\widehat u(x) = u(0) + \Delta u(0) x + \frac 1 2 \Delta^2 u(0) x (x - 1) +
\frac 1 {3!} \Delta^3 u(0) x (x - 1) (x - 2) + \dots$$

::: split
\begin{align}
[u_i] &= u_i\\
[u_i, u_j] &= \frac {u_j - u_i} {x_j - x_i}\\
[u_0, u_1, \dots, u_d] &= \frac {[u_1, \dots, u_d] - [u_0, \dots, u_{d - 1}]} {x_d - x_0}
\end{align}

::: {.proposition .fragment}
$$\frac 1 {n!} \Delta^n u(k) = [u_k, u_{k + 1}, \dots, u_{k + n}]$$
:::
:::

# Rewriting Gregory-Newton

\begin{align}
\widehat u(x)
&= u(0) + \Delta u(0) x + \frac 1 2 \Delta^2 u(0) x (x - 1) +
\frac 1 {3!} \Delta^3 u(0) x (x - 1) (x - 2) + \dots\\
&= [u_0] + [u_0, u_1] x + [u_0, u_1, u_2] x (x - 1) + [u_0, u_1, u_2, u_3] x (x - 1) (x - 2) + \dots\\
&= [u_0] + [u_0, u_1] (x - x_0) + [u_0, u_1, u_2] (x - x_0) (x - x_1)
+ [u_0, u_1, u_2, u_3] (x - x_0) (x - x_1) (x - x_2) + \dots\\
\end{align}

We see that we'll take

$$\varphi_i(x) = \prod_{j = 0}^{i - 1} (x - x_j)
= (x - x_0) (x - x_1) \dots (x - x_{i - 1})$$

The Gregory-Newton formula becomes

$$\widehat u(x) = \sum_{i = 0}^n [u_0, \dots, u_{i}] \varphi_i(x)$$

# Non-equidistant nodes [@vaes22, p. 30] {.split}

\begin{align}
\varphi_0(x) &= 1\\
\varphi_1(x) &= (x - x_0),\\
\varphi_2(x) &= (x - x_0) (x - x_1),\\
&\vdots \\
\varphi_i(x) &= (x - x_0) (x - x_1) \dots (x - x_{i - 1}),\\
\end{align}

::: question
What does the system
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
become?
:::

# Non-equidistant Gregory-Newton interpolation [@vaes22, p. 30] {.split}

\begin{align}
[u_i] &= u_i\\
[u_i, u_j] &= \frac {u_j - u_i} {x_j - x_i}\\
[u_0, u_1, \dots, u_d] &= \frac {[u_1, \dots, u_d] - [u_0, \dots, u_{d - 1}]} {x_d - x_0}
\end{align}

::: proposition
Assume that $(x_0, u_0), \dots, (x_n, u_n)$ are such that the $x_i$ are distincts.

The interpolating polynomial of degree $n$ can be expressed by
$$\widehat u(x) = \sum_{i = 0}^n [u_0, u_1 \dots, u_i] \varphi_i(x),$$
where
$$\varphi_i(x) = (x - x_0) \dots (x - x_{i - 1})$$
:::

# Example of Gregory-Newton interpolation [@vaes22, p. 31] {.split}

::: example
Find the polynomial of degree $3$ that goes through
$$(-1, 10) \quad (0, 4) \quad (2, -2) \quad (4, -40)$$
:::

# Interpolation error [@vaes22, p.32] {.split}

::: {.theorem title="Interpolation Error (examinable)"}
Assume that $u \in C^{n + 1}([a, b])$
and let $x_0, \dots, x_n$ denote $n + 1$.
Then for each $x \in [a, b]$,
we can find $\xi \in [a, b]$ such that
$$u(x) - \widehat u(x) =
\frac {u^{(n + 1)}(\xi)}{(n + 1)!} (x - x_0) \dots (x - x_n)$$
:::

# Interpolation error [@vaes22, p.32] {.split}

::: {.theorem title="Interpolation Error (examinable)"}
Assume that $u \in C^{n + 1}([a, b])$
and let $x_0, \dots, x_n$ denote $n + 1$.
Then for each $x \in [a, b]$,
we can find $\xi \in [a, b]$ such that
$$u(x) - \widehat u(x) =
\frac {u^{(n + 1)}(\xi)}{(n + 1)!} (x - x_0) \dots (x - x_n)$$
:::

::: {.corollary title="Upper bound on the interpolation error (examinable)"}
Assume that $u$ is smooth on $[a, b]$. Then
$$\sup_{[a, b]} |u - \widehat u| \leq
\frac 1 {4(n + 1)} \left(\sup_{[a, b]} |u^{(n + 1)}|\right) h^{n + 1}$$
:::

# The Runge function {.row}

::::: {.col}
~~~ {.julia .plot}
x = -1:0.01:1
y = @. 1 / (1 + 25 * x^2)
plot(x, y)
~~~

::: {.proposition title="Upper bound on the interpolation error"}
Assume that $u$ is smooth on $[a, b]$. Then
$$\sup_{[a, b]} |u - \widehat u| \leq
\frac 1 {4(n + 1)} \left(\sup_{[a, b]} |u^{(n + 1)}|\right) h^{n + 1}$$
:::
:::::

::::: {.col}
$$f(x) = \frac 1 {1 + 25 x^ 2}$$

- Equidistant interpolation fails (especially at the edges of the interval)
- Shows that higher degree doesn't mean higher accuracy
- (Later) Succeeds with **Chebyshev nodes**
:::::

# Equidistant interpolation of the Runge function [@vaes22, p. 35]

![](/static/images/1675249748.png){height=900}

# Chebyshev nodes [@vaes22, p. 34] {.split}

::: {.theorem title="Interpolation Error (examinable)"}
Assume that $u \in C^{n + 1}([a, b])$
and let $x_0, \dots, x_n$ denote $n + 1$.
Then for each $x \in [a, b]$,
we can find $\xi \in [a, b]$ such that
$$u(x) - \widehat u(x) =
\frac {u^{(n + 1)}(\xi)}{(n + 1)!} (x - x_0) \dots (x - x_n)$$
:::

::: {.question .fragment}
How to find $x_0, x_1, \dots, x_n$ to minimize the interpolation error?
:::

::: {.question .fragment title="Moving the goalposts"}
Let $u \in \mathscr P^{n + 1}$.
Find the interpolation nodes $x_0, x_1, \dots, x_n$
which minimize the interpolation error
$$u(x) - \widehat u(x) = C (x - x_0)(x - x_1) \dots (x - x_n)$$
:::

# Chebyshev polynomials [@vaes22, p. 35] {.split}

Remember, we're trying to minimize
$$(x - x_0)(x - x_1) \dots (x - x_n),$$
which means we want to find the roots
which minimize the above **monic** polynomial.

::: {.theorem}
If $p$ is a **monic** polynomial of degree $n$,
then
$$\sup_{[-1, 1]} |p| \geq \frac 1 {2^{n - 1}}.$$

Moreover, the bound is achieved for
$$p_\star(x) = 2^{-n + 1} \underbrace{\cos (n \arccos x)}_{\text{Chebyshev polynomial}}.$$
:::

# Chebyshev nodes [@vaes22, p. 37] {.split}

::: corollary
The function
$$\omega(x) = (x - x_0) (x - x_1) \dots (x - x_n),$$
where $\{x_0, x_1, \dots, x_n\} \subset [a, b]$
is minimized when
$$x_i = a + (b - a) \frac {1 + \cos\left(\frac {(2i + 1) \pi} {2n + 2}\right)} 2.$$
:::

# Interpolation of Runge with Chebyshev nodes [@vaes22, p. 38]

![](/static/images/1675252176.png){height=900}

# Bibliography
