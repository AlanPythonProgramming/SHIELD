### Interface: Functions

#### checkPassword
- **Description**: Checks the strength of the given password and returns a string representing the result. The returned string is in [Title Case](https://apastyle.apa.org/style-grammar-guidelines/capitalization/title-case) and can be one of:
  1. **"Strong Password"**:
     - At least 12 characters long.
     - Contains at least 1 number.
     - Contains at least 1 uppercase letter.
     - Contains at least 1 lowercase letter.
  2. **"Moderate Password"**:
     - At least 8 characters long.
     - Contains at least 1 letter (uppercase or lowercase).
     - Contains at least 1 number.
  3. **"Horrible Password"**:
     - Matches exactly any of the [top 5 most common passwords](https://en.wikipedia.org/wiki/List_of_the_most_common_passwords) from the 2021 Nordpass Ranking.
  4. **"Poor Password"**:
     - Any remaining passwords not categorized as horrible, moderate, or strong.
- **Input**: `(password)`
- **Output**: `string`
- **Errors**: N/A
- **Difficulty**: ⭐⭐

---

### Data Types

#### Variable Types
- **`password`**: `string`, consisting of [printable ASCII characters](https://aticleworld.com/printable-ascii-characters-list/) (Decimals 32-126 inclusive).

---

### Tasks

#### Writing Tests
1. Open the file `password.test.js`.
2. Write at least **10 tests** for `checkPassword`:
   - Avoid redundant tests.
   - Ensure each test targets a specific case.
   - Aim to cover as many different cases as possible.
   - Follow the specification closely when designing your tests.
3. Run your tests with:
   ```shell
   $ npm test
   ```
4. Push your `password.test.js` file to GitLab.

#### Implementation
1. Open `password.js` and implement `checkPassword` according to its documentation.
2. Run your tests to validate your implementation.
3. Fix any bugs and push your changes.

---

### Submission

1. Use `git` to `add`, `commit`, and `push` your changes to your master branch.
2. Verify your code is uploaded to the GitLab repository.
3. No further action is required after pushing to the master branch; submissions will be auto-collected.

---

### Notes

1. You must return the strings **exactly as specified**:
   ```js
   return "Strong Password";
   return "Moderate Password";
   return "Horrible Password";
   return "Poor Password";
   ```
2. Only test the requirements specified in the interface.
3. Do not test undefined behavior (e.g., passing non-string inputs).
4. External libraries/modules are **not allowed** unless explicitly stated.
