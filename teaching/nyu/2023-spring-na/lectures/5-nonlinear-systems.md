---
title: Solution of nonlinear systems
output: revealjs
...

# Starter {.row}

::::: {.col}

#### Plan for today

- Bisection method
- Linear, superlinear and quadratic convergence
- Banach fixed point theorem

:::::

::::: {.col}

#### Announcements

- Homework on relaxation method due on Monday 27
- French sentence of the day: "*J'invoque le 49.3*" with examples:

  - Donne-moi 100 euros, ou j'invoque le 49.3

![](/static/images/1679489658.png)
![](/static/images/1679491858.png)
![](/static/images/1679491880.png)


:::::

# Motivations {.split}

We shall attempt to numerically solve **nonlinear equations**.

::: example
- Solve $x^2 = 2$ numerically.
- Solve $\sin x = 0.2$ numerically.
- Find the roots of $f(x)$.
:::

# Intermediate value theorem {.split}

::: {.theorem title="Intermediate Value Theorem"}
Let $f$ be a continuous function on $[a, b]$.
If $f(a) f(b) < 0$, then
\begin{align*}
f(x) = 0
\end{align*}
has a solution $x_\star \in [a, b]$.
:::

::: remark
$f(a) f(b) < 0$ is a lazy way of writing that
$f(a)$ and $f(b)$ have different signs.
:::

# The bisection method: animation

~~~ {.yaml .widget name="geogebra"}
url: https://www.geogebra.org/m/krvmfpqv
~~~

# The bisection method [@vaes22, p. 123] {.split}

::: {.problem title="Bisection method"}
Assume that $f: [a, b] \to \R$ satisfies
\begin{align*}
f(a) f(b) < 0.
\end{align*}

Find $x_\star \in [a, b]$ such that $f(x_\star) = 0$.
:::

::: {.algorithm title="Bisection method"}

**Setup**: $[a_0, b_0] \defeq [a, b]$.

**Repeat as often as necessary**

#. Let $x_i \defeq \frac {a_i + b_i} 2$.
#.
\begin{align*}
[a_{i + 1}, b_{i + 1}] \defeq 
\begin{cases}
[a_i, x_i] & \text{if } f(a_i) f(x_i) < 0\\
[x_i, b_i] & \text{otherwise}
\end{cases}
\end{align*}

:::

# The bisection method: invariants [@vaes22, p. 123] {.split}

::: {.remark title="Invariants"}
- $a_i \leq x_i \leq b_i$
- $b_i - a_i = \frac {b - a} {2^i}$
- $f(a_i) < 0 < f(b_i)$.
:::

::: proposition
The sequence $(x_n)_{n \in \N}$ converges to $x_\star \in [a, b]$
with $f(x_\star) = 0$.

Moreover, we have
\begin{align*}
\abs {x_n - x_\star} \leq \frac {b - a} {2^{n + 1}}
\end{align*}
:::

::: corollary
An error of size at most $\epsilon$ can be guaranteed with
\begin{align*}
n \defeq \ceil {\log_2 \frac {b - a} \epsilon}.
\end{align*}
iterations.
:::

# The bisection method: code [@vaes22, p. 124] {.split}

::: example
Use the **bisection method** to approximate $\sqrt 2$ and $\pi$.
:::

~~~ {.julia .jupyter}
function bisection(f, a, b, ϵ = 10^-7)
    while b - a ≥ ϵ
        x = (a + b) / 2
        a, b = f(a) * f(x) ≤ 0 ? [a, x] : [x, b]
    end
    return (a + b) / 2
end

bisection(x -> x^2 - 2, 1, 2) # Approximation √2
bisection(sin, 3, 4) # Approximating π
~~~

# Exercises (recitation) {.split}

::: {.exercise title="Exercise 5.1 p. 138"}
Implement the bisection method to find the solution(s) to the equation
$x = \cos(x)$.
:::

::: {.exercise title="Exercise 5.6 p. 140"}
Calculate
\begin{align*}
x \defeq \sqrt[3] {3 + \sqrt[3] {3 + \sqrt[3]{3 + \dots}}}
\end{align*}
:::

# Evaluating an algorithm {.split}

::: info
We shall be interested in the following questions.

- When does the algorithm converge? Does it converge to the right solution?
- How fast does it converge? (e.g. linear, superlinear, quadratic)
- What if there's a perturbation? Is the algorithm **stable**?
:::

# Convergence speed [@vaes22, pp. 122-123] {.split}

::: question
How fast is convergence?
:::

::: {.definition}
We shall say $(\vec x_k)_{k \in \N}$ converges to $\vec x_\star$

- **linearly** if
  \begin{align*}
  \lim_{k \to +\infty}
  \frac {
  \norm {\vec x_{k + 1} - \vec x_\star}
  } {
  \norm {\vec x_k - \vec x_\star}
  } < 1.
  \end{align*}

- **superlinearly** if
  \begin{align*}
  \lim_{k \to +\infty}
  \frac {
  \norm {\vec x_{k + 1} - \vec x_\star}
  } {
  \norm {\vec x_k - \vec x_\star}
  } = 0.
  \end{align*}

