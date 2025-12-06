# Week 7 Introduction

## Reinforcement Learning for Robotics

This week, we dive into the exciting field of Reinforcement Learning (RL) and its applications in robotics. RL is a powerful machine learning paradigm where an agent learns to make decisions by interacting with an environment to maximize a cumulative reward. This approach is particularly well-suited for tasks where explicit programming is difficult or impossible.

### Topic 7.1: Q-Learning and Policy Gradients

We will explore two foundational algorithms in reinforcement learning:

*   **Q-Learning:** A value-based RL algorithm that learns an action-value function (Q-function) which gives the expected utility of taking a given action in a state. We will cover the Bellman equation and how Q-learning iteratively updates Q-values.
*   **Policy Gradients:** A class of policy-based RL algorithms that directly optimize a parameterized policy by estimating the gradient of the expected reward with respect to the policy parameters. This is often more suitable for continuous action spaces found in robotics.

#### Example: Simple Q-Learning in 1D (Python)

```python
import numpy as np

# Simple Q-learning example in a 1D environment
# States: 0, 1, 2, 3, 4 (e.g., positions)
# Actions: 0 (move left), 1 (move right)

# Q-table initialization (state x action)
# Here, 5 states and 2 actions
q_table = np.zeros((5, 2))

# Rewards (e.g., reaching state 4 is good)
rewards = np.array([-1, -1, -1, -1, 10]) # -1 for non-goal states, 10 for goal state 4

# Parameters
learning_rate = 0.1
discount_factor = 0.9
epsilon = 0.1 # For epsilon-greedy policy

def choose_action(state):
    if np.random.uniform(0, 1) < epsilon:
        return np.random.choice([0, 1]) # Explore
    else:
        return np.argmax(q_table[state, :]) # Exploit

def take_action(state, action):
    if action == 0: # Move left
        next_state = max(0, state - 1)
    else: # Move right
        next_state = min(4, state + 1)
    reward = rewards[next_state]
    return next_state, reward

# Training loop
num_episodes = 100

print("Q-Learning Training:")
for episode in range(num_episodes):
    current_state = np.random.choice(5) # Start from a random state
    done = False
    
    while not done:
        action = choose_action(current_state)
        next_state, reward = take_action(current_state, action)
        
        # Q-Learning update rule
        q_table[current_state, action] = q_table[current_state, action] + \
                                          learning_rate * (reward + discount_factor * np.max(q_table[next_state, :]) - \
                                                            q_table[current_state, action])
        current_state = next_state
        
        if current_state == 4: # Goal state
            done = True
            
    if episode % 20 == 0:
        print(f"Episode {episode}, Q-table:\n{q_table.round(2)}")

print("\nFinal Q-table after training:\n", q_table.round(2))

# Test learned policy
print("\nTesting learned policy (starting from state 0):")
current_state = 0
path = [current_state]
while current_state != 4:
    action = np.argmax(q_table[current_state, :])
    current_state, _ = take_action(current_state, action)
    path.append(current_state)
print("Path:", path)
```

#### Further Resources for Reinforcement Learning:

*   [Reinforcement Learning: An Introduction (Richard S. Sutton and Andrew G. Barto)](http://www.incompleteideas.net/book/the-book-2nd.html) - *The foundational textbook for reinforcement learning.*
*   [ spinningup.openai.com](https://spinningup.openai.com/en/latest/) - *A resource designed to help anyone learn to develop high-quality code for deep reinforcement learning.*
*   [PyTorch Reinforcement Learning Examples](https://pytorch.org/tutorials/intermediate/reinforcement_q_learning.html) - *Practical examples of RL implementation using PyTorch.*
*   [NVIDIA Isaac Sim Reinforcement Learning Documentation](https://docs.omniverse.nvidia.com/app_isaacsim/app_isaacsim/tutorial_rl_basic_intro.html) - *Specific documentation on using RL within the Isaac Sim environment.*

### Topic 7.2: Sim-to-Real Transfer

One of the significant challenges in applying RL to robotics is the "reality gap"—thediscrepancy between simulations and the real world. Sim-to-Real Transfer addresses this by enabling policies learned in simulation to be effectively deployed on physical robots.

*   **Domain Randomization:** Randomizing parameters in simulation (e.g., friction, mass, sensor noise) to make the learned policy robust to real-world variations.
*   **Domain Adaptation:** Techniques that adapt the learned policy from simulation to the real world, often using a small amount of real-world data.
*   **Hardware in the Loop (HIL) Simulation:** Integrating real robot hardware into the simulation loop to bridge the reality gap.