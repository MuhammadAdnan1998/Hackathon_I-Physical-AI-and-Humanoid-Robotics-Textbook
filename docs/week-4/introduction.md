# Week 4 Introduction

## Localization and Mapping

This week, we explore two fundamental challenges in robotics: localization and mapping. Localization is the process of determining a robot's position and orientation within a given map, while mapping is the process of creating such a map of the environment. Often, these two problems are tackled simultaneously in what is known as Simultaneous Localization and Mapping (SLAM).

### Topic 4.1: SLAM Algorithms

Simultaneous Localization and Mapping (SLAM) is a computational problem of constructing or updating a map of an unknown environment while simultaneously keeping track of an agent's location within it. We will cover various SLAM algorithms, including:

*   **Extended Kalman Filter (EKF) SLAM:** A probabilistic approach that uses Kalman filters to estimate the robot's pose and the map features.
*   **Particle Filter (FastSLAM):** Uses a set of particles to represent the robot's pose distribution, making it suitable for non-linear systems.
*   **Graph-Based SLAM:** Represents the robot's trajectory and map features as a graph, where nodes are robot poses and features, and edges are spatial constraints.

#### Example: Simple 1D Kalman Filter Update (Python)

Let's illustrate the measurement update step of a 1D Kalman filter. We have a noisy sensor measurement and a prior estimate of our state.

```python
import numpy as np

def kalman_update_1d(mu_prev, sigma_prev, z, R):
    """
    Performs the measurement update step of a 1D Kalman Filter.

    Args:
        mu_prev (float): Prior mean (estimate of the state before measurement).
        sigma_prev (float): Prior variance (uncertainty of the state before measurement).
        z (float): Current sensor measurement.
        R (float): Measurement noise variance.

    Returns:
        tuple: (mu_new, sigma_new) - Updated mean and variance.
    """
    # Kalman Gain
    K = sigma_prev / (sigma_prev + R)

    # Updated Mean
    mu_new = mu_prev + K * (z - mu_prev)

    # Updated Variance
    sigma_new = (1 - K) * sigma_prev

    return mu_new, sigma_new

# Example usage:
# Prior estimate of position (mean and variance)
prior_mu = 10.0
prior_sigma = 1.0

# Sensor measurement and its noise variance
measurement_z = 10.2
measurement_noise_R = 0.1

updated_mu, updated_sigma = kalman_update_1d(prior_mu, prior_sigma, measurement_z, measurement_noise_R)

print(f"Prior estimate: mu={prior_mu:.2f}, sigma={prior_sigma:.2f}")
print(f"Measurement: z={measurement_z:.2f}, R={measurement_noise_R:.2f}")
print(f"Updated estimate: mu_new={updated_mu:.2f}, sigma_new={updated_sigma:.2f}")
```

#### Further Resources for SLAM and Probabilistic Robotics:

*   [Probabilistic Robotics (Sebastian Thrun et al.)](https://www.probabilistic-robotics.org/) - *The foundational textbook for probabilistic methods in robotics.*
*   [Cyrill Stachniss - SLAM Course (YouTube)](https://www.youtube.com/playlist?list=PLgnQpQtFTOGR5i4jFNqWf8oJ_v_w7y4qA) - *Excellent video lecture series on SLAM.*
*   [ROS Navigation Stack Documentation](https://docs.ros.org/en/galactic/Concepts/Navigation2/Navigation2-Overview.html) - *Details on how localization and mapping are integrated into ROS 2 navigation.*

### Topic 4.2: Probabilistic Robotics

Probabilistic robotics deals with the problem of how robots can cope with uncertainty in their perception and action. All measurements and actions are inherently uncertain due to noise and inaccuracies. Probabilistic methods provide a robust framework for reasoning about and managing this uncertainty.

*   **Bayes' Rule:** The cornerstone of probabilistic robotics, used to update beliefs about the robot's state given new observations.
*   **Gausian Distributions:** Commonly used to model uncertainty in robot states and sensor measurements.
*   **Markov Localization:** A technique for robot localization that uses the Markov assumption to track the robot's pose over time.