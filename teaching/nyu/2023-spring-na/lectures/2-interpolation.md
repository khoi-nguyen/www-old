---
title: "Chapter 2: Interpolation and Approximation"
output: revealjs
notes: |
  - 30/01: Lagrange and equidistant Gregory-Newton interpolation (slides 1-14)
  - 01/02: Non equidistant Gregory-Newton, interpolation error (15-22)
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

# Summary

- Homework due on Monday!
- Read Julia appendix

::::: row

::::: {.col}

## Lagrange

$$\widehat u(x)
= \sum_{i = 0}^n u_i
\overbrace{
\underbrace{\frac {\prod_{j \neq i} (x - x_j)} {\prod_{j \neq i} (x_i - x_j)}}_{
\substack{
1 \text{ when } x = x_i,\\
0 \text{ when } x = x_j \neq x_i
}
}
}^{\text{Lagrange polynomial}}$$

- Evaluating $\widehat u$ is costly
- Lagrange polynomials change when adding nodes
- Numerically unstable because of cancellation between large terms

:::::

::::: {.col}

## Gregory-Newton

$$\widehat u(x) = \sum_{i = 0}^n \frac 1 {i!}
\underbrace{\Delta^i u(0)}_{\text{depends only on } u(n)}
\overbrace{\prod_{j = 0}^{i - 1} (x - x_j)}^{\text{falling powers}}$$

- Good for incremental interpolation
- Numerically more stable
- Efficient evaluation possible via Horner's method

:::::

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
and let $x_0, \dots, x_n$ denote $n + 1$ distinct interpolation nodes.
Then for each $x \in [a, b]$,
we can find $\xi \in [a, b]$ such that
$$u(x) - \widehat u(x) =
\frac {u^{(n + 1)}(\xi)}{(n + 1)!} (x - x_0) \dots (x - x_n)$$
:::

# Last time...

\begin{align}
p(x) = \sum_{i = 0}^n \frac 1 {i!} u^{(i)}(0) x^n
\quad \Longrightarrow \quad
p(x) = \sum_{i = 0}^n \frac 1 {i!} \Delta^i u(0)
\overbrace{\prod_{j = 0}^{i - 1} (x - j)}^{\text{falling}\ \text{powers}}
\quad \Longrightarrow \quad
p(x) = \sum_{i = 0}^n \underbrace{\overbrace{[u_0, \dots, u_i]}^{\text{divided}\ \text{differences}}}_{
\substack{
[u_0] = u_0\\
[u_0, \dots, u_n] = \frac {[u_1, \dots, u_n] - [u_0, \dots, u_{n - 1}]} {x_n - x_0}
}
}
\prod_{j = 0}^{i - 1} (x - x_j)
\end{align}

:::::::::: row
::::: {.col}

#### Divided differences in Julia

~~~ julia
function diff(X, Y)
    if size(Y, 1) == 1
        return Y[1]
    end
    num = diff(X[2:end], Y[2:end]) - diff(X[1:end - 1], Y[1:end - 1])
    den = X[end] - X[1]
    return num / den
end
~~~
:::::
::::: {.col}

#### Gregory-Newton Interpolation in Julia

~~~ julia
function interp(X, Y, x)
    result = 0
    phi = 1
    for i in eachindex(X)
        result += diff(X[1:i], Y[1:i]) * phi
        phi *= x - X[i]
    end
    return result
end
~~~

:::::
::::::::::

#### Interpolation error (go over again)

$$\boxed{u(x) - \widehat u(x) =
\frac {u^{(n + 1)}(\xi)}{(n + 1)!} (x - x_0) \dots (x - x_n)}$$

#### Announcements

- Homework on $\sqrt 6$ due tonight
- **New homework** due on Monday 13 February (Exercise 2.13) (start together during recitation)
- **French sentence of the day**: "J'étudie à l'université de George Santos et Rudy Giuliani".
- Printed copies of lecture notes: Mistral Photo, 40 rue Saint-Jacques.

# Interpolation error [@vaes22, p.32] {.split}

::: {.theorem title="Interpolation Error (examinable)"}
Assume that $u \in C^{n + 1}([a, b])$
and let $x_0, \dots, x_n$ denote $n + 1$ distinct interpolation nodes.
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

