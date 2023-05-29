# Formulae

## First order ODEs

### Separable equations

\begin{align*}
\frac {\dd y} {\dd x} = \frac {g(x)} {h(y)}
\implies \int h(y) \dd y = \int g(x) \dd x.
\end{align*}

### Linear equations

\begin{align*}
y' + P(x) y = f(x)
\implies
(\mu(x) y)' &= \mu(x) f(x),
\quad \mu(x) = e^{\int P(x) \dd x}
\end{align*}

### Exact equations: <small>$M(x, y) \dd x + N(x, y) \dd y = 0$ with $\partial_y M = \partial_x N$</small>

~~~ {.tex .tikz .fragment scale=1}
\node (M) at (-1, 0) {$M(x, y) dx$};
\node at (0, 0) {$+$};
\node (N) at (1, 0) {$N(x, y) dy$};
\node at (2.3, 0) {$=0$};
\node (f) at (0, -2) {$f(x, y)$};
\draw [->] (M) to[out=225,in=180] node[left]{$\int dx$} (f);
\draw [->] (f) -- node[left]{$\partial_x$} (M);
\draw [->] (f) -- node[right]{$\partial_y$} (N);
\draw [->] (N) to[out=-45,in=0] node[right]{$\int dy$} (f);
~~~

### Non-exact equations

\begin{align*}
\mu(x) = e^{\int \frac {M_y - N_x} N \dd x}
\quad \text{or} \quad
\mu(y) = e^{\int \frac {N_x - M_y} M \dd y}
\end{align*}

\begin{align*}
\mu M \dd x + \mu N \dd y = 0
\implies \text{exact case}
\end{align*}

### Substitutions

Type                    Substitution
-----                   --------------
Homogeneous             $y = ux$
$y' + P(x)y = f(x)y^n$  $u = y^{1 - n}$
$y' = f(Ax+By+C)$       $u = Ax + By + C$

## Second-order ODEs

### Linear equations with constant coefficients

\begin{align*}
ay'' + by' + cy &= g(x)\\
y &= y_p + y_h
\end{align*}

#### Homogeneous equation

\begin{align*}
y(x) = \begin{cases}
c_1 e^{m_1 x} + c_2 e^{m_2 x} & \text{if two solutions}\\
c_1 e^{m x} + c_2 x e^{m x} & \text{if one solution}\\
e^{\alpha x} (c_1 \cos \beta x + c_2 \sin \beta x) & \text{complex solutions}\ \alpha \pm i \beta\\
\end{cases}
\end{align*}
