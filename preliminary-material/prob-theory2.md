# Probability Theory 2: Advanced Topics

## Course Information
**Author**: George Kesidis  
**Date**: December 26, 2019

## Outline
1. Definitions: sample space and (measurable) random variables
2. σ-algebras
3. Expectation (integration)
4. Conditional expectation
5. Useful inequalities
6. Independent random variables
7. The central limit theorem
8. Laws of large numbers: Borel-Cantelli lemma
9. Uniform integrability
10. Kolmogorov's extension theorem for consistent finite-dimensional distributions

## Sample Space and Events

### Basic Definitions
- **Random experiment**: Results in an outcome (or "sample") $\omega$
- **Sample space**: $\Omega$ - space of all outcomes, i.e., $\omega \in \Omega$
- **Event**: A subset of $\Omega$

### Examples
- **Dice experiment**: Outcome is exact orientation and position of dice on table
- **Event example**: "The sum of dots on upward facing surfaces is 7"

### Event Operations
- Event $A \subseteq \Omega$ has **occurred** if $\omega \in A$
- Events $A$ **and** $B$ occurred if $\omega \in A \cap B$
- Events $A$ **or** $B$ occurred if $\omega \in A \cup B$

**Note**: Sample space $\Omega$ is an abstract, unordered set in general.

Let $\mathcal{F}$ be the set of events, i.e., $A \in \mathcal{F} \Rightarrow A \subseteq \Omega$.

## Probability Measures

### Definition
A **probability measure** $P$ maps each event $A \subseteq \Omega$ to a real number between zero and one inclusive:
```math
P: \mathcal{F} \to [0,1]
```

### Properties
1. **Normalized**: $P(\Omega) = 1$
2. **Complement rule**: $P(A) = 1 - P(A^c)$ for all events $A$, where $A^c = \{\omega \in \Omega : \omega \notin A\}$
3. **Finite additivity**: If events $\{A_i\}_{i=1}^n$ are disjoint (i.e., $A_i \cap A_j = \emptyset$ for all $i \neq j$), then:
   ```math
   P\left(\bigcup_{i=1}^n A_i\right) = \sum_{i=1}^n P(A_i)
   ```
4. **Countable additivity**: For any disjoint $\{A_i\}_{i=1}^{\infty}$:
   ```math
   P\left(\bigcup_{i=1}^{\infty} A_i\right) = \sum_{i=1}^{\infty} P(A_i)
   ```

## σ-Algebras

### Motivation
On large sample spaces $\Omega$ (e.g., $\Omega = \mathbb{R}$), a formal probability measure may be impossible to construct if **all** subsets of $\Omega$ are defined as events (i.e., if $\mathcal{F} = 2^{\Omega}$).

### Definition
The set of events $\mathcal{F}$ is restricted to a **σ-algebra** (or σ-field) of subsets of $\Omega$ satisfying:

1. $\Omega \in \mathcal{F}$ (possesses intersection identity)
2. If $A \in \mathcal{F}$ then $A^c \in \mathcal{F}$ (closed under complementation)
3. If $A_1, A_2, A_3, ... \in \mathcal{F}$, then $\bigcap_{n=1}^{\infty} A_n \in \mathcal{F}$ (closed under countable intersections)

### Fundamental Probability Space
We have identified a fundamental **probability (measure) space**: $(\Omega, \mathcal{F}, P)$.

**Note**: Equivalently by De Morgan's theorem, can use $\emptyset \in \mathcal{F}$ (union identity) and closed under countable unions instead of conditions 1 and 3.

## Conditional Events

### Conditional Probability
The probability that $A$ occurred **conditioned on** (or "given that") another event $B$ occurred is:
```math
P(A|B) := \frac{P(A \cap B)}{P(B)}
```
where $P(B) > 0$ is assumed.

### Mutual Independence
A group of events $A_1, A_2, ..., A_n$ are **mutually independent** if:
```math
P\left(\bigcap_{i \in I} A_i\right) = \prod_{i \in I} P(A_i) \quad \forall I \subseteq \{1, 2, ..., n\}
```

**Note**: If events $A$ and $B$ are independent and $P(B) > 0$, then $P(A|B) = P(A)$.

### Properties of Conditional Probability
Given that $B$ has occurred with $P(B) > 0$:
- The set of events $\mathcal{F}_B := \{A \cap B : A \in \mathcal{F}\}$ is itself a σ-algebra
- $P(\cdot|B)$ is also a probability measure for $(\Omega, \mathcal{F})$ and $(B, \mathcal{F}_B)$
- On $(\Omega, \mathcal{F})$: $P(A) = 0 \Rightarrow P(A|B) = 0$ for all $A \in \mathcal{F}$

## Random Variables

### Definition
A **random variable** $X$ is a real-valued function with domain $\Omega$:
```math
X: \Omega \to \mathbb{R}
```

So $X(\omega)$ is a real number representing some feature of outcome $\omega$.

### Measurability
For random variables, we are interested in:
```math
P(X \in B) := P(\{\omega \in \Omega : X(\omega) \in B\}) =: P(X^{-1}(B))
```

To ensure the probability space $(\Omega, \mathcal{F}, P)$ can evaluate such probabilities, we define random variables as being **measurable**.

## Borel σ-Algebra on ℝ

