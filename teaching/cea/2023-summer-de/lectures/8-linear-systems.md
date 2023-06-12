---
title: "Chapter 8: Linear systems"
output: revealjs
...

# Linear systems

![](/static/images/1686521709.png)

# Matrix form

![](/static/images/1686521742.png)

# Example

![](/static/images/1686521764.png)

# Verification of solution

![](/static/images/1686521795.png)

# IVP and solution

![](/static/images/1686522172.png)

# Homogeneous systems

![](/static/images/1686522199.png)

# Superposition principle

![](/static/images/1686522222.png)

# Linear independence

![](/static/images/1686522366.png)
![](/static/images/1686522379.png)

# Linear independence: solution

![](/static/images/1686523770.png)

# General solution: homogeneous system

![](/static/images/1686523800.png)
![](/static/images/1686523811.png)

# General solution

![](/static/images/1686523852.png)

# General system: nonhomogenous

![](/static/images/1686523903.png)
![](/static/images/1686523917.png)

# Exercises

<pdf-reader src="/static/documents/zill-8.1.pdf" width="100%" height="900" />

# Homogeneous linear systems and eigenvalues

Let's try to solve $\mat X' = \mat A \mat X$.

Let's try a solution of the form
\begin{align*}
\mat X = \mat K e^{\lambda t}
\end{align*}

::: proposition
\begin{align*}
\mat X' = \mat A \mat X
\iff (\mat A - \lambda \mat I) \mat K = 0.
\end{align*}
:::

We call $\lambda$ an **eigenvalue**
and $\mat K$ an **eigenvector**.

# Distinct eigenvalues

![](/static/images/1686526847.png)

# Distinct eigenvalues: example

![](/static/images/1686526866.png)
![](/static/images/1686526877.png)

# Distinct eigenvalues

![](/static/images/1686549904.png)

# Repeated eigenvalues

![](/static/images/1686550152.png)

# Repeated eigenvalues: first example

![](/static/images/1686550182.png)

# Second solution

![](/static/images/1686550217.png)

# Second example

![](/static/images/1686550250.png)
![](/static/images/1686550270.png)

# Eigenvalues of multiplicity 3

![](/static/images/1686550297.png)

# Repeated eigenvalues

![](/static/images/1686550324.png)

# Complex eigenvalues

![](/static/images/1686550360.png)

# Complex eigenvalues

![](/static/images/1686550485.png)

# Complex eigenvalues example

![](/static/images/1686550520.png)

# Exercises

<pdf-reader src="/static/documents/zill-8.2.pdf" width="100%" height="900" />