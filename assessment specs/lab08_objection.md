### Interface: Functions

#### getObjections
- **Description**: Analyzes a question and testimony to determine if any objections apply.
- **Input**: `(question: string, testimony: string, examinationType: ExaminationType)`
- **Output**:
  ```typescript
  Set<Objection>
  ```
- **Errors**:
  - Throws an error if the `question` is an empty string.
  - Throws an error if the `testimony` is an empty string.
- **Difficulty**: ⭐⭐

---

### Interface: Data Types

#### Enums
- **`Objection`**:
  - `ARGUMENTATIVE`
  - `COMPOUND`
  - `HEARSAY`
  - `LEADING`
  - `NON_RESPONSIVE`
  - `RELEVANCE`
  - `SPECULATION`

- **`ExaminationType`**:
  - `CROSS`
  - `DIRECT`

---

### Objection Items and Criteria

1. **ARGUMENTATIVE**
   - Valid only during `CROSS` examination.
   - Triggered when a `question` does not end with a question mark (`?`).

2. **COMPOUND**
   - Triggered when a `question` contains more than one question mark (`?`).

3. **HEARSAY**
   - Triggered when a `testimony` contains any of the phrases:
     - "heard from"
     - "told me"

4. **LEADING**
   - Valid only during `DIRECT` examination.
   - Triggered if:
     - `question` starts with "why did you" or "do you agree".
     - `question` ends with "right?" or "correct?".

5. **NON_RESPONSIVE**
   - Triggered when the `testimony` does not contain any word from the `question`.
     - Words are exact matches and split by whitespace.
     - Ignore characters that are not letters, numbers, or spaces.

6. **RELEVANCE**
   - Triggered when the length of the `testimony` is greater than twice the length of the `question`.

7. **SPECULATION**
   - During `DIRECT` examination:
     - Triggered when the `testimony` contains the word "think".
   - During `CROSS` examination:
     - Triggered when the `question` contains the word "think".

---

### Tasks

1. **Implement Functionality**:
   - Implement `getObjections` in `src/objection.ts` based on the criteria above.
   - Ensure all inputs are case-insensitive by normalizing them to lowercase.

2. **Write Tests**:
   - Write comprehensive tests in `src/objection.test.ts`.
   - Ensure tests cover all objection items, edge cases, and combinations.

3. **Code Coverage**:
   - Run tests with:
     ```shell
     $ npm t
     ```
   - Check test coverage by opening `coverage/lcov-report/index.html` in a browser.
   - Ensure 100% test coverage.

4. **Continuous Integration**:
   - Update `.gitlab-ci.yml` to include testing and linting steps.

---

### Submission

1. Use `git` to `add`, `commit`, and `push` your changes to your master branch.
2. Verify your code is uploaded to the GitLab repository.
3. No further action is required after pushing to the master branch; submissions will be auto-collected.

---

### Notes

1. Passing all tests and achieving 100% coverage does not guarantee full marks. Ensure your implementation adheres to the specifications.
2. Only explicitly mentioned behaviors will be tested.
3. External libraries beyond those specified in `package.json` are **not allowed**.
