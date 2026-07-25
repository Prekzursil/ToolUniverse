```markdown
# ToolUniverse Development Patterns

> Auto-generated skill from repository analysis

## Overview
This skill teaches you the core development patterns and conventions used in the ToolUniverse TypeScript codebase. You'll learn how to structure files, write imports and exports, follow commit conventions, and write tests in alignment with the repository's standards. This guide is ideal for contributors aiming for consistency and maintainability in their code.

## Coding Conventions

### File Naming
- Use **camelCase** for all file names.
  - Example: `toolManager.ts`, `userSettings.ts`

### Import Style
- Use **relative imports** for referencing modules within the codebase.
  - Example:
    ```typescript
    import { getTool } from './toolManager';
    ```

### Export Style
- Use **named exports** for all modules.
  - Example:
    ```typescript
    // In toolManager.ts
    export function getTool(id: string) { ... }
    export const TOOL_LIST = [...];
    ```

### Commit Messages
- Follow **Conventional Commits** style.
- Use the `chore` prefix for maintenance and non-feature changes.
  - Example:
    ```
    chore: update dependencies to latest versions
    ```

## Workflows

### Code Contribution
**Trigger:** When adding new features or making changes to the codebase  
**Command:** `/contribute`

1. Create a new branch for your feature or fix.
2. Use camelCase for any new file names.
3. Write code using relative imports and named exports.
4. Write or update tests in files matching `*.test.*`.
5. Commit changes using the conventional commit format (e.g., `chore: ...`).
6. Open a pull request for review.

### Testing
**Trigger:** When verifying code functionality  
**Command:** `/test`

1. Locate or create test files with the `*.test.*` pattern.
2. Write tests for new or updated code.
3. Run the test suite (framework not specified; check project documentation or scripts).
4. Ensure all tests pass before merging.

## Testing Patterns

- Test files follow the `*.test.*` naming pattern (e.g., `toolManager.test.ts`).
- The testing framework is not explicitly specified; check for scripts or documentation in the repository.
- Place test files alongside the modules they test or in a dedicated test directory.

  Example test file:
  ```typescript
  // toolManager.test.ts
  import { getTool } from './toolManager';

  describe('getTool', () => {
    it('returns the correct tool by id', () => {
      expect(getTool('hammer')).toBeDefined();
    });
  });
  ```

## Commands
| Command      | Purpose                                      |
|--------------|----------------------------------------------|
| /contribute  | Start the code contribution workflow         |
| /test        | Run or write tests for the codebase          |
```
