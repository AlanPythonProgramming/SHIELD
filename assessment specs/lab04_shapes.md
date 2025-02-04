### Interface: Functions

#### drawShape
- **Description**: Returns a string representing a particular shape based on the given `shape`, `size`, and `isSolid` properties.
  - Valid shapes:
    - `triangle`
    - `square`
  - Shapes can be solid or hollow (`isSolid` determines this).
- **Input**: `(shape: string, size: number, isSolid: boolean)`
- **Output**: `string`
- **Errors**: Returns `"Invalid Input"` if:
  - `shape` is not "square" or "triangle".
  - `size` is a negative integer.
- **Difficulty**: ⭐

---

### Data Types

#### Variable Types
- **`shape`**: `string`
- **`size`**: `number` (integer)
- **`isSolid`**: `boolean`

---

### Tasks

#### Implementation
1. Open `src/shapes.ts`.
2. Fix all linting errors in the pre-written `drawShape` function.
   - Ensure compliance with the provided linting rules.
   - Refactor the code if necessary to improve readability and maintainability.
3. Ensure the following commands run without any errors:
   ```shell
   $ npm run lint
   $ npm test
   ```

#### Testing
- Tests for `drawShape` are provided in `src/shapes.test.js`.
- You do not need to write additional tests.

#### Linting
- Use the `lint-fix` script to automatically fix any auto-fixable linting errors:
  ```shell
  $ npm run lint-fix
  ```

---

### Continuous Integration

1. Open `.gitlab-ci.yml`.
2. Update the pipeline to include:
   - `npm install`
   - `npm test`
   - `npm run lint`

---

### Submission

1. Use `git` to `add`, `commit`, and `push` your changes to your master branch.
2. Verify your code is uploaded to the GitLab repository.
3. No further action is required after pushing to the master branch; submissions will be auto-collected.

---

### Notes

1. Ensure your code adheres strictly to the linting rules defined in `.eslintrc.json`.
2. Refactoring the code to improve readability is encouraged but not mandatory.
3. Passing the tests and linting checks ensures full marks for this lab.