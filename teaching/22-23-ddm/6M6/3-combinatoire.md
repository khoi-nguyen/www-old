---
title: Probabilités et combinatoire
output: revealjs
...

# Qu'est-ce qu'une probabilité? {.split}

::: question
Qu'est-ce qu'une probabilité?
:::

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

# Combinatoire: motivations {.split}

::: info
\begin{align}
\text{probabilité} = \frac {\text{nombre de cas favorables}} {\text{nombre de cas possibles}}
\end{align}
:::

::: example
- Quelle est la probabilité de gagner au lotto?
- Quelle est la probabilité d'avoir une quinte flush?
:::

Il faut apprendre à **dénombrer**.

# Exploration {.split}

![](/static/images/1678370739.png)

# Anagrammes {.split}

![](/static/images/1678370770.png)

# Bonjour

![](/static/images/1678433789.png)

# Planche de Galton {.split}

![](/static/images/1678370800.png)
![](/static/images/1678370815.png)

# La factorielle {.split}

::: question
Combien y a-t-il de manière d'ordonner $n$ objets distincts?
:::

~~~ {.julia .jupyter}
function factorielle(n)
  if n == 1
    return 1
  end
  return n * factorielle(n - 1)
end
factorielle(4)
~~~

# Exercices sur la factorielle {.split}

![](/static/images/1678371142.png){width=100%}

# Former des "mots" et équipes {.split}

![](/static/images/1678399819.png){width=100%}

# Explosion factorielle {.split}

::: info
La croissance de la factorielle est au coeur de nombreux problèmes ouverts en maths.
:::

::: question
Je voudrais délivrer des pizzas à 20 élèves mais souhaite commencer
seulement lorsque j'aurai trouvé le chemin le plus court.
En essayant $1000$ possibilité par seconde, combien de temps cela prendrait?
:::

~~~ {.python .jupyter}
n = factorial(20)

# Combien de secondes cela prendra
secondes = n / 1000
~~~

# Combinaisons {.split}

\begin{align}
\binom n k = \frac {n!} {k! (n - k)!}
\qquad k \text{ parmi } n
\end{align}

![](/static/images/1678400990.png){width=100%}

# Dénombrer {.split}

![](/static/images/1678430160.png){width=100%}

# Dénombrer 2 {.split}

![](/static/images/1678430213.png){width=100%}

# Dénombrer 3 {.split}

![](/static/images/1678430295.png){width=100%}

# Exercices supplémentaires {.split}

![](/static/images/1678697050.png){width=100%}