::: {.proposition title="Upper bound on the interpolation error (examinable)"}
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
and let $x_0, \dots, x_n$ denote $n + 1$ distinct interpolation nodes.
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

# Are Chebyshev polynomials really polynomials? [@vaes22, p. 184] {.split}

::: proposition
Let $T_n(x) = \cos(n \overbrace{\arccos x}^\theta)$.
We have

\begin{align}
T_n(x)
&= \sum_{j = 0}^{\lfloor n/2 \rfloor} \binom n {2j} x^{n - 2j} (x^2 - 1)^j\\
T_{n + 1}(x)
&= 2 x T_n(x) - T_{n - 1}(x)
\end{align}
:::

::: {.corollary .fragment}
Let $n \in \N$. The function $p_n(x) = 2^{-n + 1} T_n(x)$ is a monic polynomial.
:::

# Chebyshev polynomials

\begin{align}
T_0(x) &= 1 \\
T_1(x) &= x \\
T_2(x) &= 2x^2 - 1 \\
T_3(x) &= 4x^3 - 3x \\
T_4(x) &= 8x^4 - 8x^2 + 1 \\
T_5(x) &= 16x^5 - 20x^3 + 5x \\
T_6(x) &= 32x^6 - 48x^4 + 18x^2 - 1 \\
T_7(x) &= 64x^7 - 112x^5 + 56x^3 - 7x \\
T_8(x) &= 128x^8 - 256x^6 + 160x^4 - 32x^2 + 1 \\
T_9(x) &= 256x^9 - 576x^7 + 432x^5 - 120x^3 + 9x \\
T_{10}(x) &= 512x^{10} - 1280x^8 + 1120x^6 - 400x^4 + 50x^2-1 \\
T_{11}(x) &= 1024x^{11} - 2816x^9 + 2816x^7 - 1232x^5 +220x^3 - 11x
\end{align}

# Monic Chebyshev polynomials {.row}

::::: {.col}
~~~ {.julia .plot}
x = -1:0.01:1
f(x, n) = 2.0^(-n + 1) * cos(n * acos(x))
for n in 1:5
  plot!(x, f.(x, n), framestyle =:origin)
end
~~~
:::::

::::: {.col}
~~~ {.julia .plot}
x = -1:0.01:1
f(x, n) = 2.0^(-n + 1) * cos(n * acos(x))
for n in 6:10
  plot!(x, f.(x, n), framestyle =:origin)
end
~~~
:::::

# Chebyshev nodes [@vaes22, p. 37] {.split}

::: {.corollary title="Chebyshev nodes (examinable)"}
The function
$$\omega(x) = (x - x_0) (x - x_1) \dots (x - x_n),$$
where $\{x_0, x_1, \dots, x_n\} \subset [a, b]$
is $\infty$-minimized when
$$x_i = a + (b - a) \frac {1 + \cos\left(\frac {(2i + 1) \pi} {2n + 2}\right)} 2.$$
:::

# Interpolation of Runge with Chebyshev nodes [@vaes22, p. 38]

![](/static/images/1675252176.png){height=900}

# Approximation [@vaes22, p. 40]

::: row

::::: {.col}

## Least squares approximation of data points

::: problem
Let $\varphi_0, \dots, \varphi_m \in C([a, b])$.
Given $n + 1$ distinct interpolation nodes $\{x_0, \dots, x_n\} \subset [a, b]$
find
$$\widehat u(x) = \alpha_0 \varphi_0(x) + \dots + \alpha_m \varphi_m(x)$$
the "best approximation" of $u : \{x_0, \dots, x_n\} \to \R$ in $\span \{\varphi_0, \dots, \varphi_m\}$.
:::

:::::

::::: {.col}

## Mean square approximation of functions

::: problem
Let $\varphi_1, \dots, \varphi_m \in C([a, b])$.
Given a function $u : [a, b] \to \R$,
$$\widehat u(x) = \alpha_0 \varphi_0(x) + \dots + \alpha_m \varphi_m(x)$$
the "best approximation" of $u$ in $\span \{\varphi_0, \dots, \varphi_m\}$.
:::

:::::

:::

::: {.block title="Comments"}
In both cases:

- We have too many $x$ values and not enough degrees of freedom with the $\alpha_i$ to interpolate.
- We need to define the notion of **best approximation**.
- The answer will depend on our notion of best approximation.
:::