### Definition
- Consider contiguous intervals of the real line: $[x, \infty) = \{z \in \mathbb{R} : z \geq x\}$ or $(x,y) = \{z \in \mathbb{R} : x < z < y\}$
- Define $\sigma(\mathcal{A})$ as the **smallest σ-algebra** containing all elements of $\mathcal{A}$
- The **Borel σ-algebra** is: $\mathcal{B} := \sigma(\{[x, \infty) : x \in \mathbb{R}\})$

### Properties
- Singleton sets $\{x\} \in \mathcal{B}$ for all $x \in \mathbb{R}$
- $\mathcal{B} = \sigma(\{(-\infty, x) : x \in \mathbb{R}\}) = \sigma(\{(x,y) : x \leq y, x,y \in \mathbb{Q}\})$
- The Vitali subset of $\mathbb{R}$ is **not** in the Borel σ-algebra: $\mathcal{B} \neq 2^{\mathbb{R}}$
- The cardinality of $\mathcal{B}$ is only that of $\mathbb{R}$

## Measurable Random Variables

### Formal Definition
Random variables are **measurable** with respect to $(\Omega, \mathcal{F})$:
```math
X^{-1}(B) \in \mathcal{F} \quad \forall B \in \mathcal{B}
```
so that $P(X \in B)$ is well-defined for all $B \in \mathcal{B}$.

### Induced Distribution
A random variable $X$ **induces** a probability measure $P_X$ on $(\mathbb{R}, \mathcal{B})$:
```math
P_X(B) := P(X \in B)
```
so that $(\mathbb{R}, \mathcal{B}, P_X)$ is also a probability space.

### Composition Properties
- If $g: \mathbb{R} \to \mathbb{R}$ is $(\mathbb{R}, \mathcal{B})$-measurable and $X$ is a random variable, then $g(X)$ is a random variable
- The **cumulative distribution function (CDF)** of $X$ is: $F_X(x) := P_X((-\infty, x]) = P(X \leq x)$

## Measurable Compositions

If $Y, X$ and $X_1, X_2, X_3, ...$ are all extended random variables, then the following are also random variables:
- $\min\{X, Y\}$, $\max\{X, Y\}$, $XY$, $\mathbf{1}_{\{X \neq 0\}}/X$ where $0/0 := 1$
- $\alpha X + \beta Y$ for all $\alpha, \beta \in \mathbb{R}$
- $\sup_{n \geq 1} X_n$, $\inf_{n \geq 1} X_n$, $\limsup_{n \to \infty} X_n$, $\liminf_{n \to \infty} X_n$

## σ-Algebra Generated by Random Variable

### Definition
```math
\sigma(X) := \sigma(\{X^{-1}(B) : B \in \mathcal{B}\})
```
i.e., the smallest σ-algebra of events for which the random variable $X$ is measurable.

**Note**: $\sigma(X) = \sigma(\{X^{-1}([x, \infty)) : x \in \mathbb{R}\})$

### Information Interpretation
$\sigma(X)$ captures the "information" gained by knowledge of $X(\omega)$ about outcomes $\omega$.

### Examples
- If $X$ is constant then $\sigma(X) = \{\emptyset, \Omega\}$
- If $X = \mathbf{1}_B$ for event $B \in \mathcal{F}$ (Bernoulli distributed), then $\sigma(X) = \{\emptyset, B, B^c, \Omega\}$
- If scalars $a \neq b$, then $Y := a\mathbf{1}_B + b\mathbf{1}_{B^c}$ also indicates whether $B$ or $B^c$ occurred, so $\sigma(X) = \sigma(Y)$

### Doob's Theorem
If $Y$ is $\sigma(X)$-measurable (so that $\sigma(Y) \subseteq \sigma(X)$), then there exists a Borel measurable $g$ such that $Y = g(X)$ a.s.

If $g$ is one-to-one, then $\sigma(Y) = \sigma(X)$.

## Independent Random Variables

### Definition
Random variables $X_1, X_2, ..., X_n$ are **mutually independent** if and only if:
```math
P\left(\bigcap_{i=1}^n \{X_i \in B_i\}\right) = \prod_{i=1}^n P(X_i \in B_i) \quad \forall B_1, ..., B_n \in \mathcal{B}
```

### Joint CDF Characterization
Mutual independence implies that the **joint CDF**:
```math
F_{X_1, X_2, ..., X_n}(x_1, x_2, ..., x_n) := P\left(\bigcap_{i=1}^n \{X_i \leq x_i\}\right)
```
satisfies:
```math
F_{X_1, X_2, ..., X_n}(x_1, x_2, ..., x_n) = \prod_{i=1}^n F_{X_i}(x_i) \quad \forall x_1, ..., x_n \in \mathbb{R}
```

**Note**: The **marginal** $F_{X_1}(x_1) = F_{X_1, ..., X_n}(x_1, \infty, \infty, ..., \infty)$.

## Key Concepts Summary
- **Probability Space**: $(\Omega, \mathcal{F}, P)$ with σ-algebra structure
- **Random Variables**: Measurable functions inducing distributions
- **Borel σ-algebra**: Generated by intervals on real line
- **Independence**: Factorization of joint distributions
- **Information**: Captured by generated σ-algebras

---
*Source: Original PDF - Preliminary Material/prob-theory2.pdf*