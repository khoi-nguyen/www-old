---
title: "Session 1: Introduction to Julia"
output: revealjs
...

# Installing Julia

::: task
- Install [**Visual Studio Code**](https://code.visualstudio.com/download)
- Install the *Jupyter* and *Julia* extensions
:::

# Learn X in Y minutes

<iframe src="https://learnxinyminutes.com/docs/julia/" width="100%" height="900">

# Help and documentation {.row}

::: col

#### Getting help

Type `?`{.julia} to access help mode,
followed by the name of the function.

::: task
Read the help pages for `if`{.julia}, `while`{.julia}, and `for`{.julia}.
:::
:::

::: col

#### Installing a package

Type `]`{.julia} to enter the package REPL,
followed by `add PackageName`{.julia}.

~~~ julia
import Plots
Plots.plot(cos)

# Alternatively, though not recommended
using Plots
plot(cos)
~~~

:::

# Exercise {.row}

::: col
::: task
Euler showed that

$$\lim_{N \to \infty}\left(
-\ln N + \sum_{n = 1}^N \frac 1 n
\right) = \gamma.$$

Write a function
that returns an approximation of the Euler-Mascheroni constant $\gamma$
by evaluating the expression between brackets at a finite value of $N$.

~~~ julia
function euler_constant(N)
    # Your code comes here
end
~~~
:::

::: question
Does the summation order matter?
If so, how can we improve accuracy?
:::
:::

::: col
::: solution
~~~ julia
euler_constant(N) = -log(N) + sum(1 / n for n in 1:N)

# Better accuracy
euler_constant(N) = -log(N) + sum(1 / n for n in N:-1:1)

# With a for loop
function euler_constant(N)
    result = 0
    for n in N:-1:1
      result += 1 / n
    end
    -log(N) + result
end
~~~
:::
:::
