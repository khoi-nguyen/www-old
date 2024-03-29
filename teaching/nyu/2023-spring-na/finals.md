---
title: Finals
...

## Chapter 4

- Perform an LU decomposition and using it to solve a linear system
- Perform a Cholesky decomposition and using it to solve a linear system
- Vector norms, especially $p = 1, 2, +\infty$.
- Matrix norms, especially $p = 1, 2, +\infty$.
- Understand the notion of spectral radius
- Understand that the behaviour of $\matrix A^k$ is linked to its spectral radius.
- Understand the condition number of a matrix.
- Richardson's method
  (iteration, interpretation as an optimisation problem or as a splitting method,
  optimality criterion)
- Splitting methods (iteration, convergence criterion with the spectral radius)
- Understand the differences between Jacobi, Gauss-Seidel and Relaxation
  (you will be given the formulae).
- Understand the steepest descent,
  and be able to derive the optimal step.

## Chapter 5

- Bisection method
- Linear, superlinear and quadratic convergence
- Understand the link between iterations and fixed point problems
- The Banach Fixed Point theorem and its proof
- Consequences of Banach on existence, uniqueness, convergence,
  convergence speed, and stability
  ("global exponential stability").
- Local Banach fixed point theorem
- Proof that $\norm {J_F} < 1$ implies local exponential stability.
- Understand why $\norm {J_F} = 0$ at the solution is good for convergence speed
  (at least superlinear convergence).
- Chord method: interpretation, iteration, convergence
- Newton-Raphson: interpretation, iteration, convergence (+proof of quadratic convergence)

## Chapter 6

- Understand PageRank and calculate exact page rank vectors for small networks
- Understand the link between PageRank and the power iteration.
- Angle between two vectors
- Power iteration
- Why the Banach theory doesn't apply to the power iteration, essential convergence
- Inverse iteration
- Railey quotient iteration
- Reduced QR decompositions
- Subspace iterations
- The QR algorithm, and its link to subspace iterations

# Algorithms

List of the algorithms you need to be able to write in pseudo-code

- Splitting methods (general case)
- Bisection method
- Newton-Raphson
- Power iteration
- Subspace iteration
- QR algorithm

# Questions you need to be able to answer

- Why is an iterative method preferable over a classical method such as the LU decomposition
  when solving a system?
- Interpret the Richardson method as an optimization problem.
- In your own words, explain what it means for a sequence to converge quadratically.
  Give an example of such sequence.
- Explain the link between iteration and fixed point problems.
  Give an example of an iteration that cannot be written as a fixed point problem.
- Give the interpretation of the Newton-Raphson method
- Why could the Newton-Raphson method fail?
- Explain the PageRank algorithm, what it represents and its link to eigenvalue problems.
- Why do we talk about **essential convergence** in the power iteration?
