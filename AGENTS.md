# AGENTS.md

## Purpose
This file provides high-value, concise instructions to help OpenCode agents navigate and work effectively in this repository. Every line is designed to prevent errors and speed up ramp-up time.

## Investigation Strategy

When investigating this repository, follow this order of exploration to prioritize the most useful information:

1. **Configuration and Overview Files:**
   - `README*`
   - Root manifests (e.g., `package.json`, `pyproject.toml`)
   - Workspace configuration (e.g., `opencode.json`, CI/CD workflows, codegen configs)
   - Lockfiles (e.g., `package-lock.json`, `poetry.lock`)

2. **Code Quality and Development Tools:**
   - Build, test, lint, format, typecheck configurations
   - Task runners and pre-commit hooks

3. **Documentation:**
   - Existing instruction files
   - `.github` configurations (e.g., CI/CD workflows, `copilot-instructions.md`)

4. **Representative Source Files:**
   - Focus first on core entry points to understand the architecture and main execution flow.
   - Avoid diving into random leaf files initially.

Prefer executable sources of truth (e.g., scripts, configs) over prose documentation if discrepancies arise.

## Key Commands and Workflow
Include here any specific commands or workflows needed for this repository. Currently:

- **Run tests:** TBD
- **Lint code:** TBD
- **Build application:** TBD

To populate the above, identify configurations in task runners, build tools, or other DevOps setups.

## Repository Structure
Describe only structural facts that are relevant to the agent:

- **Monorepo/Multipackage:** Assess if this repository is a monorepo and describe how directories are interlinked.
- **Generated code or migrations:** Note if there are auto-generated files or migrations that should not be edited manually or require specific commands.

## Style and Conventions
Document any repo-specific rules that deviate from community standards:

- Look for linting, formatting, type-checking, or branching workflows.
- Verify all style or convention rules against the existing configuration files to avoid duplication or speculative information.

## Setup and Environment
Identify and document required environment configurations:

- Check for `.env` files, Docker dependencies, or other patterns for managing secrets.
- Note any required external services or infrastructure for local development.

Ensure instructions remain concise and directly actionable. Update only when clarity gaps arise or the project structure changes.