---
id: 002
title: Update Constitution with Stricter Project-Specific Rules
stage: constitution
date: 2025-12-06
surface: "agent"
model: "Gemini"
feature: "none"
branch: "none"
user: "unknown"
command: "Edit the file '.specify/memory/constitution.md' to strictly enforce the following rules: 1. **Technical Platform Principle:** All Docusaurus components, configurations, and React code must use the **TypeScript** language. 2. **Context7 Principle:** All code generation and configuration changes must be **explicitly prompted to use Context7** for version-accurate Docusaurus, ROS 2, and NVIDIA Isaac SDK documentation. 3. **Content Principle:** The book's content must be organized into **weekly modules** that mirror the structure of the provided course breakdown (Weeks 1-13) and use **Markdown heading levels (H2, H3)** to create the Table of Contents. 4. **Hardware Principle:** A dedicated section must be created in the docs for **"Hardware Requirements"** detailing the Workstation and Edge Kit specifications."
labels: ["constitution", "rules", "typescript", "context7"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - specifyfiles/.specify/memory/constitution.md
tests:
 (none)
---

## Prompt

Edit the file '.specify/memory/constitution.md' to strictly enforce the following rules:

1.  **Technical Platform Principle:** All Docusaurus components, configurations, and React code must use the **TypeScript** language.
2.  **Context7 Principle:** All code generation and configuration changes must be **explicitly prompted to use Context7** for version-accurate Docusaurus, ROS 2, and NVIDIA Isaac SDK documentation.
3.  **Content Principle:** The book's content must be organized into **weekly modules** that mirror the structure of the provided course breakdown (Weeks 1-13) and use **Markdown heading levels (H2, H3)** to create the Table of Contents.
4.  **Hardware Principle:** A dedicated section must be created in the docs for **"Hardware Requirements"** detailing the Workstation and Edge Kit specifications.

## Response snapshot

Successfully updated the constitution.md file with new project-specific principles.

## Outcome

- ✅ Impact: The project constitution was updated to enforce four new, strict principles regarding TypeScript usage, a 'Context7' framework mandate, content structure, and hardware documentation.
- 🧪 Tests: No tests were run.
- 📁 Files: Modified 1 file: `specifyfiles/.specify/memory/constitution.md`.
- 🔁 Next prompts: Future actions will need to adhere to these new, stricter constitutional principles.
- 🧠 Reflection: Successfully replaced the core principles of the constitution while leaving other sections intact. This demonstrates targeted modification of a key project governance document.

## Evaluation notes (flywheel)

- Failure modes observed: None.
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): null
- Next experiment: N/A
