# Feature Specification: Online Book - The Guide to Modern Agentic Development

**Feature Branch**: `feat/book-structure-initial`
**Created**: 2025-12-06
**Status**: Draft
**Input**: User prompt for creating a comprehensive Docusaurus textbook.

## 1. Book Identity and Goal

*   **Book Name:** "The Guide to Modern Agentic Development: Physical AI and Humanoid Robotics"
*   **Goal:** To create a comprehensive, Docusaurus-based online textbook that covers the complete course outline, organized into weekly modules with clear learning outcomes and project requirements.

## 2. User Stories

### User Story 1 - Weekly Learning Path (Priority: P1)
As a student, I want to access course content organized into clear weekly modules that match the official syllabus, so that I can easily follow the learning path and find materials for a specific week.

**Acceptance Scenarios**:
1.  **Given** I am on the book's homepage, **When** I look at the sidebar navigation, **Then** I see a list of 13 weekly modules.
2.  **Given** I click on a specific week (e.g., "Week 3"), **Then** I am taken to a page containing the curriculum for that week.

---

### User Story 2 - Clear Learning Objectives (Priority: P1)
As a prospective or current student, I want to view the high-level learning outcomes for the course, so that I can understand the key skills and knowledge I will acquire.

**Acceptance Scenarios**:
1.  **Given** I am exploring the book, **When** I navigate to the "Learning Outcomes" section, **Then** I see a clear, bulleted list of the 6 official course outcomes.

---

### User Story 3 - Hardware Procurement (Priority: P1)
As a student preparing for the course, I want to find a single, detailed page listing all required hardware, so that I can procure the necessary equipment before the course begins.

**Acceptance Scenarios**:
1.  **Given** I am on the book's site, **When** I navigate to the "Hardware Requirements" section, **Then** I see detailed specifications for the "Digital Twin Workstation," "Edge Kit," and "Robot Lab Options."

---

### User Story 4 - Understanding Evaluation (Priority: P2)
As a student, I want to understand how I will be evaluated, so I need a clear description of all graded assessments and projects.

**Acceptance Scenarios**:
1.  **Given** I am on the book's site, **When** I find the "Assessments" section, **Then** I see a list of the four main graded projects and their objectives.
2.  **Given** I am viewing the "Assessments" section, **When** I look at the Capstone project, **Then** I see the detailed project description.

## 3. Requirements

### Functional Requirements

-   **FR-001**: The Docusaurus site MUST have the title: "The Guide to Modern Agentic Development: Physical AI and Humanoid Robotics".
-   **FR-002**: The site's content structure and primary navigation MUST be organized into **13 Weekly Modules**, as detailed in the course outline.
-   **FR-003**: A dedicated "Learning Outcomes" page/section MUST be created and display the 6 official course learning outcomes.
-   **FR-004**: A dedicated, top-level "Hardware Requirements" page/section MUST be created, detailing the specifications for the Digital Twin Workstation, Edge Kit, and Robot Lab Options.
-   **FR-005**: A dedicated "Assessments" page/section MUST be created, listing the course's graded projects.
-   **FR-006**: The "Assessments" section MUST contain a "Capstone Project" entry with the exact description: "The Autonomous Humanoid. A final project where a simulated robot receives a voice command, plans a path, navigates obstacles, identifies an object using computer vision, and manipulates it."
-   **FR-007**: All content MUST adhere to the principles in `.specify/memory/constitution.md`, including the use of Markdown H2/H3 headings for TOC generation and TypeScript for any custom components.

### Content Placeholders (To be populated)

-   **Learning Outcomes Content**:
    -   `[To be populated with the 6 Learning Outcomes]`
-   **Weekly Breakdown Content**:
    -   `[To be populated with the detailed topic list for Weeks 1-13]`
-   **Assessments Content**:
    -   `[To be populated with details for the 'ROS 2 package', 'Gazebo sim', 'Isaac perception' assessments]`
-   **Hardware Requirements Content**:
    -   `[To be populated with detailed specs for the 'Digital Twin Workstation', 'Edge Kit', and 'Robot Lab Options']`

## 4. Success Criteria

-   **SC-001**: A student can navigate from the homepage to any of the 13 weekly modules via the sidebar.
-   **SC-002**: The "Hardware Requirements", "Learning Outcomes", and "Assessments" pages are easily discoverable from the main navigation.
-   **SC-003**: All content placeholders in the functional requirements are filled with the correct and final information.
-   **SC-004**: The final rendered site structure directly mirrors the specified weekly breakdown and content hierarchy.

## RAG Chatbot Integration Feature

### 1. Core Functionality
The chatbot must be embedded within the Docusaurus site and respond only to questions about the book's content (Physical AI, ROS 2, Isaac Sim, etc.).

### 2. Contextual Mode
The bot must specifically handle contextual queries based on user-selected text within the documentation, sending that selected text as part of the RAG prompt.

### 3. Technical Stack (Advanced ChatKit Integration)
The FastAPI server must implement the Advanced ChatKit Integration pattern.

*   **Backend Focus**: The FastAPI server must primarily expose a single, secure `/api/chatkit/session` (or `/token`) endpoint for managing ChatKit sessions.
*   **Session Logic**: This endpoint will be responsible for securely managing the ChatKit session by generating a short-lived Client Secret (or token) required by the frontend.
*   **RAG Integration Point**: The RAG logic (Qdrant retrieval, contextual query processing) must be integrated using the ChatKit Python SDK within the FastAPI backend, or by referencing an external OpenAI Agent Workflow ID if the RAG is hosted externally.
*   **Frontend**: The Docusaurus React component must utilize the `@openai/chatkit-react` library to render the UI and call the FastAPI session endpoint for authentication.

### 4. Acceptance
The bot must correctly cite sources from the book content when answering questions.
