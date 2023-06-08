---
title: "Chapter 7: Laplace transform"
output: revealjs
kernel: python
...

# Introduction

The **Laplace transform** transforms an IVP in an algebraic equation.

![](/static/images/1686174276.png)

::: {.info title="French sentence of the day"}
**Désolé, monsieur le policier, je ne savais pas,
c'est légal dans le Michigan** - *Sorry officer,
I didn't know, it's legal in Michigan*.
:::

# Guys it's on the way!!

Wearing an Ohio State T-shirt was not cool.
Don't worry, I ordered a new one.

![](/static/images/1686217661.png)

# Laplace transform

::: {.definition title="Laplace transform"}
\begin{align*}
\mathscr L f(s) = \int_0^{+\infty} e^{-st} f(t) \dd t
\end{align*}
:::

Notation: $F \defeq \mathscr L f$

# Example: $1$

![](/static/images/1686173616.png)

# Example

![](/static/images/1686173670.png)

# Example

![](/static/images/1686173692.png)

# Linearity

![](/static/images/1686173718.png)
![](/static/images/1686173734.png)

# Transforms of some basic functions

![](/static/images/1686173757.png)

# Transform of a piecewise-continuous functions

![](/static/images/1686173839.png)

# Exercises

<pdf-reader src="/static/documents/zill-7.1.pdf" width="100%" height="900" />

# Inverse Laplace transform

![](/static/images/1686174112.png)

# Example

![](/static/images/1686174137.png)

# Example: Linearity

![](/static/images/1686174165.png)
![](/static/images/1686174178.png)

# Example: partial fractions

![](/static/images/1686174206.png)

# Transform of a derivative

![](/static/images/1686174240.png)
![](/static/images/1686174253.png)

# Solving IVP

![](/static/images/1686174304.png)
![](/static/images/1686174321.png)

# Solving a second-order IVP

![](/static/images/1686174344.png)

# Exercises

<pdf-reader src="/static/documents/zill-7.2.pdf" width="100%" height="900" />

# $s$-translation property

::: {.theorem title="s-translations"}
\begin{align*}
\mathscr L \{ e^{at} f(t) \} = F(s - a)
\end{align*}
:::

![](/static/images/1686260394.png)

# $s$-translations and inverse Laplace transform

![](/static/images/1686260437.png)

# An IVP

Outline only

![](/static/images/1686260636.png)

# Second IVP

![](/static/images/1686260617.png)


# Heaviside function

On-off function.

::: {.definition title="Heaviside function"}
\begin{align*}
\mathscr U(t) = \begin{cases}
0 & t < 0\\
1 & t \geq 0
\end{cases}
\end{align*}
:::

\begin{align*}
f(t) = \begin{cases}
g(t) & t < a\\
h(t) & t \geq a
\end{cases}
\implies
f(t) =
g(t) (1 - \mathscr U(t - a)) + h(t) \mathscr(t - a)
\end{align*}

\begin{align*}
f(t) = \begin{cases}
0 & t < a\\
g(t) & a \leq t < b\\
0 & t \geq b
\end{cases}
\implies
f(t) = g(t) \left( \mathscr U(t -a ) - \mathscr U(t - b) \right)
\end{align*}

# Example: step functions

![](/static/images/1686262493.png)

# $t$-translations

::: theorem
Let $a > 0$.

\begin{align*}
\mathscr L \{f(t - a) \mathscr U(t - a)\}
= e^{-as} F(s).
\end{align*}
:::

# Example

![](/static/images/1686263213.png)
![](/static/images/1686263230.png)

# Inverse Laplace

![](/static/images/1686263260.png)

# Alternative form

\begin{align*}
\mathscr L \{f(t) \mathscr U(t - a)\}
= e^{-as} \mathscr L \{f(t + a)\}
\end{align*}

![](/static/images/1686263376.png)

# IVP

![](/static/images/1686263406.png)

# Exercises

<pdf-reader src="/static/documents/zill-7.3.pdf" width="100%" height="900" />

# Multiplication by $t^n$

![](/static/images/1686264179.png)

# Example

![](/static/images/1686264256.png)
![](/static/images/1686264266.png)

# Transform of a periodic function

![](/static/images/1686264338.png)

# Example

![](/static/images/1686264354.png)

# Exercises

<pdf-reader src="/static/documents/zill-7.4.pdf" width="100%" height="900" />

# Unit impulse

![](/static/images/1686264503.png)
![](/static/images/1686264537.png)

# Dirac $\delta$ "function"

\begin{align*}
\delta(t - t_0) = \lim_{a \to 0} \delta_a(t - t_0)
\end{align*}

It is actually a "distribution", not a function.

![](/static/images/1686264698.png)

# Example

![](/static/images/1686264803.png)
![](/static/images/1686264817.png)

# Exercises

<pdf-reader src="/static/documents/zill-7.5.pdf" width="100%" height="900" />
