# Preliminary Material - Lecture 1: Review of Probability and Random Processes

## Course Information
**Course**: EECS 502 Stochastic Processes  
**Date**: January 19, 2021  
**Lecturer**: Vijay G. Subramanian

## Textbooks
1. P. G. Hoel, S. C. Port and C. J. Stone, "Introduction to stochastic processes," 1986, Waveland Press.
2. P. Brémaud, "Markov chains: Gibbs fields, Monte Carlo simulation, and queues," 2013, Vol. 31, Springer Science & Business Media.

## Mathematical Notation

### Number Systems
1. **Natural numbers**: $\mathbb{N} = \{1, 2, 3, ...\}$
2. **Integers**: $\mathbb{Z} = \{..., -2, -1, 0, 1, 2, ...\}$
3. **Whole numbers**: $\mathbb{Z}^+ = \mathbb{N} \cup \{0\} = \{0, 1, 2, ...\}$ (non-negative integers)
4. **Real numbers**: $\mathbb{R} = (-\infty, \infty)$
5. **Non-negative real numbers**: $\mathbb{R}^+ = [0, +\infty)$

### Intervals on the Real Line
- **Closed interval**: $[a, b] = \{x : a \leq x \leq b\}$
- **Open interval**: $(a, b) = \{x : a < x < b\}$
- **Half-open intervals**: 
  - $(a, b] = \{x : a < x \leq b\}$
  - $[a, b) = \{x : a \leq x < b\}$

## Sets: Open and Closed

### Closed Set $C$
**Definition**: Given a sequence $\{x_i\}_{i=1}^{\infty}$ in $C$ (i.e., $x_i \in C$ for all $i = 1, 2, ...$), if $\lim_{n \to \infty} x_n$ exists, then $\lim_{n \to \infty} x_n \in C$.

**Interpretation**: Taking limits, one cannot escape $C$.

**Example**: A square in $\mathbb{R}^2$ where the edges are included in $C$.

### Open Set $O$
**Definition**: For all $x \in O$, we can find a small enough ball (open interval $(x-\epsilon, x+\epsilon)$) - called neighborhood of $x$ - that is fully contained in $O$.

**Example**: Open circle in $\mathbb{R}^2$: $\{x : \|x\|_2 < 1\} = \{(x_1, x_2) : x_1^2 + x_2^2 < 1\}$

## Probability Spaces

### Components
A probability space consists of $(\Omega, \mathcal{F}, P)$ where:
- $\Omega$: Sample space or space of outcomes
- $\mathcal{F}$: $\sigma$-algebra (or $\sigma$-field) - collection of subsets of $\Omega$
- $\omega$: Sample point or realization where $\omega \in \Omega$
- $P$: Probability distribution that assigns values to elements of $\mathcal{F}$

## Algebras and σ-Algebras

### Algebra
A collection of subsets $\tilde{\mathcal{F}}$ of $\Omega$ is called an **algebra** if:

1. **Non-empty**: Either $\Omega \in \tilde{\mathcal{F}}$ or $\emptyset \in \tilde{\mathcal{F}}$
2. **Closure under complements**: If $F \in \tilde{\mathcal{F}}$, then $F^c \in \tilde{\mathcal{F}}$
3. **Closure under finite unions**: If $A, B \in \tilde{\mathcal{F}}$, then $A \cup B \in \tilde{\mathcal{F}}$

### σ-Algebra
A collection of subsets $\mathcal{F}$ of $\Omega$ is a **σ-algebra** if:

1. It is an algebra
2. **Closure under countable unions**: If $\{A_i\}_{i=1}^{\infty}$ with $A_i \in \mathcal{F}$ for all $i$, then $\bigcup_{i=1}^{\infty} A_i \in \mathcal{F}$

### Examples of Algebras

1. **Trivial σ-algebra**: $\tilde{\mathcal{F}} = \{\emptyset, \Omega\}$

