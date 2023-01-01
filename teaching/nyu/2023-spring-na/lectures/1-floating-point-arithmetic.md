---
title: "Chapter 1: Floating Point Arithmetic"
output: revealjs
notes: |
  - [<i class="fa-solid fa-file-pdf"></i> Lecture notes](/static/numerical-analysis/1-roundoff.pdf)
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

<pdf-reader src="/static/numerical-analysis/1-roundoff.pdf">

# Motivations {.row}

::: col
::: question
Can you explain this?

~~~ julia
julia> 0.1 * 0.1
0.010000000000000002
~~~
:::

::: {.solution .fragment collapse=0}
A bit like $\frac 1 3$ in base $10$,
$\frac 1 {10}$ does not have a finite **binary representation**.

The computer rounds it off,
which leads to error propagation.
:::
:::

::: col
::: {.question .fragment}
What about this?

~~~ julia
julia> 10^19
-8446744073709551616
~~~
:::

::: {.solution .fragment}
This is called **integer overflow**.
:::
:::

::: col
::: {.question .fragment}
Why do we have different results when we change the summation order?

~~~ julia
julia> sum(1/n for n in 1:10000)
9.787606036044348

julia> sum(1/n for n in 10000:-1:1)
9.787606036044386
~~~
:::
:::

# Binary representation of real numbers [@vaes22, p. 5] {.split}

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

::: fragment
$\beta = 2$
:   **binary**, $a_k$ is called **bit**

$\beta = 10$
:   **decimal** (default base), $a_k$ is called digit

$\beta = 16$
:   **hexadecimal** (default),
    $\{a_k\} \subset \{1, 2, \dots, 9, A, B, \dots F\}$.
:::

::: {.remark .fragment}

$$\beta = (10)_\beta$$

:::

# Binary arithmetic {.split}

- The classical algorithms that you learned in primary school
  work with minor adaptations in base $2$.
- Multiplying by *powers of 2* is easy because $2 = (10)_2$

::: {.example .fragment}
Let $x = (110)_2$ and $y = (101)_2$.

- Calculate $x + y$ in base $2$.
- Calculate $x \times y$ in base $2$.
:::

# Binary to decimal [@vaes22, p. 6]

::: example
Convert $(0.\overline{10})_2$ to decimal notation.
:::

# Decimal to binary [@vaes22, p. 6] {.split}

Converting to binary is more
because negative powers of $10$ have
*infinite* binary representations.

::: {.algorithm .fragment}
~~~ julia
function to_binary(x, n)
  bits = zeros(Bool, n)
  for i in 1:n
    x *= 2
    bits[i] = x ≥ 1
    x -= bits[i]
  end
  bits
end
~~~
:::

::: {.exercise .fragment}
Adapt the algorithm so that it works for integers.
:::

# Floating point formats [@vaes22, p. 7]

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

::: {.split .fragment}
An element such as
$$(-1)^s 2^{E_\min} (0\cdot b_1 b_2 \dots b_{p - 1})_2$$
is called **subnormal** or **denormalized**.
:::

# Floating points formats [@vaes22, p. 7] {.split}

::: {.block title="Most widely used formats"}
`Float16`
:   $\F(11, -14, 15)$, called *half-precision*

`Float32`
:   $\F(24, -126, 127)$, called *single precision*

`Float64`
:   $\F(53, -1022, 1023)$, called *double precision*
:::

::: {.question .fragment}

Why is $\F(11, -14, 15)$ called `Float16`?

:::

::: {.solution .fragment collapse=0}

- $1$ bit is used to store the sign
- $5$ bits are used to represent the exponent
  $$2^5 = 32 > 29$$
- $10$ bits are used for the mantissa

For more info, see [@vaes22, Section 1.4 pp. 13-15].

:::

# Floating point formats in Julia {.row}

::: col
~~~ {.julia .fragment}
Float64(0.1)

Float64(0.1) == Float32(0.1) # false

bitstring(0.1)
bitstring(Float32(0.1))
~~~
:::

::: col
~~~ {.julia .fragment}
julia> bitstring(0.1)
"0011111110111001100110011001100110011001100110011001100110011010"
~~~
:::

# Machine $\epsilon$ {.split}

::: {.definition title="Machine epsilon"}
Let $\F = \F(p, E_\min, E_\max)$.
We define the *machine $\epsilon$* associated with $\F$ via

$$\epsilon_{\F} \defeq 2^{-p + 1}$$

