# Development Guide

This guide provides instructions for setting up your development environment and running the online book locally.

## Prerequisites

Before you begin, ensure you have the following installed:

*   **Node.js**: Version 18.x or higher (LTS recommended). You can download it from [nodejs.org](https://nodejs.org/).
*   **npm**: Node Package Manager, which comes bundled with Node.js.

## Setup Instructions

Follow these steps to get your local development environment ready:

1.  **Clone the Repository**:
    ```bash
    git clone https://github.com/your-org/your-repo.git # Replace with the actual URL of your repository
    cd book-site # Or whatever your repository's root directory is named
    ```

2.  **Install Dependencies**:
    Navigate to the project root directory and install the required Node.js packages:
    ```bash
    npm install
    ```

## Environment Variables

The application requires certain environment variables to be set for full functionality, particularly for the vectorization script and the RAG chatbot API.

Create a `.env` file in the root of the project and add the following variables:

```
# OpenAI API Key
OPENAI_API_KEY="your-openai-api-key"

# Qdrant Cloud connection details
QDRANT_URL="your-qdrant-cloud-url"
QDRANT_API_KEY="your-qdrant-api-key"

# OpenAI ChatKit Secret Key
CHATKIT_SECRET_KEY="your-chatkit-secret-key"
```

**Note**: The Python scripts (`scripts/vectorize.py` and `api/main.py`) are configured to load these variables from the environment. Ensure the `.env` file is present or that these variables are exported in your shell.

## Running Locally

To start the local development server and view the online book:

```bash
npm run start
```

This will typically open the site in your browser at `http://localhost:3000`. The server features hot-reloading, so changes you make to the documentation files will automatically reflect in the browser.

## Content Generation Note

Please be aware that much of the content for this book was generated or scaffolded using an AI agent guided by the "Context7" framework to ensure version accuracy for Docusaurus, ROS 2, and NVIDIA Isaac SDK documentation.