2. **Largest σ-algebra**: $\tilde{\mathcal{F}} = 2^{\Omega} = \mathcal{P}(\Omega)$ (power set)
   - **Single coin toss**: $\Omega = \{H, T\}$, $\tilde{\mathcal{F}} = \{\emptyset, \{H\}, \{T\}, \{H,T\}\}$
   - **Single die**: $\Omega = \{1, 2, 3, 4, 5, 6\}$, $\tilde{\mathcal{F}} = 2^{\Omega}$

3. **Interval algebra**: $\Omega = [0,1]$, $\tilde{\mathcal{F}} = \{\text{all finite unions of intervals}\}$

### Borel σ-Algebra
**Definition**: $\mathcal{B}(\mathbb{R})$ is the smallest σ-algebra that contains all intervals.

**Generation**: For collection $\tilde{G}$ of subsets of $\Omega$, $\sigma(\tilde{G})$ is the smallest σ-algebra containing $\tilde{G}$.

**Examples**:
- $\tilde{G} = \{[a,b] : a, b \in \mathbb{R}\} \Rightarrow \sigma(\tilde{G}) = \mathcal{B}(\mathbb{R})$
- $\tilde{G} = \{O : O \text{ open in } \mathbb{R}\} \Rightarrow \sigma(\tilde{G}) = \mathcal{B}(\mathbb{R})$

## Functions and Inverse Images

### Setup
Let $(\Omega_1, \mathcal{F}_1)$ and $(\Omega_2, \mathcal{F}_2)$ be probability spaces.
Consider function $f: \Omega_1 \to \Omega_2$.

### Inverse Image
For $B \subseteq \Omega_2$:
```math
f^{-1}(B) := \{\omega_1 \in \Omega_1 : f(\omega_1) \in B\}
```

Define $\tilde{G} = \{f^{-1}(B) : B \in \mathcal{F}_2\}$ and obtain $\sigma(\tilde{G})$.

**Key Question**: How does $\sigma(\tilde{G})$ compare to $\mathcal{F}_1$?

## Probability Measures

### Definition
A probability distribution $P: \mathcal{F} \to [0,1]$ satisfies:

1. **Normalized**: $P(\Omega) = 1$
2. **Countably additive**: If $\{A_i\}_{i=1}^{\infty}$ is countable and disjoint with $A_i \in \mathcal{F}$, then:
   ```math
   P\left(\bigcup_{i=1}^{\infty} A_i\right) = \sum_{i=1}^{\infty} P(A_i)
   ```

### Examples

#### 1. Bernoulli Distribution
- $\Omega = \{0, 1\}$, $\mathcal{F} = 2^{\Omega}$
- Given $p \in [0,1]$: $P(\{1\}) = p$, $P(\{0\}) = 1-p$

#### 2. Uniform Distribution on $[0,1]$
- $\Omega = [0,1]$, $\mathcal{F} = \mathcal{B}([0,1])$
- For $0 \leq a \leq b \leq 1$: $P([a,b]) = b - a$
- General: $P(B) = \int_0^1 \mathbf{1}_B(x) dx$ where
  ```math
  \mathbf{1}_B(x) = \begin{cases}
  1 & \text{if } x \in B \\
  0 & \text{otherwise}
  \end{cases}
  ```

#### 3. Normal Distribution
- $\Omega = \mathbb{R}$, $\mathcal{F} = \mathcal{B}(\mathbb{R})$
- Mean $\mu$, variance $\sigma^2 > 0$:
  ```math
  P(B) = \int_{-\infty}^{\infty} \mathbf{1}_B(x) \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(x-\mu)^2}{2\sigma^2}} dx
  ```

## Key Concepts Summary
- **Probability Space**: $(\Omega, \mathcal{F}, P)$
- **σ-algebra**: Collection closed under complements and countable unions
- **Borel σ-algebra**: Generated by intervals/open sets
- **Probability Measure**: Normalized, countably additive function
- **Indicator Function**: $\mathbf{1}_B(x)$ for set membership

---
*Source: Original PDF - Preliminary Material/Lecture1.pdf*