# Least squares approximation of data points [@vaes22, p. 40] {.split}

Remember that interpolation was solving the system.

\begin{align}
\underbrace{
\begin{pmatrix}
\varphi_0(x_0) & \varphi_1(x_0) & \dots & \varphi_m(x_0)\\
\varphi_0(x_1) & \varphi_1(x_1) & \dots & \varphi_m(x_1)\\
\varphi_0(x_2) & \varphi_1(x_2) & \dots & \varphi_m(x_2)\\
\vdots & \vdots & \vdots & \vdots\\
\varphi_0(x_{n - 1}) & \varphi_1(x_{n - 1}) & \dots & \varphi_m(x_{n - 1})\\
\varphi_0(x_n) & \varphi_1(x_n) & \dots & \varphi_m(x_n)
\end{pmatrix}
}_{A}
\underbrace{
\begin{pmatrix}
\alpha_0 \\ \alpha_1 \\ \alpha_2 \\ \vdots \\ \alpha_m
\end{pmatrix}
}_{\boldsymbol \alpha}
=
\underbrace{
\begin{pmatrix}
u_0 \\ u_1 \\ u_2 \\ \vdots \\ u_{n - 1} \\ u_n
\end{pmatrix}
}_{\boldsymbol b}
\end{align}

As $m < n$, the equation $A \boldsymbol \alpha - \boldsymbol \beta = 0$ will not necessarily have a solution.
We will try to **minimise** $\| A \boldsymbol \alpha - \boldsymbol b \|_2$ instead.

# Normal equations [@vaes22, p. 41] {.split}

::: theorem
Assume that $\boldsymbol \alpha_\star$ minimizes
$\boldsymbol \alpha \mapsto \|A \boldsymbol \alpha - \boldsymbol b \|_2$.

Then $\boldsymbol \alpha_\star$ satisfies
$$A^T A \boldsymbol \alpha_\star = A^T \boldsymbol b$$

The solution is unique if the columns of $A$ are linearly independent.
:::

::: remark
Note that $\boldsymbol \alpha_\star = (A^T A)^{-1} A^T b$.
The matrix $A^+ = (A^T A)^{-1} A^T$ satisfies $A^+A = I$,
and is called the Moore-Penrose pseudoinverse of $A$.

In Julia, the backslash operator uses the Moore-Penrose pseudo-inverse,
so that $\boldsymbol \alpha_\star$ can be found via `α = A \ b`{.julia}
:::

# From "least square" to "mean square" approximations {.split}

Previously, we sought to minimize
$$\sum_{i = 0}^n |u_i - \widehat u(x_i)|^2$$
which is equivalent to minimizing
$$\frac 1 n \sum_{i = 0}^n |u_i - \widehat u(x_i)|^2.$$

The advantage of the latter is that it may converge as $n \to +\infty$.

::: {.proposition}
Let $f \in C([a, b])$.

$$\lim_{n \to \infty} \frac 1 n \sum_{i = 0}^{n} \left|f(x_i)\right|^2
= \frac 1 {b - a} \int_a^b \left|f(x)\right|^2 \dd x$$
:::

# Mean square approximation of functions {.split}

::: problem
Let $\varphi_1, \dots, \varphi_m \in C([a, b])$.
Given a function $u : [a, b] \to \R$,
find
$$\widehat u(x) = \alpha_0 \varphi_0(x) + \dots + \alpha_m \varphi_m(x)$$
such that it minimizes
$$\int_a^b \left|u(x) - \widehat u(x)\right|^2 \dd x.$$
:::

# Scalar products

:::::::::: row
::::: {.col}

### On $\R^n$

$$\langle x, y \rangle = \sum_{i = 1}^n x_i y_i.$$
$$\|x\|_2 = \sqrt{\langle x, x \rangle}$$
:::::

::::: {.col}

### On $C([a, b])$, or rather $L^2([a, b])$.

$$\langle f, g \rangle = \int_a^b f(x) g(x) \dd x.$$
$$\|f\|_2 = \sqrt{\langle f, f \rangle}$$
:::::
::::::::::

::: {.block title="Properties"}
In both cases, the map $\langle \cdot, \cdot \rangle$ is

- symmetric
- bilinear
- positive definite.

In other words, it's a **scalar product**.
:::

# Bibliography
