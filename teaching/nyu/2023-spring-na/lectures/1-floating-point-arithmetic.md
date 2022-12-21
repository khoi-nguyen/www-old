---
title: "Chapter 1: Floating Point Arithmetic"
output: revealjs
notes: |
  - [Lecture notes](https://urbain.vaes.uk/static/teaching/numerical_analysis_fall/build/roundoff.pdf)
...

# Welcome

<table class="table table-bordered table-striped container text-center">
<tr>
<th>Type</th>
<th>Day</th>
<th>Time</th>
</tr>
<tr>
<th rowspan="2" class="align-middle">Lectures</th>
<td>Monday</td>
<td rowspan="2" class="align-middle">16:45-18:00</td>
</tr>
<tr>
<td>Wednesday</td>
</tr>
<tr>
<th rowspan="2" class="align-middle">Recitations</th>
<td>Monday</td>
<td rowspan="2" class="align-middle">18:05-18:50</td>
</tr>
<tr>
<td>Wednesday</td>
</tr>
</table>

- Slides: <https://nguyen.me.uk/teaching/nyu/2023-spring-na/>
- Lecture notes: <https://urbain.vaes.uk/teaching/2022-fall-na/>
- Nguyen: A thi**ng we in**tend to do...

# Prerequisites

- Linear Algebra
- Real Analysis
- (Desirable) Some familiarity with a programming language,
  ideally `python` or `julia`.

# Lecture notes

~~~ {.yaml .widget name="pdf"}
url: https://urbain.vaes.uk/static/teaching/numerical_analysis_fall/build/main.pdf
~~~

# Motivations {.row}

::: col
::: question
Can you explain this?

~~~ julia
julia> 0.1 * 0.1
0.010000000000000002
~~~
:::

::: question
What about this?

~~~ julia
julia> 10^19
-8446744073709551616
~~~
:::
:::

::: col
::: question
Why do we have different results when we change the summation order?

~~~ julia
julia> sum(1/n for n in 1:10000)
9.787606036044348

julia> sum(1/n for n in 10000:-1:1)
9.787606036044386
~~~
:::
:::

# Binary representation of real numbers (p. 14) {.split}

::: {.definition title="Positional notation"}
Let $x \in \R$ and $\beta \in \N_0$.
We call
$$\pm (a_{-n} a_{-n + 1} \dots a_{-1} a_0 \cdot a_1 a_2 \dots)_\beta$$
its **representation in base $\beta$**
if
\begin{align}
  x = \pm \sum_{k = -n}^{+\infty} a_k \beta^{-k},
  \quad a_k \in \{0, \dots, \beta - 1\}
\end{align}
:::

$\beta = 2$
:   **binary**, $a_k$ is called **bit**

$\beta = 10$
:   **decimal** (default base), $a_k$ is called digit

$\beta = 16$
:   **hexadecimal** (default),
    $\{a_k\} \subset \{1, 2, \dots, 9, A, B, \dots F\}$.

::: remark
$$\beta = (10)_\beta$$
:::

# Binary arithmetic {.split}

- The classical algorithms that you learned in primary school
  work with minor adaptations in base $2$.
- Multiplying by *powers of 2* is easy because $2 = (10)_2$

::: example
Let $x = (110)_2$ and $y = (101)_2$.

- Calculate $x + y$ in base $2$.
- Calculate $x \times y$ in base $2$.
:::

# Binary to decimal

::: example
Convert $(0.\overline{10})_2$ to decimal notation.
:::

# Decimal to binary {.split}

Converting to binary is more
because negative powers of $10$ have
*infinite* binary representations.

::: algorithm
~~~ julia
function to_binary(x, error = 0)
  if (x < 0 || x > 1)
    throw(DomainError(x, "x should be between 0 and 1"))
  end
  bits = []
  while x ≥ error:
    x *= 2
    bit = Int(x ≥ 1)
    x -= bit
  bits
end
~~~
:::

::: exercise
Adapt the algorithm so that it works for integers.
:::

# Floating point formats

::: {.definition title="Floating point format"}
\begin{align}
  \F(p, E_\min, E_\max) = \left\{
    ((-1)^s 2^E (b_0. b_1 \dots b_{p - 1})_2:
    s \in \{0, 1\},
    b_i \in \{0, 1\},
    E_\min \leq E \leq E_\max
  \right\}
\end{align}
:::

::: split
An element such as
$$(-1)^s 2^{E_\min} (0\cdot b_1 b_2 \dots b_{p - 1})_2$$
is called **subnormal** or **denormalized**.

`Float16`
:   $\F(11, -14, 15)$, called *half-precision*

`Float32`
:   $\F(-14, -126, 127)$, called *single precision*

`Float64`
:   $\F(53, -1022, 1023)$, called *double precision*

~~~ julia
Float64(0.1)

Float64(0.1) == Float32(0.1) # false
~~~

~~~ python
# In Python
import numpy as np

np.Float32(0.1)
~~~
:::

# Machine $\epsilon$ {.split}

[@vaes22, p. 9]

Let $x \in \F(p, E_\min, E_\max)$ be positive and **non-denormalized**, i.e.
$$x = 2^n (1. b_1 \dots b_{p - 1})_2.$$
If $\Delta : \F \to \R$ associates with $x \in \F$
its distance to its successor, then
$$\Delta(x) = 2^{n - p + 1}$$

::: {.definition title="Machine epsilon"}
$$\epsilon_M \defeq 2^{-p + 1}$$
:::

::: proposition
Let $\Delta : \F \to \R$ be the function which associates
with $x$ its distance to its *successor*.
The inequality
$$\frac {\epsilon_M} 2 \leq \frac {\Delta(x)} {|x|} \leq \epsilon_M$$
holds for every non-denormalized $x \in \F \setminus \{0\}$.
:::

In Julia, $\epsilon_M$ can be calculated via the `eps` function,
e.g. `eps(Float64)`{.julia},
which yields `np.finfo(float).eps`{.sympy}.

# Density

In Julia, the fonction `nextfloat` gives the next representable number.

::: row
::: col
~~~ {.plot .julia}
p = -4:0.01:4
x = 2.0.^p
y = @. nextfloat(x) - x
plot(x, y, label=L"\Delta(x)")
title!("Distance to the next float")
xticks!(floor.(2.0.^(0:4)))
xlabel!(L"x")
yticks!(
  2.0.^(0:4).*eps(Float64),
  [latexstring(string(2^i) * "\\epsilon_M") for i in 0:4]
)
~~~
:::
::: col
~~~ {.plot .julia}
p = -4:0.01:4
x = 2.0.^p
y = @. (nextfloat(x) - x) / x
plot(x, y, label=L"\frac{\Delta(x)}{x}")
title!("Relative distance to the next float")
xticks!(floor.(2.0.^(0:4)))
xlabel!(L"x")
yticks!(
  eps(Float64).*(0.5:0.5:1),
  [latexstring(string(i) * "\\epsilon_M") for i in 0.5:0.5:1]
)
~~~
:::
:::

# Relative distance to the next float

~~~ {.plot .julia}
p = -4:0.01:4
x = 2.0.^p
y = @. (nextfloat(x) - x) / x
plot(x, y, label=L"\frac{\Delta(x)}{x}", xaxis=:log)
title!("Relative distance to the next float (semi-logarithmic)")
xticks!(
  2.0.^(-4:4),
  [latexstring("2^{" * string(i) * "}") for i in -4:4]
)
xlabel!(L"x")
yticks!(
  eps(Float64).*(0.5:0.5:1),
  [latexstring(string(i) * "\\epsilon_M") for i in 0.5:0.5:1]
)
~~~

# Relative distance to the next float with denormalized numbers

~~~ {.plot .julia}
p = -1024:0.01:-1016
x = 2.0.^p
y = @. (nextfloat(x) - x) / x
plot(x, y, label=L"\frac{\Delta(x)}{x}", xaxis=:log)
title!("Relative distance to the next float (semi-logarithmic)")
xticks!(
  2.0.^(-1024:-1016),
  [latexstring("2^{" * string(i) * "}") for i in -1024:-1016]
)
xlabel!(L"x")
yticks!(
  eps(Float64).*(0.5:0.5:4),
  [latexstring(string(i) * "\\epsilon_M") for i in 0.5:0.5:4]
)
~~~

# Round to nearest {.split}

Assume $x \notin \F$ is positive.

::: {.exampleblock title="Round to nearest"}
- **Standard case**
    the number $x$ is rounded to the nearest representable number
    if this number is unique.

- **Edge case**
    Rule in favour of the one with least significant bit equal to $0$.

- **Infinities**

    - If $x_\max \leq x < 2^{E_\max} (2 - 2^{-p - 1})$, return $x_\max$
    - Otherwise, the special value `Inf` is delivered.
:::

This define an operation $\fl_\F : \R \to \F$.

# Operation on floating numbers

Let $\F, \F'$, with $\F'' = \F \cup \F'$.

If $\circ : \R \times \R \to \R$,
we can naturally define an operation

$$\hat \circ : \F \times \F' \to \F'' : (x, y) \mapsto \fl_{\F''}(x \circ y).$$

e.g. $\widehat +$, $\widehat -$, $\widehat \times$, $\widehat \div$

These operations **aren't associative**.

$$x \widehat + (y \widehat + z) \neq (x \widehat + y) \widehat + z$$

# Non-associativity {.split}

::: question
When we have three or more terms,
what order should we add them in
if we want our answer to be as accurate as possible?
:::

::: example
$$x = 1 \quad y = 3 \times 2^{-13} \quad z = 3 \times 2^{-13}$$

Show that $(x \widehat + y) \widehat + z \neq x \widehat + (y \widehat + z)$.
:::

# Bibliography
