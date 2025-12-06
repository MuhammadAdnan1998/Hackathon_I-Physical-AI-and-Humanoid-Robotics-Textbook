# Hardware Requirements

## Minimum System Requirements

To effectively engage with the course material and execute basic simulations within the Docusaurus environment, a minimum hardware configuration is necessary. This setup allows for foundational development and limited testing without the full fidelity of advanced simulations.

*   **Processor (CPU):** Quad-core Intel i5 (8th Gen or newer) or AMD Ryzen 5 (2000 series or newer)
*   **Memory (RAM):** 16 GB DDR4
*   **Storage:** 500 GB SSD (NVMe recommended for faster loading times)
*   **Graphics (GPU):** NVIDIA GeForce GTX 1660 or AMD Radeon RX 580 (minimum 6GB VRAM)
*   **Operating System:** Ubuntu 20.04 LTS (recommended), Windows 10/11 (with WSL2 enabled)
*   **Network:** Stable internet connection (50 Mbps download / 10 Mbps upload)

## Recommended System Specifications

For optimal performance, complex simulations, real-time robotics control, and advanced AI model training within ROS 2 and NVIDIA Isaac SDK, the following specifications are highly recommended. This configuration ensures a smooth development experience and the ability to handle larger datasets and more intricate robotic models.

*   **Processor (CPU):** Intel Core i7 (10th Gen or newer) or AMD Ryzen 7 (3000 series or newer) with 8+ cores
*   **Memory (RAM):** 32 GB DDR4 (or more)
*   **Storage:** 1 TB NVMe SSD
*   **Graphics (GPU):** NVIDIA GeForce RTX 3070 (or newer) / NVIDIA Quadro RTX 4000 (or newer) (8GB+ VRAM). **NVIDIA GPU is critical for Isaac SDK compatibility.**
*   **Operating System:** Ubuntu 20.04 LTS or 22.04 LTS
*   **Network:** High-speed internet connection (100 Mbps download / 20 Mbps upload)

## Software Requirements

The following software stack is essential for development within the course, covering Docusaurus, ROS 2, and the NVIDIA Isaac SDK ecosystems.

*   **Operating System:**
    *   Ubuntu 20.04 LTS (Focal Fossa) or 22.04 LTS (Jammy Jellyfish) - *Primary development environment*
    *   Windows 10/11 with WSL2 (Windows Subsystem for Linux 2) - *Alternative for Windows users*
*   **Docusaurus:**
    *   Node.js (LTS version, e.g., 18.x or 20.x)
    *   npm or yarn (package manager)
*   **ROS 2 (Robot Operating System 2):**
    *   Foxy Fitzroy (for Ubuntu 20.04) or Humble Hawksbill (for Ubuntu 22.04)
    *   Colcon build tools
    *   Python 3 (default with Ubuntu)
*   **NVIDIA Isaac SDK (Context7 version):**
    *   Isaac Sim (latest compatible version with ROS 2 and Ubuntu)
    *   NVIDIA GPU Driver (latest stable version)
    *   Docker and NVIDIA Container Toolkit (for containerized environments)
*   **Development Tools:**
    *   VS Code (with C++, Python, Docker, ROS, and Remote Development extensions)
    *   Git (for version control)
    *   CMake (build system for C++)
    *   Gazebo (robot simulator, often bundled with ROS 2)
    *   Jupyter Notebook (for data analysis and ML experiments)