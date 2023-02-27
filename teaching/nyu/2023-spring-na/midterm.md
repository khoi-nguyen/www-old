---
title: Midterm
...

## Chapter 1: Floating point arithmetic

Expect True/False questions.

- Adding and multiplying in other bases
- Converting between different bases, including recurring decimals
- Know that $0.1$ does not have a finite binary representation and be able to use that fact
- Understand floating formats
- Understand how the spacing between consecutive numbers evolves
- Understand what the machine $\epsilon$ represents
- Understand how machine operations are defined
- Understand that the machine addition/multiplication is not commutative and be able to provide an example
- Understand how to reorganize a sum for best accuracy

Exercises: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 1.10, 1.11, 1.25

## Chapter 2: Interpolation and approximation

- Write the interpolation equations under matrix form, in particular for the Vandermonde, Langrange and Gregory-Newton cases
- Interpolate a polynomial in the Lagrange basis
- Interpolate a polynomial with the Gregory-Newton formula
  (equidistant and non-equidistant)
- Understand the strengths and weaknesses of each interpolation method
- Know, use and understand the consequences of the interpolation error
- Prove that piecewise interpolation converges uniformly to a smooth function
- Understand the role of Chebyshev polynomials, and be able to prove basic properties
- Understand why Chebyshev nodes may be more suited to interpolation
- Derive the normal equations for least square and mean square approximation
- Apply the Gram-Schmidt algorithm to derive orthogonal polynomials

Exercises: 2.1, 2.2, 2.3, 2.5, 2.6, 2.7

## Chapter 3: Numerical integration

- Find the weights associated with a quadrature rule (Newton-Cotes, Gauss-Legendre, or more general rules)
- Prove that the weights are given by the integral of the Lagrange polynomials
- Understand how to write a composite rule
- Know the composite trapezium and Simpson rules, and their associated error estimates
- Know for what polynomials a quadrature rule is exact
- Apply a composite rule to calculate an integral and show its associated error
- Apply one iteration of Romberg's method
- Prove that the nodes in Gauss-Legendre polynomial are the roots of a Legendre polynomial
- Prove that the weights are positive in Gauss-Legendre quadrature
- Understand the strengths and weaknesses of each integration method (Newton-Cotes, composite Newton-Cotes, Gauss-Legendre)
- Be able to explain the curse of dimensionality
  and how $\bigo (h^k)$ actually means $\bigo (N^{-\frac k d})$

Exercises: 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.9, 3.10

## Chapter 4: Linear systems

- Find the LU decomposition and understand why/how it works
- Forward and backward substitution
- Find the Cholesky decomposition of a symmetric matrix
- Know or be able to calculate the complexity of these algorithms