:::

::: {.proposition .fragment}
Let $\F = \F(p, E_\min, E_\max)$.
We have

$$1 + \epsilon_\F = \min \{x \in \F : x > 1\}.$$

~~~ {.tex .tikz}
\draw (-1.75, 0) -- (4.5, 0);
\draw[to-to] (0, 0.3) -- node[above] {$\varepsilon_{\mathbb F}$} (1, 0.3);
\fill (0, 0) circle (0.05) node[below] {$1$};
\foreach \x in {1, 2, 3, 4} \fill (\x, 0) circle (0.05);
\foreach \x in {-0.5, -1, -1.5} \fill (\x, 0) circle (0.05);
~~~
:::

::: {.fragment .remark}
In Julia, the machine $\epsilon$ can be calculated via the `eps` function.

Format           Machine $\epsilon$
-------          ------------------
`Float16`        `np.finfo(np.float16).eps`{.sympy}
`Float32`        `np.finfo(np.float32).eps`{.sympy}
`Float64`        `np.finfo(np.float64).eps`{.sympy}

:::

# Machine $\epsilon$ [@vaes22, p.8] {.row}

::: col

~~~ {.julia .plot}
p = -4:0.01:4
x = 2.0.^p
y = @. nextfloat(x) - x
plot(x, y, label=L"\Delta(x)")
title!("Distance to the successor")
xticks!(floor.(2.0.^(0:4)))
xlabel!(L"x")
yticks!(
  2.0.^(0:4).*eps(Float64),
  [latexstring(string(2^i) * "\\epsilon_{\\mathbb{F}}") for i in 0:4]
)
~~~

::: {.proposition .fragment}
Let $x_-, x_+ \in \F$ be two consecutive non-denormalized numbers.
We have

$$x_+ - x_- = 2^{\lfloor\log_2 x_-\rfloor} \epsilon_\F$$
:::

:::

::: col

~~~ {.julia .plot .fragment}
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

::: {.fragment}
In particular, the relative distance satisfies:
$$\frac {x_+ - x_-} {|x_-|} = \frac {2^{\lfloor\log_2 x_-\rfloor}} {|x_-|} \epsilon_\F$$
:::

:::

# Relative distance to the next float [@vaes22, pp. 9-10]

~~~ {.julia .plot}
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

::: {.proposition .fragment}
Let $x_\min, x_\max \in \F_{>0}$ be
the smallest and largest denormalized numbers in $\F$.
If $x \in \R$ satisfies $x_\min \leq |x| \leq x_\max$, then
$$\min_{\widehat x \in \F} \left|\frac {x - \widehat x} x\right| \leq \frac 1 2 \epsilon_M.$$
:::

# Relative distance to the next float with denormalized numbers [@vaes22, p. 10]

~~~ {.julia .plot}
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

# Round to nearest [@vaes22, p. 10] {.split}

Assume $x \notin \F$ is positive.

::: {.exampleblock title="Round to nearest" .fragment}
- **Standard case**
    the number $x$ is rounded to the nearest representable number
    if this number is unique.

- **Edge case**
    Rule in favour of the one with least significant bit equal to $0$.

- **Infinities**

    - If $x_\max \leq x < 2^{E_\max} (2 - 2^{-p - 1})$, return $x_\max$
    - Otherwise, the special value `Inf` is delivered.
:::

::: fragment
This define an operation $\fl_\F : \R \to \F$.
:::

# Operation on floating numbers [@vaes22, p. 11]

Let $\F, \F'$, with $\F'' = \F \cup \F'$.

::: fragment
If $\circ : \R \times \R \to \R$,
we can naturally define an operation

$$\hat \circ : \F \times \F' \to \F'' : (x, y) \mapsto \fl_{\F''}(x \circ y).$$

e.g. $\widehat +$, $\widehat -$, $\widehat \times$, $\widehat \div$
:::

::: fragment
These operations **aren't associative**.

$$x \widehat + (y \widehat + z) \neq (x \widehat + y) \widehat + z$$
:::

# Non-associativity [@vaes22, p. 12] {.split}

::: question
When we have three or more terms,
what order should we add them in
if we want our answer to be as accurate as possible?
:::

::: {.example .fragment}
$$x = 1 \quad y = 3 \times 2^{-13} \quad z = 3 \times 2^{-13}$$

Show that $(x \widehat + y) \widehat + z \neq x \widehat + (y \widehat + z)$.
:::

# Bibliography
