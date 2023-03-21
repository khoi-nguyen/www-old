---
title: Solution of nonlinear systems
output: revealjs
...

# Motivations {.split}

::: example
- Solve $x^2 = 2$.
- Solve $\sin x = 0.2$
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

# The bisection method {.split}

::: {.problem title="Bisection method"}
Assume that
\begin{align*}
f(a) < 0 < f(b).
\end{align*}

Find $x_\star$ such that $f(x_\star) = 0$.
:::

::: {.algorithm title="Bisection method"}

**Setup**.

$a_0 \defeq a$, $b_0 \defeq b$

**Repeat as often as necessary**

#. Let $x_i \defeq \frac {a_i + b_i} 2$.
#.
\begin{align*}
f(x_i) &< 0 \implies
\qquad
a_{i + 1} \defeq x_i
\quad
b_{i + 1} \defeq b_i\\
f(x_i) &> 0 \implies
\qquad
a_{i + 1} \defeq a_i
\quad
b_{i + 1} \defeq x\\
f(x_i) &= 0 \implies
\qquad \text{stop}
\end{align*}

:::

# The bisection method: invariants {.split}

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
\abs {x_n - x_\star} \leq \frac {b - a} {2^n}
\end{align*}
:::

::: corollary
An error of size at most $\epsilon$ can be guaranteed with
\begin{align*}
n \defeq \ceil {\log_2 \frac {b - a} \epsilon}.
\end{align*}
iterations.
:::

# The bisection method: code {.split}

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
