# Week 5 Introduction

## Motion Planning

This week, we will focus on motion planning, a critical area in robotics that deals with finding a sequence of valid robot configurations that moves the robot from a start configuration to a goal configuration while avoiding obstacles. Motion planning algorithms are essential for autonomous navigation and manipulation tasks.

### Topic 5.1: Configuration Space

The concept of Configuration Space (C-space) is fundamental to motion planning.

*   **Definition:** C-space is a representation of all possible positions and orientations of a robot. Each point in C-space corresponds to a unique configuration of the robot.
*   **Obstacle C-space:** We will learn how to map physical obstacles from the robot's workspace into C-space, creating "C-obstacles" that the robot must avoid.
*   **C-space Dimensionality:** Understanding how the number of degrees of freedom of a robot affects the complexity of its C-space.

### Topic 5.2: Sampling-Based Planners

Sampling-based planners are a class of motion planning algorithms that explore the C-space by randomly sampling configurations and connecting them to build a roadmap or tree. These methods are particularly effective for high-dimensional C-spaces and complex environments.

*   **Probabilistic Roadmap (PRM):** Constructs a roadmap by randomly sampling configurations and connecting them with collision-free paths. The roadmap is then searched for a path between the start and goal.
*   **Rapidly-exploring Random Tree (RRT):** Builds a tree by incrementally extending random samples towards unexplored regions of the C-space. Variants like RRT* optimize the path quality.
*   **Applications:** Discussing practical applications of sampling-based planners in autonomous vehicles, robot arms, and humanoid robots.

#### Example: Simple Path Smoothing (Python)

```python
def smooth_path(path, weight_data=0.5, weight_smooth=0.1, tolerance=0.0001):
    """
    Applies a simple path smoothing algorithm to a 2D path.
    The algorithm iteratively adjusts path points to be closer to both
    the original data points and the smoothed neighbors.

    Args:
        path (list of lists): A list of [x, y] coordinates representing the path.
        weight_data (float): How much to adhere to the original path.
        weight_smooth (float): How much to smooth the path.
        tolerance (float): Convergence threshold.

    Returns:
        list of lists: The smoothed path.
    """
    smoothed_path = [[x, y] for x, y in path]  # Initialize smoothed path
    change = tolerance

    while change >= tolerance:
        change = 0.0
        for i in range(1, len(path) - 1):  # Exclude start and end points
            for j in range(len(path[0])):  # For x and y coordinates
                aux = smoothed_path[i][j]
                smoothed_path[i][j] += weight_data * (path[i][j] - smoothed_path[i][j])
                smoothed_path[i][j] += weight_smooth * (
                    smoothed_path[i-1][j] + smoothed_path[i+1][j] - (2.0 * smoothed_path[i][j])
                )
                change += abs(aux - smoothed_path[i][j])
    return smoothed_path

# Example usage:
original_path = [
    [0.0, 0.0],
    [1.0, 0.1],
    [2.0, -0.1],
    [3.0, 0.2],
    [4.0, -0.2],
    [5.0, 0.0]
]

smoothed_result = smooth_path(original_path)

print("Original Path:")
for point in original_path:
    print(f"  [{point[0]:.2f}, {point[1]:.2f}]")

print("\nSmoothed Path:")
for point in smoothed_result:
    print(f"  [{point[0]:.2f}, {point[1]:.2f}]")
```

#### Further Resources for Motion Planning:

*   [Planning Algorithms (Steven M. LaValle)](http://planning.cs.uiuc.edu/book.html) - *A free online textbook covering a vast range of planning algorithms.*
*   [Open Motion Planning Library (OMPL)](https://ompl.kavrakilab.org/) - *A C++ library for sampling-based motion planning, with Python bindings.*
*   [ROS MoveIt! Framework](https://moveit.ros.org/) - *The most widely used software for mobile manipulation and motion planning in ROS.*