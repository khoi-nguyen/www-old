---
title: "Chapter 5: Solution of nonlinear systems"
output: revealjs
notes: |
  - 22/03: Bisection method, convergence speed, Banach fixed point (1-16)
  - 29/03: Local Banach fixed point, condition on the derivative, chord method (17-30)
  - 03/04: Newton-Raphson, secant method (31-end)
...

# Starter

::::: {.col}

#### Plan for today

- Bisection method
- Linear, superlinear and quadratic convergence
- Banach fixed point theorem

:::::

::::: {.col}

#### Announcements

- Homework on relaxation method due on Monday 27
- French sentence of the day: "*J'invoque le 49.3*" with examples:

  - Donne-moi 100 euros, ou j'invoque le 49.3

![](/static/images/1679489658.png)
![](/static/images/1679491858.png)
![](/static/images/1679491880.png)


:::::

# Motivations {.split}

We shall attempt to numerically solve **nonlinear equations**.

::: example
- Solve $x^2 = 2$ numerically.
- Solve $\sin x = 0.2$ numerically.
- Find the roots of $f(x)$.
:::

# Intermediate value theorem {.split}

::: {.theorem title="Intermediate Value Theorem"}
Let $f$ be a continuous function on $[a, b]$.
If $f(a) f(b) < 0$, then
\begin{align*}
f(x) = 0
\end{align*}
has a solution $x_\star \in [a, b]$.
:::

::: remark
$f(a) f(b) < 0$ is a lazy way of writing that
$f(a)$ and $f(b)$ have different signs.
:::

# The bisection method: animation

~~~ {.yaml .widget name="geogebra"}
url: https://www.geogebra.org/m/krvmfpqv
~~~

# The bisection method [@vaes22, p. 123] {.split}

::: {.problem title="Bisection method"}
Assume that $f: [a, b] \to \R$ satisfies
\begin{align*}
f(a) f(b) < 0.
\end{align*}

Find $x_\star \in [a, b]$ such that $f(x_\star) = 0$.
:::

::: {.algorithm title="Bisection method"}

**Setup**: $[a_0, b_0] \defeq [a, b]$.

**Repeat as often as necessary**

#. Let $x_i \defeq \frac {a_i + b_i} 2$.
#.
\begin{align*}
[a_{i + 1}, b_{i + 1}] \defeq 
\begin{cases}
[a_i, x_i] & \text{if } f(a_i) f(x_i) < 0\\
[x_i, b_i] & \text{otherwise}
\end{cases}
\end{align*}

:::

# The bisection method: invariants [@vaes22, p. 123] {.split}

::: {.remark title="Invariants"}
- $a_i \leq x_i \leq b_i$
- $b_i - a_i = \frac {b - a} {2^i}$
- $f(a_i) < 0 < f(b_i)$.
:::

::: proposition
The sequence $(x_n)_{n \in \N}$ converges to $x_\star \in [a, b]$
with $f(x_\star) = 0$.

Moreover, we have
\begin{align*}
\abs {x_n - x_\star} \leq \frac {b - a} {2^{n + 1}}
\end{align*}
:::

::: corollary
An error of size at most $\epsilon$ can be guaranteed with
\begin{align*}
n \defeq \ceil {\log_2 \frac {b - a} \epsilon}.
\end{align*}
iterations.
:::

# The bisection method: code [@vaes22, p. 124] {.split}

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

# Exercises (recitation) {.split}

::: {.exercise title="Exercise 5.1 p. 138"}
Implement the bisection method to find the solution(s) to the equation
$x = \cos(x)$.
:::

::: {.exercise title="Exercise 5.6 p. 140"}
Calculate
\begin{align*}
x \defeq \sqrt[3] {3 + \sqrt[3] {3 + \sqrt[3]{3 + \dots}}}
\end{align*}
:::

# Evaluating an algorithm {.split}

::: info
We shall be interested in the following questions.

