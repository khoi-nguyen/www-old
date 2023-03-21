---
title: Solution of nonlinear systems
output: revealjs
...

# Motivations

# The bisection method {.split}

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
