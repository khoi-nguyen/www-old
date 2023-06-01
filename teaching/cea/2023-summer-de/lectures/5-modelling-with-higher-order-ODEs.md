---
title: "Chapter 5: Modelling with Higher-Order ODEs"
output: revealjs
kernel: python
...

# Hooke's law

![](/static/images/1685657021.png)

\begin{align*}
F = k s
\implies
m \frac {\dd^2 x} {\dd t^2} = -k(x + s) + mg = -kx
\end{align*}

::: {.info title="Simple harmonic or free undamped motion"}
\begin{align*}
\frac {\dd^2 x} {\dd t^2} + \omega^2 x = 0
\quad \omega = \sqrt {k / m}.
\end{align*}
:::

# Free undamped motion

\begin{align*}
\frac {\dd^2 x} {\dd t^2} + \omega^2 x = 0
\quad \omega = \sqrt {k / m}.
\end{align*}

\begin{align*}
x(t) = c_1 \cos \omega t + c_2 \sin \omega t = A \sin (\omega t + \phi)
\end{align*}

Quantity                      Formula
---------                     --------
Circular frequency            $\omega = \sqrt{k/m}$
Period                        $T = 2 \pi / \omega$
Frequency                     $f = 1/T$
Amplitude                     $A = \sqrt{c_1^2 + c_2^2}$
Phase angle                   $\tan \phi = c_1 / c_2$

# Example: free undamped motion

![](/static/images/1685657639.png)
![](/static/images/1685657653.png)

# Double spring systems

::::: {.col}
![](/static/images/1685657793.png)
:::::

::::: {.col}
**Parallel springs**: same displacement, forces add up
\begin{align*}
k_{eff} = k_1 + k_2
\end{align*}

**Springs in series**: forces are the same, displacement add up:
\begin{align*}
-k_{eff}(x_1 + x_2) = -k_1 x_1 = -k_2 x_2
\end{align*}
:::::

# Free damped motion

![](/static/images/1685658107.png)

\begin{align*}
m \frac {\dd^2 x} {\dd t^2} = -k x - \beta \frac {\dd x} {\dd t}
\end{align*}

\begin{align*}
\frac {\dd^2 x} {\dd t^2} + 2 \lambda \frac {\dd x} {\dd t} + \omega^2 x = 0.
\end{align*}

# Free damped motions (3 cases)

![](/static/images/1685658201.png){width=100%}
![](/static/images/1685658228.png){width=100%}

# Overdamped motion

![](/static/images/1685658383.png){width=100%}

# Critically damped motion

![](/static/images/1685658446.png){width=100%}
![](/static/images/1685658465.png){width=100%}

# Underdamped motion

![](/static/images/1685658509.png)

# Driven motion

\begin{align*}
m \frac {\dd^2 x} {\dd t^2} = -k x - \beta \frac {\dd x} {\dd t} + f(t)
\end{align*}

\begin{align*}
\frac {\dd^2 x} {\dd t^2} + 2 \lambda \frac {\dd x} {\dd t} + \omega^2 x = F(t).
\end{align*}

# Interpretation of an initial-value problem

![](/static/images/1685658969.png)

# Transient/steady-state solutions

![](/static/images/1685659056.png){width=100%}

# Series circuit analogue

\begin{align*}
m \frac {\dd^2 x} {\dd t^2} + \beta \frac {\dd x} {\dd t} + kx = f(t)
\end{align*}

\begin{align*}
L \frac {\dd^2 q} {\dd t^2} + R \frac {\dd q} {\dd t} + \frac 1 C x = E(t)
\end{align*}

![](/static/images/1685659237.png)

# Example: underdamped series circuit

![](/static/images/1685659324.png)

# Exercises

<pdf-reader src="/static/documents/zill-5.1.pdf" width="100%" height="900" />
