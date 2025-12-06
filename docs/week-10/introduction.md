# Week 10 Introduction

## Bio-inspired Robotics

This week, we explore Bio-inspired Robotics, a field that draws inspiration from natural systems to design and develop novel robotic solutions. By mimicking the elegant designs and complex behaviors found in biology, engineers can create robots with enhanced locomotion, manipulation, and sensing capabilities.

### Topic 10.1: Legged Robots

Legged robots are designed to emulate the walking, running, and climbing abilities of animals, offering superior mobility over uneven terrain compared to wheeled or tracked robots.

*   **Gaits and Locomotion:** Analyzing different gaits (e.g., trot, gallop, crawl) and the underlying control principles that enable stable and efficient locomotion.
*   **Dynamic Balancing:** Techniques for maintaining balance and stability, particularly in bipedal and quadrupedal robots.
*   **Applications:** Exploring applications in rough terrain exploration, disaster response, and assistance robotics.

#### Example: Simplified Trot Gait Generation (Python)

This Python code provides a simplified conceptual example of how a trot gait might be generated for a quadruped robot. A trot involves diagonally opposite pairs of legs moving in sync.

```python
import random
import math
import numpy as np # Added for linspace

class Boid: # This class is not used in the gait example but was part of the original content.
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

def generate_trot_gait(leg_count, step_height=0.1, step_length=0.2, duration=1.0):
    """
    Generates a simplified trot gait for a quadruped robot.
    In a trot, diagonally opposite legs move simultaneously.

    Args:
        leg_count (int): Number of legs (e.g., 4 for quadruped).
        step_height (float): Max vertical displacement of the foot.
        step_length (float): Horizontal distance covered in one step.
        duration (float): Time taken for one complete gait cycle.

    Returns:
        list: A list of leg movements over time (simplified).
              Each element could represent [leg_id, x_offset, y_offset, z_offset].
    """
    gait_sequence = []
    time_points = np.linspace(0, duration, 100) # 100 steps in one cycle

    # Assuming 4 legs: Front-Left (FL), Rear-Right (RR), Front-Right (FR), Rear-Left (RL)
    # Trot pairs: (FL, RR) and (FR, RL)
    trot_pairs = [(0, 3), (1, 2)] # Example mapping if legs are indexed 0,1,2,3

    for t in time_points:
        # Phase 1: FL and RR move (swing), FR and RL are on the ground (stance)
        if t < duration / 2:
            # Swing phase for FL/RR
            x_swing = -step_length * math.cos(math.pi * t / (duration / 2)) # -step_length to step_length
            z_swing = step_height * math.sin(math.pi * t / (duration / 2)) # 0 to step_height and back to 0
            
            gait_sequence.append([trot_pairs[0][0], x_swing, 0, z_swing]) # FL leg
            gait_sequence.append([trot_pairs[0][1], x_swing, 0, z_swing]) # RR leg
            
            # Stance phase for FR/RL (simplified: no movement)
            gait_sequence.append([trot_pairs[1][0], 0, 0, 0]) # FR leg
            gait_sequence.append([trot_pairs[1][1], 0, 0, 0]) # RL leg
            
        # Phase 2: FR and RL move (swing), FL and RR are on the ground (stance)
        else:
            # Adjust time for the second half of the cycle
            t_phase2 = t - (duration / 2)
            x_swing = -step_length * math.cos(math.pi * t_phase2 / (duration / 2))
            z_swing = step_height * math.sin(math.pi * t_phase2 / (duration / 2))
            
            gait_sequence.append([trot_pairs[1][0], x_swing, 0, z_swing]) # FR leg
            gait_sequence.append([trot_pairs[1][1], x_swing, 0, z_swing]) # RL leg
            
            # Stance phase for FL/RR
            gait_sequence.append([trot_pairs[0][0], 0, 0, 0]) # FL leg
            gait_sequence.append([trot_pairs[0][1], 0, 0, 0]) # RR leg
            
    return gait_sequence

# Example usage (simplified output):
# gait = generate_trot_gait(4)
# print(f"Generated {len(gait)} gait steps for a 4-legged robot (first few steps):")
# for i in range(min(5, len(gait))):
#     print(f"  Step {i}: Leg {gait[i][0]} moves to ({gait[i][1]:.2f}, {gait[i][2]:.2f}, {gait[i][3]:.2f})")

print("This code provides a simplified conceptual example of generating a trot gait for a quadruped robot.")
print("Actual robot gait generation involves complex inverse kinematics, dynamics, and trajectory optimization.")
print("For visualization and practical application, this would be integrated into a robot simulator or controller.")
```

#### Further Resources for Bio-inspired Robotics:

*   [Biologically Inspired Robotics (MIT OpenCourseware)](https://ocw.mit.edu/courses/mechanical-engineering/2-167-biologically-inspired-robotics-fall-2005/) - *Course materials for bio-inspired robotics.*
*   [Dynamic Locomotion (ANYmal Research)](https://www.leggedrobotics.ethz.ch/research/dynamic-locomotion) - *Research from ETH Zurich on dynamic locomotion of legged robots.*
*   [Soft Robotics Toolkit (Harvard University)](https://softroboticstoolkit.com/) - *Resources for designing, fabricating, and modeling soft robots.*
*   [Bionics Learning Network](https://www.festo.com/group/en/cms/10233.htm) - *Festo's initiatives in bio-inspired automation.*

### Topic 10.2: Soft Robotics

Soft robotics is a subfield of robotics that deals with the design, control, and fabrication of robots from highly compliant materials, similar to biological organisms. Unlike traditional rigid robots, soft robots can deform, stretch, and twist, offering unique advantages.

*   **Compliant Materials:** Utilizing elastomers, gels, and other soft materials to create flexible robot bodies and actuators.
*   **Soft Actuators:** Designing actuators that leverage fluidic (pneumatic, hydraulic) or dielectric elastomer principles to achieve motion.
*   **Safe Interaction:** How the inherent compliance of soft robots makes them safer for human interaction and delicate object manipulation.
*   **Biomimicry in Soft Robots:** Examples of soft robots inspired by octopuses, worms, and other soft-bodied creatures.