# Lecture 2 - August 27: Models of Stochastic Dynamical Systems

## General Model of Stochastic Dynamical Systems (SDS)

### System Components
**State Evolution**:
```math
X_{t+1} = f_t(X_t, U_t, W_t)
```

**Observation Equation**:
```math
Y_t = h_t(X_t, V_t)
```

**Variables**:
- $\{X_t\}$: System state sequence
- $\{Y_t\}$: Observation sequence  
- $\{U_t\}$: Control action sequence
- $\{W_t, V_t\}$: Primitive random variables (not under our control)

### Example: Queueing System
**Arrival Process**: $\{A_t\}$ - arrival sequence of jobs
- $A_t \in \{0, 1, 2, ...\}$ - number of jobs arriving at time $t$

**Service Process**: $\{W_t\}$ - service sequence at servers
- $W_t$ - amount of work completed at time $t$

**System State**: $X_t$ - number of jobs in each queue
- $X_t = (X_t^{(1)}, X_t^{(2)}, ...)$ where $X_t^{(i)}$ is queue length at server $i$

**State Evolution**:
```math
X_{t+1}^{(i)} = \max(X_t^{(i)} + A_t^{(i)} - W_t^{(i)}, 0)
```

**Perfect Observations**: $Y_t = X_t$

## Control Strategies/Laws/Policies

### Open Loop Control
**Definition**: Control sequence determined at time 0, independent of system evolution

```math
U_t = g_t \quad \text{for } t = 0, 1, 2, ..., T-1
```

**Characteristics**:
- Control sequence $\{U_0, U_1, ..., U_{T-1}\}$ fixed at start
- Independent of system state evolution
- No feedback from observations

**System Evolution under Open Loop**:
```math
\begin{align}
X_0 &= \text{given} \\
X_1 &= f_0(X_0, U_0, W_0) \\
X_2 &= f_1(X_1, U_1, W_1) \\
&\vdots \\
X_t &= f_{t-1}(X_{t-1}, U_{t-1}, W_{t-1})
\end{align}
```

### Feedback Control Laws
**Definition**: Control action depends on available information at each time

```math
U_t = \gamma_t(I_t)
```

where $I_t$ is the information available at time $t$.

**Information Structure**:
- **Perfect State Information**: $I_t = \{X_0, X_1, ..., X_t, U_0, U_1, ..., U_{t-1}\}$
- **Perfect Observation**: $I_t = \{Y_0, Y_1, ..., Y_t, U_0, U_1, ..., U_{t-1}\}$

## Equivalence for Deterministic Systems

### Theorem: Open Loop vs Feedback Equivalence
**For deterministic systems** (no random variables $W_t, V_t$), **feedback control laws and open loop control laws are equivalent**.

**Proof**:
1. **Open Loop → Feedback**: Given open loop sequence $\{U_0^*, U_1^*, ..., U_{T-1}^*\}$
   
   Define feedback law: $\gamma_t(X_t) = U_t^*$ for all $X_t$
   
   This produces the same control sequence.

2. **Feedback → Open Loop**: Given feedback law $\gamma_t(X_t)$
   
   Since system is deterministic, $X_t$ is known at time 0:
   ```math
   \begin{align}
   X_0 &= \text{given} \\
   U_0 &= \gamma_0(X_0) \\
   X_1 &= f_0(X_0, U_0) \\
   U_1 &= \gamma_1(X_1) \\
   &\vdots
   \end{align}
   ```
   
   Define open loop: $U_t^* = \gamma_t(X_t)$ where $X_t$ is computed as above.

### Why Feedback is Richer for Stochastic Systems
**Feedback control laws can generate a richer set of system trajectories** because they can adapt to random realizations.

## Key Difference: SDS vs Deterministic Systems

### Markov Property in Deterministic Systems
For deterministic systems:
```math
X_{t+1} = f_t(X_t, U_t)
```

**Sufficient Statistic**: Knowing state $X_t$ at time $t$ is sufficient to determine future evolution.

**Knowledge of past** $\{X_0, X_1, ..., X_{t-1}, U_0, U_1, ..., U_{t-1}\}$ **gives no additional advantage**.

### Breakdown for Stochastic Systems
For stochastic systems, the Markov property may not hold for control purposes.

**Question**: Is $E[X_{t+1} | I_t] = E[X_{t+1} | X_t, U_t]$?

**Answer**: Not necessarily!

**Counter-example**: If $U_t$ is a function of $\{W_0, W_1, ..., W_{t-1}, V_0, V_1, ..., V_{t-1}\}$, then:
- **LHS**: $E[X_{t+1} | X_t, U_t, \text{past info}]$  
- **RHS**: $E[X_{t+1} | X_t, U_t]$

These may not be equal because $U_t$ contains information about past disturbances.

### When Markov Property Holds
**Assumption A1**: $W_t$ and $V_t$ are independent of $\{W_0, ..., W_{t-1}, V_0, ..., V_{t-1}, U_0, ..., U_{t-1}\}$

Under A1:
```math
E[X_{t+1} | X_t, U_t] = E[f_t(X_t, U_t, W_t) | X_t, U_t] = E[f_t(X_t, U_t, W_t)]
```

This **is** a function of $(X_t, U_t)$ only, so the Markov property holds for control.

## Linear Example with Perfect Observations

### System Model
```math
X_{t+1} = X_t + U_t + W_t
```

where $\{W_t\}$ are i.i.d. Gaussian random variables.

**Question**: Can any feedback control law generate trajectories that no open loop law can?

**Answer**: Yes! 

**Example**: Consider feedback law $U_t = -W_t$ (if $W_t$ were observable)
- This would make $X_{t+1} = X_t$ (perfect regulation)
- No open loop sequence can achieve this for all realizations

## Summary
- **Deterministic systems**: Open loop ≡ Feedback control
- **Stochastic systems**: Feedback control is strictly more powerful
- **Markov property**: May not hold for stochastic control problems
- **Information structure**: Critical for determining optimal policies

---
*Source: Original PDF - Lecture Notes/Lecture2_August27.pdf*