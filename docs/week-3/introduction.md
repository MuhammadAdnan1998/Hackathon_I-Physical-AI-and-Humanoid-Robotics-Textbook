# Week 3 Introduction

## Perception and Sensing

This week, we will explore how robots perceive and sense the world around them. Perception is the process of acquiring, interpreting, selecting, and organizing sensory information. It is a critical component of any autonomous system, as it enables the robot to understand its environment and make intelligent decisions.

### Topic 3.1: Computer Vision for Robotics

Computer vision is a field of artificial intelligence that trains computers to interpret and understand the visual world. In robotics, computer vision is used for a wide range of tasks, including:

*   **Object Detection and Recognition:** Identifying and classifying objects in the environment.
*   **Scene Understanding:** Building a semantic understanding of the robot's surroundings.
*   **Visual Servoing:** Using visual feedback to control the robot's motion.
*   **Simultaneous Localization and Mapping (SLAM):** Building a map of the environment while simultaneously tracking the robot's location within it.

#### Example: Basic Image Processing with OpenCV (Python)

```python
import cv2
import numpy as np

def process_image(image_path):
    """
    Loads an image, converts it to grayscale, applies a blur, and displays it.
    """
    # Load the image
    img = cv2.imread(image_path)

    if img is None:
        print(f"Error: Could not load image from {image_path}")
        return

    # Convert to grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply a Gaussian blur
    blurred_img = cv2.GaussianBlur(gray_img, (5, 5), 0)

    # Display the original and processed images (requires a display environment)
    cv2.imshow('Original Image', img)
    cv2.imshow('Grayscale Blurred Image', blurred_img)
    cv2.waitKey(0) # Wait indefinitely until a key is pressed
    cv2.destroyAllWindows()

# Example usage (assuming 'example.jpg' is in the same directory)
# You would replace 'example.jpg' with a path to an actual image file
# process_image('example.jpg')
print("To run the OpenCV example, ensure you have an image file (e.g., 'example.jpg') and uncomment the call to process_image().")
```

#### Further Resources for Computer Vision and 3D Sensing:

*   [OpenCV Documentation](https://docs.opencv.org/4.x/) - *Official documentation for the OpenCV library.*
*   [Computer Vision: Algorithms and Applications (Richard Szeliski)](http://szeliski.org/Book/) - *A comprehensive textbook on computer vision.*
*   [Point Cloud Library (PCL)](https://pointclouds.org/) - *A large-scale, open project for 2D/3D image and point cloud processing.*
*   [ROS 2 Perception Stack](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Using-Rqt-Console-And-Logger-Level.html#ros2-perception-stack) - *Overview of perception tools within the ROS 2 ecosystem.*

### Topic 3.2: LiDAR and 3D Sensing

LiDAR (Light Detection and Ranging) is a remote sensing method that uses light in the form of a pulsed laser to measure ranges (variable distances) to the Earth. In robotics, LiDAR is used to create high-resolution 3D maps of the environment. We will also explore other 3D sensing technologies, such as:

*   **Stereo Cameras:** Using two cameras to perceive depth, similar to human vision.
*   **Structured Light:** Projecting a known pattern of light onto the environment to determine the 3D structure of objects.
*   **Time-of-Flight (ToF) Cameras:** Measuring the time it takes for a light signal to travel from the camera to the object and back to determine depth.
