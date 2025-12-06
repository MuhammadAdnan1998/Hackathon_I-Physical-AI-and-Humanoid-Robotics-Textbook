# Week 9 Introduction

## Swarm Robotics

This week, we explore the fascinating field of Swarm Robotics, which draws inspiration from the collective behavior of social insects and other biological systems. Swarm robotics focuses on coordinating large numbers of relatively simple robots to achieve complex tasks that are beyond the capabilities of individual robots.

### Topic 9.1: Emergent Behavior

Emergent behavior is a key characteristic of swarm robotics, where complex, intelligent global behavior arises from the local interactions of individual robots with each other and with their environment, without centralized control.

*   **Local Rules:** Understanding how simple rules applied at the individual robot level can lead to sophisticated collective patterns (e.g., foraging, aggregation, pattern formation).
*   **Decentralized Coordination:** The benefits of decentralized control in terms of robustness, scalability, and flexibility.
*   **Flocking and Swarming Algorithms:** Exploring classic algorithms that produce cohesive group movement.

#### Example: Simplified Boids Algorithm (Flocking Simulation - Python)

The Boids algorithm, created by Craig Reynolds, simulates the flocking behavior of birds. It's a classic example of emergent behavior where complex patterns arise from simple local rules (separation, alignment, cohesion).

```python
import random
import math

class Boid:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def distance_to(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def apply_rules(self, boids, separation_distance=20, alignment_strength=0.05, cohesion_strength=0.01):
        # Rule 1: Separation - steer to avoid crowding local flockmates
        separation_vector_x = 0
        separation_vector_y = 0
        for other in boids:
            if other is not self and self.distance_to(other) < separation_distance:
                separation_vector_x += (self.x - other.x)
                separation_vector_y += (self.y - other.y)

        # Rule 2: Alignment - steer towards the average heading of local flockmates
        avg_vx = 0
        avg_vy = 0
        num_neighbors = 0
        for other in boids:
            if other is not self and self.distance_to(other) < 100: # Arbitrary neighborhood for alignment
                avg_vx += other.vx
                avg_vy += other.vy
                num_neighbors += 1
        if num_neighbors > 0:
            avg_vx /= num_neighbors
            avg_vy /= num_neighbors

        # Rule 3: Cohesion - steer to move towards the average position of local flockmates
        center_of_mass_x = 0
        center_of_mass_y = 0
        num_neighbors_cohesion = 0
        for other in boids:
            if other is not self and self.distance_to(other) < 100: # Arbitrary neighborhood for cohesion
                center_of_mass_x += other.x
                center_of_mass_y += other.y
                num_neighbors_cohesion += 1
        if num_neighbors_cohesion > 0:
            center_of_mass_x /= num_neighbors_cohesion
            center_of_mass_y /= num_neighbors_cohesion

        # Apply forces (simplified)
        self.vx += separation_vector_x * 0.01 # Separation force
        self.vy += separation_vector_y * 0.01

        self.vx += (avg_vx - self.vx) * alignment_strength # Alignment force
        self.vy += (avg_vy - self.vy) * alignment_strength

        self.vx += (center_of_mass_x - self.x) * cohesion_strength # Cohesion force
        self.vy += (center_of_mass_y - self.y) * cohesion_strength

    def update(self, width, height):
        self.x += self.vx
        self.y += self.vy

        # Wrap around edges
        if self.x < 0: self.x += width
        if self.x > width: self.x -= width
        if self.y < 0: self.y += height
        if self.y > height: self.y -= height

        # Limit speed (simplified)
        speed = math.sqrt(self.vx**2 + self.vy**2)
        if speed > 5:
            self.vx = (self.vx / speed) * 5
            self.vy = (self.vy / speed) * 5

# Simulation setup
# boids = []
# for _ in range(50):
#     boids.append(Boid(random.uniform(0, 800), random.uniform(0, 600),
#                      random.uniform(-5, 5), random.uniform(-5, 5)))

# For a real simulation, you'd update boids in a loop and visualize them
# for frame in range(100):
#     for boid in boids:
#         boid.apply_rules(boids)
#     for boid in boids:
#         boid.update(800, 600)
#     # print(f"Frame {frame}: Boid positions and velocities (simplified)")

print("This is a simplified Boids algorithm (flocking simulation).")
print("To run it, you would typically use a visualization library (e.g., Pygame, Matplotlib) to see the emergent behavior.")
print("Uncomment the simulation setup and loop to observe the flocking behavior.")
```

#### Further Resources for Swarm Robotics:

*   [Swarm Robotics (E. Sahin, W. Spears, A. Winfield, J.L. Kube, H. Hamann)](https://link.springer.com/referenceworkentry/10.1007%2F978-0-387-30162-4_147) - *An overview of key concepts in swarm robotics.*
*   [Flocking (Boids) Simulation by Craig Reynolds](https://www.red3d.com/cwr/boids/) - *The original research paper and description of the Boids algorithm.*
*   [Multi-Robot Systems Lab (EPFL)](https://www.epfl.ch/labs/mrs/) - *Research on multi-robot systems and swarm intelligence.*
*   [ROS 2 Multi-Robot Systems](https://docs.ros.org/en/galactic/Concepts/About-Quality-of-Service-Settings.html) - *While not directly about swarm, QoS settings are crucial for multi-robot communication in ROS 2.*

### Topic 9.2: Decentralized Control

Decentralized control is central to swarm robotics, contrasting with traditional robotics where a single controller dictates the actions of one or more robots. In swarm systems, each robot makes decisions based on its local sensor data and communication with neighbors.

*   **Peer-to-Peer Communication:** Strategies for limited-range communication between robots in a swarm.
*   **Leaderless Architectures:** Designing systems where no single robot is designated as the leader, enhancing resilience.
*   **Robustness to Failure:** How decentralized control allows swarms to continue operating effectively even if individual robots fail.
*   **Scalability:** The ability of swarm systems to grow in size without a proportional increase in control complexity.