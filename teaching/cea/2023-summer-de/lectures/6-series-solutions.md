---
title: "Chapter 6: Series solutions"
output: revealjs
kernel: python
...

# Power series: review

Power series **centered at $a$**.
\begin{align*}
\sum_{n = 0}^{+\infty} c_n (x - a)^n
= c_0 + c_1(x - a) + c_2(x - a^2 + \dots
\end{align*}

Such a power series **converges** if the following limit exists
\begin{align*}
\lim_{n \to +\infty} \sum_{n = 0}^N c_n (x - a)^n.
\end{align*}

It converges **absolutely** if
\begin{align*}
\lim_{n \to +\infty} \sum_{n = 0}^N \abs{c_n (x - a)^n}.
\end{align*}

::: remark
Absolute convergence is necessary to talk about operations on series.
:::

# Radius and interval of convergence

\begin{align*}
\sum_{n = 0}^{+\infty} c_n (x - a)^n
= c_0 + c_1(x - a) + c_2(x - a^2 + \dots
\end{align*}

- The **interval of convergence** is symmetric,
  and has the form $[a - R, a + R]$.
\begin{align*}
[a - R, a + R], (a - R, a + R], [a - R, a + R), (a - R, a + R)
\end{align*}
  $R$ is called the **radius of convergence**.
  Remark

![](/static/images/1685946379.png)

# Convergence

::: proposition
The series
\begin{align*}
\sum_{n = 0}^{+\infty} c_n (x - a)^n
= c_0 + c_1(x - a) + c_2(x - a^2 + \dots
\end{align*}
converges if
\begin{align*}
\lim_{n \to +\infty} \abs{x - a} \abs{\frac {c_{n + 1}} {c_n}} < 1.
\end{align*}
:::

# Example: interval of convergence

![](/static/images/1685947101.png)

# Functions as power series

- A power series defines a function
\begin{align*}
f(x) \defeq \sum_{n = 0}^{+\infty} c_n(x - a)^n
\end{align*}
- Functions that have power series are called **analytic**.
- Identity property
\begin{align*}
\sum_{n = 0}^{+\infty} c_n (x - a)^n = 0
\text{ for } x \in (a - R, a + R)
\implies c_n = 0
\end{align*}
- Power series are the **Taylor series** of the function
\begin{align*}
f(x) \defeq \sum_{n = 0}^{+\infty} \frac {f^{(n)}(a)} {n!}(x - a)^n
\end{align*}

# Differentiation and integration

\begin{align*}
y = \sum_{n = 0}^{+\infty} c_n(x - a)^n
\end{align*}

Differentiation and integration can be performed term by term

\begin{align*}
y' = \sum_{n = 1}^{+\infty} c_n n (x - a)^{n - 1}\\
\int y \dd x = \sum_{n = 0}^{+\infty} \frac {c_n} {n + 1} (x - a)^{n + 1}
\end{align*}

The convergence radius is the same (check using the ratio test)
but we may lose convergence when differentiation or gain convergence
when integrating at endpoints.

# Some Taylor series

![](/static/images/1685950472.png)

# Example: multiplication of power series

![](/static/images/1685950524.png)

# Example: addition of power series

![](/static/images/1685950634.png)
![](/static/images/1685950653.png)

# Example: power series solution

![](/static/images/1685950738.png)

# Exercises

<pdf-reader src="/static/documents/zill-6.1.pdf" width="100%" height="900" />

# Ordinary and singular points

\begin{align*}
y'' + P(x) y' + Q(x) y = 0.
\end{align*}

- **ordinary point**: $P$ and $Q$ are **analytic** at that point
- **singular point**: not ordinary

# Example: ordinary point

![](/static/images/1685951446.png)

# Singular points

![](/static/images/1685951466.png)

# Polynomial coefficients and division

![](/static/images/1685951501.png)

# Existence of power series solution

::: theorem
Assume $x_0$ is an **ordinary point** of
a_2(x) y'' + a_1(x) y' + a_0(x) y = 0.
We can find two linearly independent solutions
expressed as power series whose convergence radius
is greater than the distance from $x_0$ to the closest singular point.
:::

# Example: minimum radius of convergence

![](/static/images/1685951931.png)
![](/static/images/1685951941.png)

# Example: Power Series solution

![](/static/images/1685952258.png){width=100%}

# Example 6: Power series solution

![](/static/images/1685952518.png)

# Example 7: three-term recurrence relation

![](/static/images/1685952902.png)
![](/static/images/1685952922.png)

# Example 8: DE with nonpolynomial coefficient

![](/static/images/1685953290.png)

# Exercises

<pdf-reader src="/static/documents/zill-6.2.pdf" width="100%" height="900" />