- When does the algorithm converge? Does it converge to the right solution?
- How fast does it converge? (e.g. linear, superlinear, quadratic)
- What if there's a perturbation? Is the algorithm **stable**?
:::

# Convergence speed [@vaes22, pp. 122-123] {.split}

::: question
How fast is the convergence?
:::

::: {.definition}
We shall say $(\vec x_k)_{k \in \N}$ converges to $\vec x_\star$

- **linearly** if
  \begin{align*}
  \lim_{k \to +\infty}
  \frac {
  \norm {\vec x_{k + 1} - \vec x_\star}
  } {
  \norm {\vec x_k - \vec x_\star}
  } < 1.
  \end{align*}

- **superlinearly** if
  \begin{align*}
  \lim_{k \to +\infty}
  \frac {
  \norm {\vec x_{k + 1} - \vec x_\star}
  } {
  \norm {\vec x_k - \vec x_\star}
  } = 0.
  \end{align*}

- **quadratically** if
  \begin{align*}
  \lim_{k \to +\infty}
  \frac {
  \norm {\vec x_{k + 1} - \vec x_\star}
  } {
  \norm {\vec x_k - \vec x_\star}^2
  } \in \R.
  \end{align*}
:::

# Convergence speed: examples {.split}

::: example
The sequence $u_n = 2^{-n}$ converges linearly to $0$.
:::

::: proposition
In the bisection method,
$(x_n)_{n \in \N}$ converges linearly to the solution $x_\star$.
:::

# Fixed point iterations [@vaes22, p. 124] {.split}

Assume we want to solve the equation $\vec F(\vec x) = \vec x$.

::: proposition
Let $\vec F: \R^n \to \R^n$ be a continuous function.
If the iteration
\begin{align*}
\vec x_{k + 1} = \vec F(\vec x_k),
\end{align*}
converges to $\vec x_\star$, then $\vec F(\vec x_\star) = \vec x_\star$.
:::

::: {.example title="Splitting methods"}
A splitting $\mat A = \mat M - \mat N$ allows to recast the system
$\mat A \vec x = \vec b$ as a fixed point problem:
\begin{align*}
\vec x = \underbrace{\mat M^{-1} (\mat N \vec x + \vec b)}_{\vec F(\vec x)}
\end{align*}
:::

We will work on a general criterion for convergence and stability.

# Contraction [@vaes22, p. 126] {.split}

::: definition
A function $\vec F: \R^n \to \R^n$ is a **contraction**
if we can find $L < 1$ such that
\begin{align*}
\norm {\vec F(\vec y) - \vec F(\vec x)}
\leq L
\norm {\vec y - \vec x},
\qquad x, y \in \R^n.
\end{align*}
:::