- **quadratically** if
  \begin{align*}
  \lim_{k \to +\infty}
  \frac {
  \norm {\vec x_{k + 1} - \vec x_\star}
  } {
  \norm {\vec x_k - \vec x_\star}^2
  } \in \R.
  \end{align*}
:::

# Convergence speed: examples {.split}

::: example
The sequence $u_n = 2^{-n}$ converges linearly to $0$.
:::

::: proposition
In the bisection method,
$(x_n)_{n \in \N}$ converges linearly to the solution $x_\star$.
:::

# Fixed point iterations [@vaes22, p. 124] {.split}

Assume we want to solve the equation $\vec F(\vec x) = \vec x$.

::: proposition
Let $\vec F: \R^n \to \R^n$ be a continuous function.
If the iteration
\begin{align*}
\vec x_{k + 1} = \vec F(\vec x_k),
\end{align*}
converges to $\vec x_\star$, then $\vec F(\vec x_\star) = \vec x_\star$.
:::

::: {.example title="Splitting methods"}
A splitting $\mat A = \mat M - \mat N$ allows to recast the system
$\mat A \vec x = \vec b$ as a fixed point problem:
\begin{align*}
\vec x = \underbrace{\mat M^{-1} (\mat N \vec x + \vec b)}_{\vec F(\vec x)}
\end{align*}
:::

We will work on a general criterion for convergence and stability.

# Contraction [@vaes22, p. 126] {.split}

::: definition
A function $\vec F: \R^n \to \R^n$ is a **contraction**
if we can find $L < 1$ such that
\begin{align*}
\norm {\vec F(\vec y) - \vec F(\vec x)}
\leq L
\norm {\vec y - \vec x},
\qquad x, y \in \R^n.
\end{align*}
:::

::: example
- $\vec F(\vec x) = L \vec x$, with $L < 1$.
- A differentiable function $f: \R \to \R$ with $\sup \abs{f'} < 1$.
:::

![](https://francetoday.com/wp-content/uploads/2022/03/9639839563806.jpg)

# Banach's fixed point theorem [@vaes22, p. 126] {.split}

\begin{align*}
\text{contraction:} \qquad
\norm {\vec F(\vec y) - \vec F(\vec x)}
\leq L
\norm {\vec y - \vec x},
\qquad L < 1.
\end{align*}

::: {.theorem title="Banach's fixed point theorem"}
Let $\vec F: \R^n \to \R^n$ be a contraction with constant $L < 1$.
The iteration
\begin{align*}
\vec x_{k + 1} \defeq \vec F(\vec x_k)
\end{align*}
converges for each choice of $\vec x_0 \in \R^n$
towards the unique fixed point $\vec x_\star \in \R^n$ of $\vec F$.
Moreover, we have
\begin{align*}
\norm {\vec x_k - \vec x_\star} \leq L^k \norm {\vec x_0 - \vec x_\star}.
\end{align*}
:::

::: {.info title="Cauchy criterion for sequences"}
A sequence $(x_k)_{k \in \N}$ converges if and only if^[
Usually, this criterion is written
\begin{align*}
\forall \epsilon > 0 \quad \exists N > 0 \quad
\forall k, l \in \N : k, l \geq N \quad
\norm {\vec x_k - \vec x_l} \leq \epsilon.
\end{align*}
I hope you don't mind that I didn't write it like that.
]
\begin{align*}
\lim_{k, l \to +\infty} \norm {\vec x_k - \vec x_l} = 0.
\end{align*}
:::

# Convergence speed and stability [@vaes22, p. 126] {.split}

#. The equation
\begin{align*}
\norm {\vec x_{k + 1} - \vec x_\star} &\leq L \norm {\vec x_k - \vec x_\star}\\
\end{align*}
   shows we have **linear convergence**^[
   Confusingly, this type of convergence is sometimes called **exponential**
   or **geometric** because of the second equation.].

#. The equation
\begin{align*}
\norm {\vec x_k - \vec x_\star} &\leq L^k \norm {\vec x_0 - \vec x_\star}.
\end{align*}
   shows a property of strong **stability** called **global exponential stability**:
   should $\vec x_0$ be changed to *any* other value,
   we will still have convergence to $\vec x_\star$,
   with an estimate on that convergence.

# Local stability of a fixed point [@vaes22, p. 127] {.split}

We often already know the solution exists and its approximate location.
In this case, we are interested in whether the iteration converges
with a good initial first guess, and how fast.

::: theorem
Assume that $\vec F(\vec x_\star) = \vec x_\star$ and
that there is $\delta > 0$ and $0 \leq L < 1$ such that
\begin{align*}
\norm {\vec x - \vec x_\star} \leq \delta
\implies
\norm {\vec F(\vec x) - \vec F(\vec x_\star)} \leq L \norm {\vec x - \vec x_\star}.
\end{align*}

All the iterates $\vec x_k$, $k \in \N$ satisfy $\norm {\vec x - \vec x_\star} \leq \delta$
and satisfy
\begin{align*}
\norm {\vec x_k - \vec x_\star} &\leq L^k \norm {\vec x_0 - \vec x_\star}.
\end{align*}
:::

::: remark
The conclusion means that $\vec x_\star$ is a locally **exponentially stable** fixed point.
:::

# Bibliography
