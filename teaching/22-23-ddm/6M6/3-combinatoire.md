---
title: Probabilités et combinatoire
output: revealjs
...

# Journée internationale des femmes

Ada Lovelace
:   A écrit le premier programme informatique

Emmy Noether (physique mathématique)
:   Conservation de l'énergie provient de l'invariance du temps sous les translations.

Maryam Mirzakhani (topologie et géométrie)
:   Première femme à recevoir la médaille Fields (2014)

# Qu'est-ce qu'une probabilité?

~~~ {.julia .jupyter}
using Plots, Statistics
N = 5000
X = rand(0:1, N)
plot(1:N, n -> mean(X[1:n]), label="Fréquence de 'pile'")
plot!(1:N, n -> 0.5, label="Résultat théorique (50%)")
~~~

# Définition (empirique) de probabilité {.split}

::: {.definition title="Probabilité (Borel, Komolgorov)"}
La probabilité d'un événement est la limite (*presque sûre*)
\begin{align}
\lim_{n \to +\infty} \frac {\text{\# réalisations sur } n \text{ essais}} n
\end{align}
:::

::: remark
On parle de limite *presque sûre* puisqu'il reste possible de n'obtenir que des "faces"
en jouant à pile ou face.
Pour cette suite particulière, la fréquence de "face" converge vers $1$.
![](/static/images/1678138694.png){width=100%}
:::

# Introduction: Théorème central limite {.split}

~~~ {.julia .jupyter}
using Plots
n = 5
results = [sum(rand(1:6, n)) for i in 1:10^6]
f(x) = count(i -> i == x, results)
bar(n:6n, f, label="Distribution des lancers de dés")
~~~

# Théorème central limite {.split}

::: {.quote title="Francis Galton"}
I know of scarcely anything so apt to impress the imagination
as the wonderful form of cosmic order expressed by the law of frequency of error.
The law would have been personified by the Greeks if they had known of it.
It reigns with serenity and complete self-effacement amidst the wildest confusion.
The larger the mob, the greater the apparent anarchy, the more perfect is its sway.
It is the supreme law of unreason.
:::

# Monty-Hall

~~~ {.julia}
switch = false

function play(switch=false)
    choices = [0, 1, 2]
    correct, choice = rand(0:2), 0
    if switch
        return
    end
    return
end
~~~
