# Preliminary Material - Lecture 2: Random Variables and Probability Theory

## Course Information
**Course**: EECS 502 Stochastic Processes  
**Date**: January 14, 2020  
**Lecturer**: Vijay G. Subramanian  
**Scribes**: Xupeng Wei

## Random Variables

### Definition
**Random Variable**: $X: \Omega \to \mathbb{R}$ that is measurable.

### Measurability Condition
For the Borel σ-algebra $\mathcal{B}(\mathbb{R})$:

For all $B \in \mathcal{B}(\mathbb{R})$, find $X^{-1}(B) = \{\omega \in \Omega : X(\omega) \in B\}$ (inverse map).

Let $\tilde{G} = \{X^{-1}(B) : B \in \mathcal{B}(\mathbb{R})\}$ - collection of subsets of $\Omega$.

**Key Question**: Is $\tilde{G} \subseteq \mathcal{F}$?

**Answer**: If yes, then $X$ is measurable and a random variable.

**Equivalent Statement**: For all $B \in \mathcal{B}(\mathbb{R})$, $X^{-1}(B) \in \mathcal{F}$.

### Generated σ-Algebra
$\sigma(\tilde{G})$ = smallest σ-algebra that contains $\tilde{G}$.

$X$ is a random variable if and only if $\sigma(\tilde{G}) \subseteq \mathcal{F}$.

### Induced Distribution
For a random variable $X$, the induced distribution is defined on each $B \in \mathcal{B}(\mathbb{R})$ by:
```math
P_X(B) = P(X \in B) = P(X^{-1}(B))
```
since $X^{-1}(B) \in \mathcal{F}$.

## Generalization to Other Spaces

### Random Variables in General Spaces
```math
X: \Omega_1 \to \Omega_2
```
where $(\Omega_1, \mathcal{F}_1, P)$ and $(\Omega_2, \mathcal{F}_2)$ are probability spaces.

$X$ is a random variable if it is a measurable map:
```math
\forall B \in \mathcal{F}_2, \quad X^{-1}(B) \in \mathcal{F}_1
```

**Examples**: $\mathbb{R}^2$, $\mathbb{R}^3$, etc.

## Examples

### Example 1: Uniform Distribution
- $\Omega = [0,1]$, $\mathcal{F} = \mathcal{B}([0,1])$, $P$ = uniform distribution
- For $[a,b] \subseteq [0,1]$: $P([a,b]) = b - a$
- For $B \in \mathcal{B}([0,1])$: $P(B) = \int_0^1 \mathbf{1}_B(x) dx$

### Example 2: Binary Expansion
- $\Omega = \{0,1\}^{\infty}$, $\omega = \omega_1\omega_2\omega_3...$
- Binary expansion: $0.\omega_1\omega_2\omega_3...$
- Suppose $0.1000...$ with probability $\frac{1}{2}$, or $0.0111...$ with probability $\frac{1}{2}$
- Define $X: \Omega \to \{0,1\}$, $X(\omega) = \omega_1$
- $\Omega_2 = \{0,1\}$, $\mathcal{F}_2 = 2^{\{0,1\}} = \{\emptyset, \{0\}, \{1\}, \{0,1\}\}$
- Induced measure: $P_X(X = 0) = \frac{1}{2} = P_X(X = 1)$
- $X$ is a Bernoulli random variable

### Example 3: Decimal Expansion
- $\Omega = [0,1]$, $\mathcal{F} = \mathcal{B}([0,1])$, $P$ = uniform distribution
- $X: \Omega \to \{0,1,...,9\}$, $\omega \mapsto 0.\omega_1\omega_2\omega_3...$
- $X(\omega) = \omega_1$, $\Omega_2 = \{0,...,9\}$ contains all subsets
- $P_X(X = 0) = P_X(X = 1) = ... = P_X(X = 9) = \frac{1}{10}$

### Example 4: Exponential Distribution
- $X(\omega) = -\log(\omega)$, $\Omega = [0,1]$
- Space of $X(\omega)$ is $\mathbb{R}^+$, $\mathcal{B}(\mathbb{R}^+)$ is the σ-algebra
- Cumulative distribution function:
  ```math
  \begin{align}
  F_X(x) &= P_X(X \in [0,x]) \\
  &= P(X^{-1}([0,x])) \\
  &= P([e^{-x}, 1]) \\
  &= 1 - e^{-x}
  \end{align}
  ```
- This is the exponential distribution with parameter 1

### Example 5: Two-Bit System
- $\Omega = \{0,1\}^2$ = $\{(0,0), (0,1), (1,0), (1,1)\}$
- $\mathcal{F} = 2^{\Omega}$ (power set), $P$ = uniform on $\Omega$
- Define:
  - $X(\omega)$ = first bit
  - $Y(\omega)$ = second bit  
  - $Z(\omega) = X(\omega) \oplus Y(\omega)$ (XOR)
- All take values in $\{0,1\} = \Omega_2$, $\mathcal{F}_2 = 2^{\{0,1\}}$

**Inverse Images**:
- $X^{-1}(\{0\}) = \{(0,0), (0,1)\}$, $X^{-1}(\{1\}) = \{(1,0), (1,1)\}$
- $Y^{-1}(\{0\}) = \{(0,0), (1,0)\}$, $Y^{-1}(\{1\}) = \{(0,1), (1,1)\}$
- $Z^{-1}(\{0\}) = \{(0,0), (1,1)\}$, $Z^{-1}(\{1\}) = \{(0,1), (1,0)\}$

**Generated σ-algebra**: $\sigma(X) = \{\emptyset, \{(0,0), (0,1)\}, \{(1,0), (1,1)\}, \Omega\}$

This is strictly smaller than $2^{\Omega}$ (e.g., $\{(0,0)\} \in 2^{\Omega}$ but $\{(0,0)\} \notin \sigma(X)$).

### Example 6: Indicator Random Variable
- $\Omega = [0,1]$, $\mathcal{F} = \mathcal{B}([0,1])$
- Define:
  ```math
  Z(\omega) = \begin{cases}
  0 & \text{if } \omega \in [0, 0.5) \\
  1 & \text{if } \omega \in [0.5, 1]
  \end{cases}
  ```
- $\sigma(Z) = \{\emptyset, [0, 0.5), [0.5, 1], [0,1]\}$

## Key Concepts Summary
- **Random Variable**: Measurable function from probability space to measurable space
- **Measurability**: Inverse images of measurable sets are measurable
- **Induced Distribution**: Distribution on target space induced by random variable
- **Generated σ-algebra**: Smallest σ-algebra making the function measurable
- **Discrete vs Continuous**: Power set vs Borel σ-algebra

---
*Source: Original PDF - Preliminary Material/Lecture2.pdf*