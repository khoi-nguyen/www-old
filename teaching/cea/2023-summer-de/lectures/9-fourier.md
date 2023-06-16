---
title: "Chapter 7: Fast Fourier Transform"
output: revealjs
split: true
notes: |
...

# Motivations

Assume we know that
\begin{align*}
f(t) = \sum_{n = 0}^{+\infty} a_n \sin(n t),
\end{align*}
i.e. $f$ is a **superposition** of signals
with **amplitude** $a_n$
and frequency $n$.

::: question
- Which frequencies contribute to the signal?
- What are the amplitudes?
:::

# Orthogonality

::: {.proposition title="Orthogonality"}
\begin{align*}
\int_0^{2 \pi} \sin (nt) \sin (mt) \dd t
= \begin{cases}
0 & \text{if } m \neq n\\
\pi & \text{if } m = n.
\end{cases}.
\end{align*}
:::

::: info
\begin{align*}
\sin a \sin b = \frac {\cos (a - b) - \cos (a + b)} 2
\end{align*}
:::

# Fourier coefficients

::: proposition
Let $f$ be given by the formula
\begin{align*}
f(t) = \sum_{n = 0}^{+\infty} a_n \sin(n t)
\end{align*}

The coefficients $a_n$ satisfy:
\begin{align*}
a_n = \frac 1 \pi \int_0^{2 \pi} f(t) \sin (n t) \dd t.
\end{align*}
:::

::: {.definition title="Fourier coefficient"}
The integral
\begin{align*}
\frac 1 \pi \int_0^{2 \pi} f(t) \sin (n t) \dd t.
\end{align*}
is called the $n$-th *Fourier coefficient* of $f$.
:::

# Fourier coefficients (general case)

\begin{align*}
f(t) = a_0
+ \sum_{n = 1}^{+\infty} a_n \sin(n t)
+ \sum_{n = 1}^{+\infty} b_n \cos(n t)
\end{align*}

- To find $a_0$, integrate $f$
- To find $a_n$, integrate $f \sin (n t)$
- To find $b_n$, integrate $f \cos (n t)$.

We shall see the theory is much more elegant
with complex numbers

::: exercise
Find the values of $c_n$ in terms of $a_n, b_n$ so that
\begin{align*}
f(t) = \sum_{n \in \Z} c_n e^{i nt}
\end{align*}
:::

# Complex Fourier coefficients

::: proposition
\begin{align*}
f(t) = \sum_{n \in \Z} c_n e^{i 2 \pi n t}
\implies
c_n = \int_0^1 f(t) e^{-i 2 \pi n t} \dd t.
\end{align*}
:::

::: {.definition title="Fourier coefficient"}
\begin{align*}
\widehat f(n) = \int_0^1 f(t) e^{-i 2 \pi n t} \dd t.
\end{align*}
:::

\begin{align*}
f(t) = \sum_{n \in \Z} \widehat f(n) e^{i 2 \pi n t}
\end{align*}

We call the RHS the *Fourier series*.

# Interpretation of complex Fourier coefficients

~~~ {.yaml .widget name="youtube"}
url: https://www.youtube.com/watch?v=QVuU2YCwHjw
zoom: 2
~~~

# Riemann-Lebesgue Lemma

::: proposition
The Fourier coefficients $\widehat f(n)$ tend to $0$
as $n \to +\infty$.
:::

Proof: try for a characteristic function.

::: info
This means that it makes sense to "remove"
high frequency terms.
:::

# Parseval's theorem

::: theorem
Let $f$ be a square-integrable function.
The Fourier series of $f$ converge to $f$
in the mean square norm:
\begin{align*}
\lim_{N \to +\infty}
\int_0^1 \abs{
f(t) - \sum_{n = -N}^N \widehat f(n) e^{i 2 \pi n t}
}^2 \dd t = 0.
\end{align*}
:::

# Discrete Fourier Transform

\begin{align*}
\widehat f(n)
&= \int_0^1 f(t) e^{-i 2 \pi n t} \dd t\\
&\approx \sum_{k = 0}^N \underbrace{f\left( \frac k N \right)}_{y_k}
e^{-i 2 \pi n \frac k N} \frac 1 N
\end{align*}

::: {.definition title="Discrete Fourier Transform"}
\begin{align*}
Y_n \defeq \frac 1 N \sum_{k = 0}^{N - 1} y_k e^{-\frac {i 2 \pi n k} N}.
\end{align*}
:::

# Implementation and complexity

\begin{align*}
Y_n \defeq \frac 1 N \sum_{k = 0}^{N - 1} y_k e^{-\frac {i 2 \pi n k} N}.
\end{align*}

~~~ julia
e(n) = [exp(i * 2 * π * n * k / N) for k in 0:N - 1]
Y(n) = 1 / N * y .* e(-n)
~~~

::: proposition
Computing all the Fourier coefficients: $\bigo(N^2)$.
:::

# Inverse Fourier Transform

::: exercise
Show that
\begin{align*}
y_k = \sum_{n = 0}^{N - 1} Y_n e^{\frac {i 2 \pi n k} N}
\end{align*}
:::