::: example
- $\vec F(\vec x) = L \vec x$, with $L < 1$.
- A differentiable function $f: \R \to \R$ with $\sup \abs{f'} < 1$.
:::

::: text-center
![](https://francetoday.com/wp-content/uploads/2022/03/9639839563806.jpg){width=50%}
:::

# Banach's fixed point theorem [@vaes22, p. 126] {.split}

\begin{align*}
\text{contraction:} \qquad
\norm {\vec F(\vec y) - \vec F(\vec x)}
\leq L
\norm {\vec y - \vec x},
\qquad L < 1.
\end{align*}

::: {.theorem title="Banach's fixed point theorem"}
Let $\vec F: \R^n \to \R^n$ be a contraction with constant $L < 1$.
The iteration
\begin{align*}
\vec x_{k + 1} \defeq \vec F(\vec x_k)
\end{align*}
converges for each choice of $\vec x_0 \in \R^n$
towards the unique fixed point $\vec x_\star \in \R^n$ of $\vec F$.
Moreover, we have
\begin{align*}
\norm {\vec x_k - \vec x_\star} \leq L^k \norm {\vec x_0 - \vec x_\star}.
\end{align*}
:::

::: {.info title="Cauchy criterion for sequences"}
A sequence $(x_k)_{k \in \N}$ converges if and only if^[
Usually, this criterion is written
\begin{align*}
\forall \epsilon > 0 \quad \exists N > 0 \quad
\forall k, l \in \N : k, l \geq N \quad
\norm {\vec x_k - \vec x_l} \leq \epsilon.
\end{align*}
I hope you don't mind that I didn't write it like that.
]
\begin{align*}
\lim_{k, l \to +\infty} \norm {\vec x_k - \vec x_l} = 0.
\end{align*}
:::

# Convergence speed and stability [@vaes22, p. 126] {.split}

#. The equation
\begin{align*}
\norm {\vec x_{k + 1} - \vec x_\star} &\leq L \norm {\vec x_k - \vec x_\star}\\
\end{align*}
   shows we have **linear convergence**^[
   Confusingly, this type of convergence is sometimes called **exponential**
   or **geometric** because of the second equation.].

#. The equation
\begin{align*}
\norm {\vec x_k - \vec x_\star} &\leq L^k \norm {\vec x_0 - \vec x_\star}.
\end{align*}
   shows a property of strong **stability** called **global exponential stability**:
   should $\vec x_0$ be changed to *any* other value,
   we will still have convergence to $\vec x_\star$,
   with an estimate on that convergence.

# 29 March 2023

::::: {.col}

### Bisection method

\begin{align*}
[a_{i + 1}, b_{i + 1}] \defeq 
\begin{cases}
[a_i, x_i] & \text{if } f(a_i) f(x_i) < 0\\
[x_i, b_i] & \text{otherwise},
\end{cases}
\end{align*}

\begin{align*}
x_\star
\defeq \lim_{n \to +\infty} a_n
= \lim_{n \to +\infty} b_n
\end{align*}

Both sequences converge **linearly** to the solution $x_\star$.

\begin{align*}
f(x_\star)^2 = \lim_{n \to +\infty} f(a_i) f(b_i) \leq 0
\implies
f(x_\star) = 0.
\end{align*}

### Fixed point iteration

The simplest iterations take the form
\begin{align*}
\vec x_{k + 1} = \vec F(\vec x_k).
\end{align*}

Should $(\vec x_k)_{k \in \N}$ converge, it will be towards a fixed point
\begin{align*}
\vec x_\star \defeq \lim_{n \to +\infty} \vec x_k
\implies
\vec x_\star = \vec F(\vec x_\star).
\end{align*}

:::::

::::: {.col}

### Solving a non-linear system $\vec f(\vec x) = \vec 0$

Step 1
: Rewrite our equation $\vec f(\vec x) = \vec 0$ as a fixed point problem $\vec F(\vec x) = \vec x$.

Step 2
: Use the iteration $\vec x_{k + 1} = \vec F(\vec x_k)$.

### Banach fixed point theorem

If $\vec F$ is a contraction,
the iteration
\begin{align*}
\vec x_{k + 1} = \vec F(\vec x_k).
\end{align*}
converges towards the unique fixed point.
Moreover, convergence is **linear** and the solution is **exponentially stable**.

### Announcements

- Online Lecture on Friday 31 March 2022

:::::

# Comments on Banach's fixed point theorem {.split}

- Banach's fixed point theorem proves **existence**, **uniqueness**, a lower bound on **convergence speed** and **stability**.
- The constraint on $\vec F$ is **global** and **very strict**.
- In general, we our problems have a solution.

::: question
Could we turn Banach's fixed point theorem in a local result if we already assume the solution exists?
:::

# Local stability of a fixed point [@vaes22, p. 127] {.split}

::: definition
\begin{align*}
B_\delta(\vec x) \defeq \{ \vec y \in \R^n : \norm {\vec y - \vec x} \leq \delta \}
\end{align*}
:::

::: {.theorem title="Local Banach theorem"}
Assume that $\vec F(\vec x_\star) = \vec x_\star$ and
that there is $\delta > 0$ and $0 \leq L < 1$ such that
\begin{align*}
\norm {\vec F(\vec x) - \vec F(\vec x_\star)} \leq L \norm {\vec x - \vec x_\star}.
\end{align*}
for every $\vec x \in B_\delta(\vec x)$.

If $\vec x_0 \in B_\delta(\vec x)$, then
$\vec x_k \in B_\delta(\vec x)$ for every $k \in \N$ and
\begin{align*}
\norm {\vec x_k - \vec x_\star} &\leq L^k \norm {\vec x_0 - \vec x_\star}.
\end{align*}
:::

::: remark
The conclusion means that $\vec x_\star$ is a locally **exponentially stable** fixed point.
:::

# Calculus recap [@vaes22, p. 127] {.split}

Assume that $\vec F$ has partial derivatives at $x$.


::: {.definition title="Jacobian matrix"}
The matrix

\begin{align*}
\vec J_{\vec F} =
\begin{pmatrix}
\partial_1 F_1(\vec x) & \dots & \partial_n F_1(\vec x)\\
\vdots & \vdots & \vdots \\
\partial_1 F_n(\vec x) & \dots & \partial_n F_n(\vec x)
\end{pmatrix}
\end{align*}
is called the **Jacobian** matrix of $\vec F$ at $\vec x$.
:::

::: {.definition title="Differentiability"}
$\vec F$ is **differentiable** at $x \in \R^n$
if
\begin{align*}
\lim_{\vec h \to 0}
\frac {\norm {\vec F(\vec x + \vec h) - \vec F(\vec x) - \vec J_\vec F(\vec x) \vec h}}
{\norm {\vec h}} = 0
\end{align*}
:::

::: example
In dimension $1$, $\vec J_{\vec F}(\vec x) = \vec F'(\vec x)$.
:::

# A sufficient condition to be a local contraction [@vaes22, p. 127] {.split}

::: {.proposition}
Assume that $\vec F$ is a smooth function^[Being of class $C^1$ is enough.] around a fixed point $\vec x_\star$
and that
\begin{align*}
\norm {\vec J_{\vec F}(\vec x_\star)} < 1.
\end{align*}

There exists $0 \leq L < 1$ and $\delta > 0$ such that
\begin{align*}
\norm {\vec F(\vec x) - \vec F(\vec x_\star)} \leq L \norm {\vec x - \vec x_\star}.
\end{align*}
:::

# A sufficient condition for local exponential stability [@vaes22, p. 127] {.split}

::: theorem
Assume that $\vec F$ is a smooth function^[Actually, we can assume that $\vec F$ is of class $C^1$.]
around $\vec x_\star$
and that $\vec F(\vec x_\star) = \vec x_\star$.
If in addition
\begin{align*}
L \defeq \norm {\vec J_{\vec F}(\vec x_\star)} < 1,
\end{align*}
there exists $\delta > 0$ such that the following property holds:
if $\vec x_0 \in B_\delta(\vec x)$, then $\vec x_k \in B_\delta(\vec x_\star)$ for every $k \in \N$ and
\begin{align*}
\norm {\vec x_k - \vec x_\star} &\leq L^k \norm {\vec x_0 - \vec x_\star}.
\end{align*}
:::

# A sufficient condition for *superlinear* convergence [@vaes22, p. 128] {.split}

::: {.proposition title="Superlinear convergence towards a fixed point"}
Assume that $\vec x_\star$ is a fixed point of a smooth function $\vec F$.
If $\vec J_{\vec F}(\vec x_\star) = 0$
then should an iterative sequence converge to $\vec x_\star$,
it does so **superlinearly**.
:::

# Chord method [@vaes22, p. 129] {.split}

Let's write $f(x) = 0$ as a fixed point problem.

::: proposition
Let $a \neq 0$ and consider
\begin{align*}
F(x) \defeq x - \frac {f(x)} {a}.
\end{align*}

Then $f(x) = 0$ if and only if $F(x) = x$.
:::

::: proposition
Let $\mat A$ be invertible and consider
\begin{align*}
\vec F(\vec x) \defeq \vec x - \mat A^{-1} \vec f(\vec x).
\end{align*}

Then $\vec f(\vec x) = \vec 0$ if and only if $\vec F(\vec x) = \vec x$.
:::

# Interpretation of the chord method [@vaes22, Figure 5.1 p. 130] {.split}

~~~ {.tex .tikz opts="thick, yscale=0.65"}
\draw[-latex,name path=xaxis] (-1,0) -- (12,0) node[above]{\large $x$};
\draw[-latex] (0,-2) -- (0,8)node[right]{\large $y$};;
\draw[ultra thick, blue,name path=function]  plot[smooth,domain=1:9.5] (\x, {0.1*\x^2-1.5}) node[left]{$f(x)$};
\node[red,right=0.2cm] at (8,4.9) {\large Affine approximation};
\draw[gray,thin,dotted] (8,0) -- (8,4.9) node[circle,fill,inner sep=2pt]{};
\draw[dashed, red,name path=Tfunction]  plot[smooth,domain=0:9.5] (\x, {0.7*(\x-8) + 4.9});
\draw (8,0.1) -- (8,-0.1) node[below] {$x_k$};
\draw [name intersections={of=Tfunction and xaxis}] ($(intersection-1)+(0,0.1)$) -- ++(0,-0.2) node[below,fill=white] {$x_{k+1}$} ;
~~~

::: {.info title="Interpretation of the chord method"}
Given $x_k$, $x_{k + 1}$ is the root of the affine function with gradient $a$ going through $(x_k, f(x_k))$.
:::

# Convergence of the chord method [@vaes22, p. 129] {.split}

A good choice of $\mat A$ is $\mat A \approx \vec J_{\vec f}(\vec x_\star)$.

::: {.proposition title="Convergence of the chord method"}
Assume that
\begin{align*}
\norm {\mat I - \mat A^{-1} \vec J_{\vec f}(\vec x_\star)} < 1
\end{align*}
Then the iteration
\begin{align*}
\vec x_{k + 1} \defeq \vec F(\vec x_k)
\defeq \vec x_k - \mat A^{-1} \vec f(\vec x_k)
\end{align*}
locally converges to $\vec x_\star$,
and is a locally exponentially stable fixed point of $\vec F$.

Moreover, if $\mat A = \vec J_{\vec f}(\vec x_\star)$,
then the convergence of the chord method is at least **superlinear**.
In fact, if $f$ is of class $C^2$ around $\vec x_\star$,
then the convergence is **quadratic**.
:::

# Quadratic convergence of the chord method {.split}

::: proposition
Let $x_\star \in \R$ be a root of a function $f : \R \to \R$.
If $f$ is of class $C^2$ around $x_\star$ and $f'(x_\star) \neq 0$,
then the iteration
\begin{align*}
x_{k + 1} \defeq x_k - \frac {f(x_k)} {f'(x_\star)}
\end{align*}
converges **quadratically**
provided that $x_0$ is sufficiently close to $x_\star$.
:::

# Meaning of quadratic convergence {.split}

::: {.info title="Quadratic convergence"}
\begin{align*}
\lim_{k \to +\infty}
\frac {
\norm {\vec x_{k + 1} - \vec x_\star}
} {
\norm {\vec x_k - \vec x_\star}^2
} = C.
\end{align*}
:::

Assume that $\abs {x_k - x_\star} = 10^{-p}$.
It follows that

\begin{align*}
\abs {x_{k + 1} - x_\star} \leq C \times 10^{-2p}.
\end{align*}

Intuitively, provided that $C$ isn't too large,
the number of \emph{correct decimals} double at each iteration
if we are sufficiently close to the solution.

# Chord method in Julia {.split}

\begin{align*}
x_{k + 1} \defeq \underbrace{x_k - \frac {f(x_k)} a}_{F(x_k)}
\end{align*}

~~~ {.julia .jupyter}
function chord_method(f, x, a, ϵ = 10^-12)
    while abs(f(x)) > ϵ
        x -= f(x) / a
    end
    return x
end

chord_method(x -> x^2 - 2, 1.41, 2.82)
~~~

# Exercise 5.7 [@vaes22, pp. 139] {.split}

::: exercise
Solve the equation $f(x) = \e^x - 2 = 0$ using a fixed point iteration of the form
\begin{align*}
x_{k+1} = F(x_k), \qquad
F(x) = x - \alpha^{-1} f(x).
\end{align*}
Using your knowledge of the exact solution $x_* = \log 2$,
write a sufficient condition on $\alpha$ to guarantee that $x_*$ is locally exponentially stable.
Verify your findings numerically and plot,
using a logarithmic scale for the $y$ axis,
the error in absolute value as a function of $k$.
:::

# 3 April 2023

::::: {.col}

### Solving $\vec f(\vec x) = \vec 0$

Step 1
: Rewrite $\vec f(\vec x) = \vec 0$ as a **fixed point** problem $\vec F(\vec x) = \vec x$.

Step 2
: Use the iteration $\vec x_{k + 1} = \vec F(\vec x_k)$.

### Local convergence

::: theorem
If $\norm {\vec J_{\vec F}(\vec x_\star)} < 1$,
the iteration
\begin{align*}
\vec x_{k + 1} \defeq \vec F(\vec x_k)
\end{align*}
converges to $\vec x_\star$
provided that $\vec x_0$ is sufficiently close to $\vec x_\star$,
and that fixed point is locally exponentially stable.

If in addition $\vec J_{\vec F}(\vec x_\star) = \mat 0$,
then convergence is **superlinear**.
:::

:::::

::::: {.col}

### Chord method

~~~ {.tex .tikz opts="thick, yscale=0.65"}
\draw[-latex,name path=xaxis] (-1,0) -- (12,0) node[above]{\large $x$};
\draw[-latex] (0,-2) -- (0,8)node[right]{\large $y$};;
\draw[ultra thick, blue,name path=function]  plot[smooth,domain=1:9.5] (\x, {0.1*\x^2-1.5}) node[left]{$f(x)$};
\node[red,right=0.2cm] at (8,4.9) {\large Affine approximation};
\draw[gray,thin,dotted] (8,0) -- (8,4.9) node[circle,fill,inner sep=2pt]{};
\draw[dashed, red,name path=Tfunction]  plot[smooth,domain=0:9.5] (\x, {0.7*(\x-8) + 4.9});
\draw (8,0.1) -- (8,-0.1) node[below] {$x_k$};
\draw [name intersections={of=Tfunction and xaxis}] ($(intersection-1)+(0,0.1)$) -- ++(0,-0.2) node[below,fill=white] {$x_{k+1}$} ;
~~~

\begin{align*}
\vec f(\vec x) = \vec 0
\iff \vec F(\vec x) = \vec x - \mat A^{-1} \vec f(\vec x)
\end{align*}

- $\vec J_{\vec F}(\vec x) = \mat I - \mat A^{-1} \vec J_{\vec f}(\vec x)$
- $\mat A = \vec J_{\vec f}(\vec x_\star) \implies$ **quadratic** convergence.

### Announcements

- Homework due Wednesday 12 April: Exercise 5.12
- French sentence of the day: Le certificat de naissance long format^[
  Unfortunately, I couldn't find a French translation for 'perp walk',
  so this will have to do.]

:::::

# Towards Newton-Raphson {.split}

::: {.info title="Chord method"}
\begin{align*}
x_{k + 1} \defeq x_k - \frac {f(x_k)} a
\end{align*}
:::

::: {.remark title="Newton-Raphson iteration"}
Convergence of the chord method can be accelerated by having $a = f'(x_\star)$.

As $x_\star$ is not known,
an alternative would be to use the approximation $a \approx f'(x_k)$ and get
\begin{align*}
x_{k + 1} \defeq x_k - \frac {f(x_k)} {f'(x_k)}
\end{align*}
:::

# Newton-Raphson [@vaes22, p. 130] {.split}

~~~ {.tex .tikz opts="thick, yscale=0.65"}
\draw[-latex,name path=xaxis] (-1,0) -- (12,0) node[above]{\large $x$};
\draw[-latex] (0,-2) -- (0,8)node[right]{\large $y$};;
\draw[ultra thick, blue,name path=function]  plot[smooth,domain=1:9.5] (\x, {0.1*\x^2-1.5}) node[left]{$f(x)$};
\node[red,right=0.2cm] at (8,4.9) {\large Tangent};
\draw[gray,thin,dotted] (8,0) -- (8,4.9) node[circle,fill,inner sep=2pt]{};
\draw[dashed, red,name path=Tfunction]  plot[smooth,domain=4.25:9.5] (\x, {1.6*\x-7.9});
\draw (8,0.1) -- (8,-0.1) node[below] {$x_k$};
\draw [name intersections={of=Tfunction and xaxis}] ($(intersection-1)+(0,0.1)$) -- ++(0,-0.2) node[below,fill=white] {$x_{k+1}$} ;
~~~

# Newton-Raphson: animation

~~~ {.yaml .widget name="geogebra"}
url: https://www.geogebra.org/m/DGFGBJyU
~~~

# Newton-Raphson iteration [@vaes22, p. 130] {.split}

::: {.algorithm title="Newton-Raphson"}
\begin{align*}
x_{k + 1} \defeq x_k - \frac {f(x_k)} {f'(x_k)}
\end{align*}
:::

::: {.algorithm title="Newton-Raphson in higher dimension"}
\begin{align*}
\vec x_{k + 1} \defeq \vec x_k - \vec J_f(\vec x_k)^{-1} \vec f(\vec x_k)
\end{align*}
:::

# Newton-Raphson: implementation {.split}

~~~ {.julia .jupyter}
using Zygote # Library for automatic differentiation
function newton_raphson(f, x, ϵ = 10^-12)
    while abs(f(x)) > ϵ
        x -= f(x) / f'(x)
    end
    return x
end
newton_raphson(x -> x^2 - 2, 1.41)
~~~

~~~ {.julia .jupyter}
using LinearAlgebra, Zygote
function newton_raphson(f, x, ϵ = 10^-12)
    while norm(f(x)) > ϵ
        x -= jacobian(f, x)[1] \ f(x)
    end
    return x
end
~~~


# Exercises 5.8 and 5.9 [@vaes22, p. 139]

::::: {.col}
::: exercise
Implement the Newton–Raphson method for solving $f(x) = e^x − 2 = 0$, and
plot the error in absolute value as a function of the iteration index $k$.
:::

::: exercise
Find the point $(x, y)$ on the parabola $y = x^2$ that is closest to the point $(3, 1)$.
:::
:::::

::::: {.col}

~~~ {.julia .jupyter}
using Zygote # Library for automatic differentiation
function newton_raphson(f, x, ϵ = 10^-12)
    while abs(f(x)) > ϵ
        x -= f(x) / f'(x)
    end
    return x
end
newton_raphson(x -> x^2 - 2, 1.41)
~~~

:::::

# Convergence and convergence speed [@vaes22, p. 131] {.split}

Given how we arrived at the Newton-Raphson method from the chord method,
it should not surprise us that we get superlinear convergence.

::: proposition
If $x_\star$ is a simple root, then the Newton-Raphson iteration converges superlinearly.
:::

::: idea
Simply show that $F'(x_\star) = 0.$
:::

# Quadratic convergence [@vaes22, p. 132] {.split}

::: theorem
Assume that $x_\star$ is a root of a function $f \in C^2(\R)$ with $f'(x_\star) \neq 0$.
There exists $\delta > 0$ such that if $x_0 \in B_\delta(x_\star)$,
the iteration
\begin{align*}
x_{k + 1} \defeq x_k - \frac {f(x_k)}{f'(x_k)}
\end{align*}

then $(x_k)_{k \in \N}$ converges **quadratically** to $\vec x$.
:::

# BigFloat in Julia

The `BigFloat` format has arbitrary precision.

~~~ {.julia}
# Set precision in bits
setprecision(50)

# Number of correct digits in base 10
setprecision(50, base=10)

BigFloat(π)
~~~

# A Numerical experiment: $\sqrt 2$ [@vaes22, p. 137]

~~~ {.julia .jupyter}
function sqrt_two(x, ε = 10^-200)
  f(x) = x^2 - 2
  error(x) = abs(x - sqrt(BigFloat(2)))
  while error(x) > ε
    x -= f(x) / (2√BigFloat(2))
    digits = ceil(Int, -log10(error(x)))
    println("Number of correct digits: $digits")
  end
end
setprecision(400, base=10)
sqrt_two(BigFloat(1.41))
~~~

# A Numerical experiment: $\pi$ [@vaes22, p. 137]

~~~ {.julia .jupyter}
function my_pi(x, ε = 10^-200)
  f(x) = sin(x)
  error(x) = abs(x - BigFloat(π))
  while error(x) > ε
    x -= f(x) / -1
    digits = ceil(Int, -log10(error(x)))
    println("Number of correct digits: $digits")
  end
end
setprecision(400, base=10)
my_pi(BigFloat(3.14))
~~~

# The secant method [@vaes22, p. 135] {.split}

::: question
What if we don't know the derivative,
but still want superlinear convergence or better?
:::

::: {.idea title="Secant method"}
The next iteration $x_{k + 2}$ is given by the root of
\begin{align*}
f(x_k) + \frac {f(x_{k + 1}) - f(x_k)} {x_{k + 1} - x_k} (x - x_k)
\approx f(x)
\end{align*}
:::

::: proposition
\begin{align*}
x_{k + 2}
= \frac {f(x_{k + 1}) x_k - f(x_k) x_{k + 1}} {f(x_{k + 1}) - f(x_k)}
\end{align*}
:::

# The secant method: implementation [@vaes22, p. 135]

~~~ {.julia .jupyter}
function secant(f, x, ϵ = 10^-12)
    while abs(f(x[end])) > ϵ
        push!(x, (f(x[end]) * x[end-1] - f(x[end-1]) * x[end]) / (f(x[end]) - f(x[end-1])))
    end
    return x
end
secant(x -> x^2 - 2, [1.4, 1.41])
~~~

~~~ {.julia .jupyter}
function secant(f, x, ϵ = 10^-12)
    while abs(f(x[end])) > ϵ
        x = [x[2], (f(x[2]) * x[1] - f(x[1]) * x[2]) / (f(x[2]) - f(x[1]))]
    end
    return x
end
secant(x -> x^2 - 2, [1.4, 1.41])
~~~

# Convergence of the secant method [@vaes22, p. 135] {.split}

::: theorem
Assume that $x_\star$ is a root of a function $f C^2(\R)$ with $f'(x_\star) \neq 0$.
There exists $\delta > 0$ such that if $x_0, x_1 \in B_\delta(x_\star)$,
the iteration defined by
\begin{align*}
x_{k + 2}
= \frac {f(x_{k + 1}) x_k - f(x_k) x_{k + 1}} {f(x_{k + 1}) - f(x_k)}
\end{align*}
satisfies
\begin{align*}
\lim_{k \to +\infty}
\frac {\abs{x_{k + 1} - x_\star}} {\abs{x_k - x_\star}^\varphi} \in \R,
\qquad \varphi^2 - \varphi - 1 = 0.
\end{align*}
:::

::: remark
$\varphi$ is known as the **golden ratio**.
:::

# Bibliography
