### Interface: Functions

#### isLeap
- **Description**: Given a strictly positive year, return `true` if it is a [leap year](https://en.wikipedia.org/w/index.php?title=Leap_year&oldid=1130382965#Algorithm_for_Gregorian_leap_year), and `false` otherwise.
- **Input**: `(year)`
- **Output**: `boolean`
- **Errors**: N/A
- **Difficulty**: ⭐

#### countLeaps
- **Description**: Given an array of strictly positive years, return the number of leap years present in the array.
- **Input**: `(yearArray)`
- **Output**: `number`
- **Errors**: N/A
- **Difficulty**: ⭐

#### getNextLeap
- **Description**: Given a strictly positive year, return the closest leap year **AFTER** the given year.
- **Input**: `(year)`
- **Output**: `number`
- **Errors**: N/A
- **Difficulty**: ⭐

---

### Data Types

#### Variable Types
- **`year`**: `number`
- **`yearArray`**: `number[]` (same as `Array<number>`)

---

### Tasks

1. Implement the specified functions in `leap.js` according to the descriptions above.
2. Ensure all returned values and errors conform to the provided interface.

---

### Implementation Details

1. Open the file `leap.js` in your preferred text editor.
2. Replace the provided stub code with your implementation.

---

### Testing

#### Running Your Code
To test your implementation:
```shell
$ node leap.js
```
This will execute the code, including the `console.assert` and `console.log` at the bottom of `leap.js`.

#### Debugging
- If there are no **'Assertion failed'** messages, your implementation passes the starter tests.
- Extend testing by adding your own cases with `console.assert` and `console.log`.

---

### Submission

1. Use `git` to `add`, `commit`, and `push` your changes to your master branch.
2. Verify your code is uploaded to the GitLab repository.
3. No further action is required after pushing to the master branch; submissions will be auto-collected.

---

### Notes

1. Only explicitly mentioned behaviours in the interface will be tested.
2. Non-positive years are not tested for `isLeap`; handle them as you see fit.
3. Passing the starter tests does not guarantee full marks; further testing is encouraged.
4. External libraries/modules are **not allowed**.
