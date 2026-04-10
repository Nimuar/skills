---
name: spec-driven-design
description: A skill for following a structured, specification-first development process using Markdown artifacts. It guides users through four phases: Constitution (Project Rules), Specification (Requirements), Planning (Architecture), and Execution (Tasks). Use this skill whenever a user wants to start a new project, implement a significant feature, or perform a complex software change. This skill ensures that the "what" and "why" are defined before the "how" and any code is written.
---

# Spec-Driven Design (SDD)

Spec-Driven Design is a development methodology that inverts the traditional power structure: **Specifications don't serve code—code serves specifications.** The specification is the central source of truth, and code is merely its "last-mile" expression.

### Core Philosophy
1. **Intent-Driven**: Development begins with natural language intent, not code.
2. **Constitutional**: All implementations are governed by a set of immutable principles (The Constitution).
3. **No-Gap Implementation**: Specifications are refined until they are precise enough to generate implementation and tests directly.

## The SDD Workflow

The process consists of five distinct phases. DO NOT skip phases. All artifacts must be stored in the `.spec/` directory (or organized in sub-directories like `.spec/features/[ID]-[name]/`).

### Phase 0: Constitution
**Goal**: Establish the "Architectural DNA" and "The Nine Articles of Development".
- **Artifact**: `memory/constitution.md` (or `.spec/CONSTITUTION.md`)
- **Focus**: Global constraints, technology preferences, and non-negotiable standards (Library-First, CLI-First, Test-First).
- **Trigger**: Start here for any new project.

### Phase 2: Specification
**Goal**: Define the "What" and "Why".
- **Artifact**: `.spec/SPECIFICATION.md`
- **Focus**: User journeys, functional requirements, success criteria, and business value.
- **Rules**: NO technical implementation details here. Focus only on the experience and outcomes.

### Phase 3: Planning
**Goal**: Define the "How".
- **Artifact**: `.spec/IMPLEMENTATION_PLAN.md`
- **Focus**: Technical architecture, data models, API signatures, and dependency changes.

### Phase 4: Testing
**Goal**: Define the "Verification".
- **Artifact**: `.spec/TEST_PLAN.md`
- **Focus**: Unit tests, integration tests, manual verification steps, and edge cases.

### Phase 5: Execution
**Goal**: Break it down into work.
- **Artifact**: `.spec/TASKS.md`
- **Focus**: A granular, checkable list of tasks based on the Plan and Test Plan.

---

## Instructions for the Assistant

1. **Initialize Phase**: If the user hasn't started SDD, help them initialize the `.spec/` directory and start with the `CONSTITUTION.md`.
2. **Phase Gating**: Before moving to the next phase, ask the user to review and approve the current artifact. Check off the completion in the `task.md`.
3. **Artifact Integrity**: Ensure all artifacts are strictly Markdown. Do not use external tools or CLI commands for these documents.
4. **Context Building**: Refer back to previous artifacts to ensure consistency (e.g., the Plan must satisfy the Spec, and the Tasks must implement the Plan).

## Templates

Use the templates in the `templates/` directory as a baseline for creating these artifacts.

---

## Example Trigger Queries

- "I want to build a new React app for tracking library books."
- "Let's add a multi-player mode to our game."
- "I need to refactor the authentication system to use OAuth2."
- "Start a spec-driven design process for a new CLI tool."
- "Help me plan out the next set of software changes using SDD."
