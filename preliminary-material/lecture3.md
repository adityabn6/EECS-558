# Preliminary Material - Lecture 3: Stochastic Processes and π-Systems

## Course Information
**Course**: EECS 502 Stochastic Processes  
**Date**: January 16, 2020  
**Lecturer**: Vijay G. Subramanian  
**Scribes**: Kang Gong

## π-Systems and Probability Distributions

### Definition: π-System
**Definition**: A collection $\mathcal{S}$ of subsets of $\Omega$ is a **π-system** if it is closed under finite intersection.

### Fundamental Theorem
**Theorem**: Given two probability distributions $P_1$ and $P_2$ such that they are the same on a π-system $\mathcal{S}$, then they are also the same on $\sigma(\mathcal{S})$.

**Formally**: If $\forall A \in \mathcal{S}, P_1(A) = P_2(A)$, then $\forall B \in \sigma(\mathcal{S}), P_1(B) = P_2(B)$.

**Remark**: This theorem means that specifying the values on a π-system uniquely specifies the probability distribution on the smallest σ-algebra containing it.

### Example 1: Real Line
- $\Omega = \mathbb{R}$
- $\mathcal{S} = \{(-\infty, x] : x \in \mathbb{R}\}$
- $\mathcal{S}$ is a π-system since if $x_1 > x_2$:
  ```math
  (-\infty, x_1] \cap (-\infty, x_2] = (-\infty, x_2] \in \mathcal{S}
  ```
- $P_X((-\infty, x]) = F_X(x)$ is the CDF for random variable $X$

### Example 2: Random Processes
**Setup**: Random processes $\{X_t\}_{t \in \mathbb{R}}$ all take values in $\mathbb{R}$.

**π-system Construction**:
- Consider Borel σ-algebra $\mathcal{B}(\mathbb{R})$
- π-system: $\{B_{t_i} : B_{t_i} \in \mathcal{B}(\mathbb{R})\}$
- Can also use $\{B_{t_i} : B_{t_i} = (-\infty, x] \forall x \in \mathbb{R}\}$

**Finite-Dimensional Distributions**:
Let $B_n = \prod_{i=1}^n B_{t_i}$ where $\prod$ means Cartesian product.

For $x = (x_1, ..., x_n) \in B_n \Rightarrow x_i \in B_{t_i}$ for any $i$.

The smallest σ-algebra containing such a π-system is the Borel σ-algebra.

**Key Result**: For all $t_1 < t_2 < ... < t_n \in \mathbb{R}$ and all $n \in \mathbb{N}$:
```math
P(B_n) = P(X_{t_1} \in B_{t_1}, ..., X_{t_n} \in B_{t_n})
```

**Conclusion**: Specifying all finite-dimensional marginals is equivalent to specifying the distribution of the random process. This specifies the joint CDF for all finite-dimensional collections.

## Stationarity

### Strict Stationarity
**Definition**: A process $\{X_t : t \in \mathbb{R}\}$ is **(strictly) stationary** if for any finite set of indices $t_1 < t_2 < ... < t_n \in \mathbb{R}$ and any $\tau \in \mathbb{R}$:

```math
P(X_{t_1} \in B_1, X_{t_2} \in B_2, ..., X_{t_n} \in B_n) = P(X_{t_1+\tau} \in B_1, X_{t_2+\tau} \in B_2, ..., X_{t_n+\tau} \in B_n)
```

**Interpretation**: Any time shifts don't change the distribution of the process.

**Example**: Let $\{X_n\}_{n \in \mathbb{Z}}$ be i.i.d. Bernoulli($\frac{1}{2}$) random variables. This is a stationary process.

### Consequences of Strict Stationarity

**Consequence 1**: $P(X_t \in B)$ for all $B \in \mathcal{B}(\mathbb{R})$ is independent of $t$.
- $F_{X_t}(x)$ is independent of $t$
- $\mu_t = E[X_t]$ is independent of $t$ (if it exists)

**Consequence 2**: $P(X_t \in B_1, X_s \in B_2) = P(X_{t-s} \in B_1, X_0 \in B_2)$ is a function of $(t-s)$.
- So are the covariance $E[X_t X_s]$ and the correlation function $E[(X_t - \mu_t)(X_s - \mu_s)] = R_X(t-s)$

### Wide-Sense Stationarity
**Definition**: A process $\{X_t\}_{t \in \mathbb{R}}$ is **wide-sense stationary (WSS)** if:

1. $\mu_t \triangleq E[X_t] \equiv \mu$ (not a function of $t$)
2. $R_X(t,s) \triangleq E[(X_t - \mu_t)(X_s - \mu_s)] = R_X(t-s)$

**Remark**: 
- Strict stationary process is also WSS
- The reverse is only true for Gaussian processes

## Independence

### Definition: Independence
**Definition**: $X_1$ and $X_2$ are **independent** if:

**Joint Distribution**: 
```math
P(X_1 \in B_1, X_2 \in B_2) = P(X_1 \in B_1) P(X_2 \in B_2) \quad \forall B_1, B_2 \in \mathcal{B}(\mathbb{R})
```

## Key Concepts Summary

### π-Systems
- **Purpose**: Efficient way to specify probability distributions
- **Property**: Closed under finite intersections
- **Power**: Uniquely determines distribution on generated σ-algebra

### Stationarity
- **Strict**: All finite-dimensional distributions invariant under time shifts
- **Wide-Sense**: Mean constant, covariance depends only on time difference
- **Relationship**: Strict ⟹ WSS, equality for Gaussian processes

### Random Processes
- **Characterization**: Finite-dimensional distributions
- **π-system approach**: Efficient specification method
- **Applications**: Foundation for stochastic control theory

---
*Source: Original PDF - Preliminary Material/Lecture3.pdf*