---
title: "Chapter 3: Modelling with First-Order ODEs"
output: revealjs
kernel: python
notes: |
  24/05: All chapter
...

# Example 1: Bacterial growth

![](/static/images/1684870275.png){width=100%}

# Example 2: Half-Life (unfortunately not the game)

![](/static/images/1684869770.png){width=100%}

# Example 3: Carbon dating

You'd be given that the half-life of $C-14$ is 5730 years.

![](/static/images/1684870324.png)

# Example 4: Cooling of a cake

::::: {.col}
![](/static/images/1684869809.png){width=100%}
:::::

::::: {.col}
\begin{align*}
\frac {\dd T} {\dd t} = k(T - T_m)
\end{align*}
:::::

# Example 5:

::::: {.col}
![](/static/images/1684870462.png)
:::::

::::: {.col}
![](/static/images/1684870503.png)
:::::

# Example 6:

![](/static/images/1684870524.png)
![](/static/images/1684870541.png)

# Example 7: circuits

![](/static/images/1684870575.png)

# Exercises

<pdf-reader src="/static/documents/zill-3.1.pdf" width="100%" height="900" />

# Non-linear models: logistic equation

Assume that an environment is capable of sustaining no more than $K$ individuals.
It follows that in our population model,
\begin{align*}
\frac {\dd P / \dd t} {P} = f(P)
\end{align*}
$f(0) = r$ and $f(K) = 0$. The simplest equation to obey such constraints in a straight line.
\begin{align*}
\frac {\dd P} {\dd t} = P\left(r - \frac r K P\right).
\end{align*}

Equation $\frac {\dd P} {\dd t} = P(a - bP)$ is known as the **logistic equation**.
It is quite accurate in predicting the growth patterns, 
in a limited space, of certain types of bacteria, protozoa, water feas (Daphnia), and 
fruit fies (Drosophila).

To solve them, we use separation of variables.

![](/static/images/1684910530.png)

# Example 1: logistic growth

![](/static/images/1684910565.png)

# Chemical reactions

![](/static/images/1684910846.png)

# Example 2: chemical reactions

![](/static/images/1684910969.png)

# Example 2: part 2

![](/static/images/1684911012.png)

# Exercises

<pdf-reader src="/static/documents/zill-3.2.pdf" width="100%" height="900" />

