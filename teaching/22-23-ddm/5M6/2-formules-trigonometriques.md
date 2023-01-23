---
title: Formules trigonométriques
output: revealjs
...

# Formules trigonométriques

::: {.block title="Motivations"}
Dans le chapitre sur les dérivées,
nous aurons besoin de pourvoir écrire $\sin (a + b)$ et $\cos (a + b)$
en terme de $\sin a$, $\cos a$, $\sin b$, $\cos b$.
:::

# Rappels: distance et relation fondamentale {.split}

- Calculer la distance entre $A(2, 1)$ et $B(4, -2)$ (5-24).
- Montrer que $\sin^2 x + \cos^2 x = 1$.

# $\cos(a - b)$ p. 5-23 {.split}

![](/static/images/1673999517.png)

::: proposition
$$\cos (a - b) = \cos a \cos b + \sin a \sin b.$$
:::

# $\cos(a + b)$ p. 5-25 {.split}

::: proposition
$$\cos(a + b) = \cos a \cos b - \sin a \sin b.$$
:::

# $\sin(a - b)$ p. 5-25 {.split}

::: proposition
$$\sin x = \cos \left(\frac \pi 2 - x\right)$$
:::

::: proposition
$$\sin(a - b) = \sin a \cos b - \cos a \sin b.$$
:::

# $\sin(a + b)$ p. 5-26 {.split}

::: proposition
$$\sin(a + b) = \sin a \cos b + \cos a \sin b.$$
:::

# $\tan(a - b)$ p. 5-26 {.split}

::: proposition
$$\tan (a - b) = \frac {\tan a - \tan b} {1 + \tan a \tan b}$$
:::

# $\tan(a + b)$ p. 5-26 {.split}

::: proposition
$$\tan (a + b) = \frac {\tan a + \tan b} {1 - \tan a \tan b}$$
:::

# Formules de duplication 5-27 {.split}

::: {.exampleblock title="Rappel"}
$$\sin(a + b) = \sin a \cos b + \cos a \sin b.$$
$$\cos(a + b) = \cos a \cos b - \sin a \sin b.$$
$$\tan (a + b) = \frac {\tan a + \tan b} {1 - \tan a \tan b}$$
:::

::: proposition
$$\cos 2a = \cos^2 a - \sin^2 a$$
$$\sin 2a = 2 \sin a \cos a$$
$$\tan 2a = \frac {2 \tan a} {1 - \tan^2 a}$$
:::

# Exercices dirigés 5-27, 5-28 {.split}

::: {.exampleblock title="Rappel"}
$$\sin (a \pm b) = \sin a \cos b \pm \cos a \sin b$$
$$\cos (a \pm b) = \cos a \cos b \mp \sin a \sin b$$
$$\tan (a \pm b) = \frac {\tan a \pm \tan b} {1 \mp \tan a \tan b}$$
:::

::: exercise
1. Réduire $\cos 3x \cos 5x - \sin 3x \sin 5x$
2. Calculer $A = \frac {\sin 3x} {\sin x} - \frac {\cos 3x} {\cos x}$.
3. Sans calculatrice, calculer $\cos 15^\circ$
4. Montre que $\sin^2 (a + b) + \cos^2 (a - b) = 1 + \sin 2a \sin 2b$.
5. Montre que
   $$\sin \left(\frac \pi 4 - x\right) \cos\left(\frac {3 \pi} 4 + x\right)
   + \sin\left(\frac {3 \pi} 4 + x\right) \cos \left(\frac \pi 4 - x\right) = 0$$
:::

# Exercices dirigés 5-29 {.split}

::: {.exampleblock title="Rappel"}
$$\sin (a \pm b) = \sin a \cos b \pm \cos a \sin b$$
$$\cos (a \pm b) = \cos a \cos b \mp \sin a \sin b$$
$$\tan (a \pm b) = \frac {\tan a \pm \tan b} {1 \mp \tan a \tan b}$$
:::

::: exercise
1. On donne $\sin a = \frac 3 5$ avec $a$ au premier quadrant.
   a. Calcule $\sin 2a$, $\cos 2a$ et $\tan 2a$ sans utiliser la calculatrice.
   b. En déduire à quel cadrant appartient $2a$. Justifie.
2. Poser les CE et résoudre
   a. $\tan(45^\circ + a) - \tan(45^\circ - a) = 2 \tan 2 a$
   b. $\frac {\cot^2 a - 1} {\cot^2 a + 1} = \cos 2a$.
:::

# Exercices sur les formules d'addition et duplication 5-30 {.split}

::: {.exampleblock title="Rappel"}
$$\sin (a \pm b) = \sin a \cos b \pm \cos a \sin b$$
$$\cos (a \pm b) = \cos a \cos b \mp \sin a \sin b$$
$$\tan (a \pm b) = \frac {\tan a \pm \tan b} {1 \mp \tan a \tan b}$$
:::

# Formules de Carnot 5-36 {.split}

::: {.proposition title="Formules de Carnot"}
$$\cos^2 a = \frac {1 + \cos 2a} 2.$$
$$\sin^2 a = \frac {1 - \cos 2a} 2.$$
:::

::: exercise
- Calcule, sans calculatrice, $\cos 15^\circ$.
- Montre que
  $$\frac {\cos a} {1 + \cos a} \cdot \frac {\sin 2a} {1 + \cos 2a} = \tan \frac a 2$$
:::

# Formules de Simpson 5-37 {.split}

::: {.proposition title="Formules de Simpson"}
$$\sin a + \sin b = 2 \sin \frac {a + b} 2 \cos \frac {a - b} 2$$
$$\sin a - \sin b = 2 \sin \frac {a - b} 2 \cos \frac {a + b} 2$$
:::

::: example
$$\sin 4x + \sin 2x = \dots$$
:::

# Formules de Simpson 5-38 {.split}

::: {.proposition title="Formules de Simpson"}
$$\sin a + \sin b = 2 \sin \frac {a + b} 2 \cos \frac {a - b} 2$$
$$\sin a - \sin b = 2 \sin \frac {a - b} 2 \cos \frac {a + b} 2$$
$$\cos a + \cos b = 2 \cos \frac {a + b} 2 \cos \frac {a - b} 2$$
$$\cos a - \cos b = -2 \sin \frac {a + b} 2 \sin \frac {a - b} 2$$
:::

# Exercices dirigés sur les formules de Simpson 5-39

::: {.proposition title="Formules de Simpson"}
$$\sin a + \sin b = 2 \sin \frac {a + b} 2 \cos \frac {a - b} 2$$
$$\sin a - \sin b = 2 \sin \frac {a - b} 2 \cos \frac {a + b} 2$$
$$\cos a + \cos b = 2 \cos \frac {a + b} 2 \cos \frac {a - b} 2$$
$$\cos a - \cos b = -2 \sin \frac {a + b} 2 \sin \frac {a - b} 2$$
:::
