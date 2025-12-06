# Docusaurus Documentation Constitution

## Core Principles

### I. Technical Platform Principle
All Docusaurus components, configurations, and React code must use the **TypeScript** language to ensure type safety, clarity, and maintainability across the project.

### II. Context7 Principle
All automated code generation, configuration changes, and documentation retrieval must be **explicitly prompted to use the 'Context7' framework**. This is mandatory to ensure version-accurate and context-aware documentation for Docusaurus, ROS 2, and the NVIDIA Isaac SDK.

### III. Content Principle
The book's content must be organized into **weekly modules** that mirror the provided course breakdown (Weeks 1-13). The Table of Contents for these modules must be structured using **Markdown heading levels (primarily H2 and H3)** to ensure consistent navigation and structure.

### IV. Hardware Principle
A dedicated, top-level section must be created and maintained in the documentation for **"Hardware Requirements"**. This section must provide detailed specifications for both the primary Workstation and the required Edge Kit.

## Quality and Consistency

### Code Formatting
All code will be formatted using the project's configured Prettier settings. Consistent formatting is non-negotiable and should be applied before any commit.

### Naming Conventions
- React Components: `PascalCase` (e.g., `MyComponent.tsx`)
- CSS Modules: `styles.module.css`
- TypeScript Interfaces: `IPrefix` or `PascalCaseProps` (e.g., `IButtonProps`, `ButtonProps`)

## Governance
These principles supersede all other practices. Amendments require team discussion and documentation to ensure the project's long-term health and maintainability. All contributions will be reviewed for compliance with this constitution.

**Version**: 2.0.0 | **Ratified**: 2025-12-06 | **Last Amended**: 2025-12-06
