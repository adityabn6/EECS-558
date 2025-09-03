# Lecture 1 - August 25: Introduction to Stochastic Control

## Course Overview
**ECE 558: Stochastic Control**
- **Focus**: Centralized Stochastic Control
- **System Type**: Stochastic dynamical systems with one controller
- **Information Structure**: Controller has perfect recall
- **Approach**: Structural and foundational aspects with algorithmic ideas

## Related Courses
- **CSE 598** (Satinder Banja, FA 2025): Reinforcement Learning (RL)
- **ECE 602** (Lei Ying, WN 2026): RL focus

## Applications of Stochastic Control

### 1. Scheduling in Cloud Systems
**Problem**: Data centers with many servers
- **Challenge**: Dispatcher handles millions of jobs
- **Uncertainty**: Service times are stochastic/random
- **Objective**: Minimize delay in server queues
- **Information**: Dispatcher sees full state, knows server capacities
- **Decision**: Based on job type, send job to specific server
- **Framework**: Markov Decision Process (MDP)

**Information Constraints**:
- Sending information is costly
- Dispatcher polls fixed number of servers → Partial observability
- **Framework**: Partially Observable MDP (POMDP)

**Constraint Types**:
- **Soft constraint**: Meet on average
- **Hard constraint**: Never allowed to exceed
- **Framework**: Constrained MDPs, POMDPs

### 2. Autonomous Vehicle/Spacecraft Control
**Problem**: Controlling trajectory of spacecraft, autonomous car, or robot
- **Known state**: MDP with state feedback
- **Sensor-based**: POMDP with output feedback

### 3. Portfolio Management
**Setup**:
- Have money on day k: $X_t$
- K instruments to choose from
- Choose distribution over K options

**Dynamics**:
- Often get $X_t$ amount of money
- Stochastic outcome function of market behavior
- **Goal**: Over T periods, maximize wealth at end while minimizing chance of bankruptcy

### 4. Hypothesis Testing
**Problem**: Compare 2 images to find differences
- **Challenge**: Small differences, unknown model
- **Goal**: Tell apart images if different, identify differences quickly
- **Strategy**: Take different views at different granularities
- **Decision**: High resolution on small region vs low resolution over bigger region
- **Adaptive**: Choose resolution/region based on past choices and results

### 5. Queueing Network Control
**Setup**:
- Two queues: Q₁, Q₂
- Service rates: μ₁, μ₂
- Cost per customer per unit of operation
- Network operates until time T
- State: Occupancy of each queue at time t

**Control Problem**:
- Route jobs to Q₁ or Q₂
- **Goal**: Find routing policy that minimizes expected total cost

## State and Action Spaces

### State Information
- **Present state values**: A₁, A₂, ..., Aₙ
- **Past action values**: Controller uses all past information
- **Perfect recall**: Controller remembers all history

### Complexity Issues
- **State space size**: Can be exponentially large
- **Function space**: Number of possible policies grows exponentially
- **Solution approach**: Dynamic Programming (DP) breaks time dependence

## General Framework

### System Model
**State Evolution**:
```math
X_{t+1} = f(X_t, U_t, W_t)
```

**Observation**:
```math
Y_t = h(X_t, V_t)
```

Where:
- $X_t$: State at time t
- $U_t$: Control action at time t  
- $W_t$: Process noise
- $Y_t$: Observation at time t
- $V_t$: Observation noise

**Cost Function**:
```math
\text{Cost at time } t: g(X_t, U_t)
```

**Objective**:
```math
\text{Minimize: } E\left[\sum_{t=0}^{T-1} g(X_t, U_t) + \Phi(X_T)\right]
```

## Course Scope

### Covered Topics
- **Time**: Discrete time
- **State space**: Discrete or continuous
- **Information**: Perfect recall controller
- **Control**: Single controller problems

### Not Covered
- Continuous time problems
- Multi-controller problems (conceptually more demanding)
- Team problems
- Game theory (though same ideas apply)

## Key Concepts
- **MDP**: Markov Decision Process
- **POMDP**: Partially Observable MDP
- **Perfect Recall**: Controller remembers all past information
- **Dynamic Programming**: Method to solve optimal control problems
- **Stochastic Control**: Control of systems with random disturbances

---
*Source: Original PDF - Lecture Notes/Lecture1_August25.pdf*