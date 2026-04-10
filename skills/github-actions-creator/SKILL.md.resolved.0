---
name: github-actions-creator
description: Scaffold and create production-ready GitHub Actions in TypeScript or as Composite actions. Use this skill when the user wants to "create a github action", "scaffold a custom action", or "setup a github task automation". It follows best practices from official GitHub action templates, including dependency bundling and automatic test generation.
---

# GitHub Actions Creator

This skill enables you to create a professional GitHub Action from scratch. It supports two primary types:
1. **TypeScript Action** (Default): best for complex logic, using `@actions/core` and requiring a bundling step.
2. **Composite Action**: best for simple shell script sequences, requiring no build step.

## Workflow

### 1. Discovery
Ask the user for the following information if not already provided:
- **Action Name**: (e.g., `my-custom-action`)
- **Description**: What does the action do?
- **Action Type**: TypeScript or Composite?
- **Inputs**: Names, descriptions, defaults.
- **Outputs**: Names, descriptions.
- **Branding**: Icon name (see GitHub branding docs) and color.

### 2. Initialization
Use the `scripts/init_repo.py` script to generate the project structure.

#### TypeScript Structure:
```text
.
├── .github/workflows/test-action.yml
├── __tests__/main.test.ts
├── src/
│   ├── index.ts
│   └── main.ts
├── action.yml
├── package.json
├── tsconfig.json
├── jest.config.js
└── README.md
```

#### Composite Structure:
```text
.
├── .github/workflows/test-action.yml
├── action.yml
└── README.md
```

### 3. Implementation Details

- **TypeScript Boilerplate**: Always include error handling with `core.setFailed()` and input retrieval with `core.getInput()`.
- **Bundling**: For TypeScript, always configure `ncc` or `rollup` to bundle dependencies into `dist/index.js` so they don't need to be committed in `node_modules`.
- **Testing**: Include a basic Jest test for TypeScript actions.
- **Verification Workflow**: Generate a `.github/workflows/test-action.yml` that uses the action locally:
  ```yaml
  jobs:
    test:
      runs-on: ubuntu-latest
      steps:
        - uses: actions/checkout@v4
        - uses: ./
          with:
            # inputs...
  ```

## Reference documentation
- [GitHub Actions Metadata Syntax](https://docs.github.com/en/actions/creating-actions/metadata-syntax-for-github-actions)
- [Toolkit Documentation (@actions/core)](https://github.com/actions/toolkit)
