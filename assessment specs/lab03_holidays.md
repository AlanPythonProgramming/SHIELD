### Interface: Functions

#### holidaysInRange
- **Description**: Determines the dates for Valentine’s Day, Easter, and Christmas for a range of years.
  - If `start` is less than 325, return an empty array.
  - If `start` is greater than `end`, return an empty array.
  - Otherwise, return an array of objects, each containing the dates for Valentine’s Day, Easter, and Christmas for every year in the range (inclusive).
- **Input**: `(start, end)`
- **Output**: `holidaysArray` where:
  - Each element is an object containing:
    ```js
    {
      valentinesDay: string, // e.g. "Sunday, 14.02.1971"
      easter: string,        // e.g. "Sunday, 11.04.1971"
      christmas: string      // e.g. "Saturday, 25.12.1971"
    }
    ```
- **Errors**: N/A
- **Difficulty**: ⭐⭐⭐

#### main
- **Description**: Reads a starting and ending year from the user and prints the results of `holidaysInRange`.
  - Use `console.log` to display the output.
  - Use [prompt-sync](https://www.npmjs.com/package/prompt-sync) to read user input.
  - Convert input to integers using `parseInt()`.
- **Input**: `(start, end)`
- **Output**: `undefined` (prints directly to stdout).
- **Errors**: N/A
- **Difficulty**: ⭐

---

### Data Types

#### Variable Types
- **`start`**: `number` (integer)
- **`end`**: `number` (integer)
- **`valentinesDay`**: `string`, e.g. "Sunday, 14.02.1971"
- **`easter`**: `string`, e.g. "Sunday, 11.04.1971"
- **`christmas`**: `string`, e.g. "Saturday, 25.12.1971"
- **`holidaysArray`**: Array of objects, where each object contains:
  ```js
  {
    valentinesDay: string,
    easter: string,
    christmas: string
  }
  ```

---

### Tasks

1. Implement the function `holidaysInRange` in `holidays.js` according to its description.
2. Implement the `main` function in `main.js` to handle user input and print the output.
3. Ensure all output conforms to the expected format.

---

### Testing

#### Writing Tests (optional)
- Write tests for `holidaysInRange` in `holidays.test.js`.
- Cover cases like:
  - Valid year ranges.
  - Start less than 325.
  - Start greater than end.
- You do not need to write tests for `main`.

#### Running Your Code
To test your implementation:
```shell
$ npm test holidays.test.js
```

---

### Submission

1. Use `git` to `add`, `commit`, and `push` your changes to your master branch.
2. Verify your code is uploaded to the GitLab repository.
3. No further action is required after pushing to the master branch; submissions will be auto-collected.

---

### Notes

1. Only explicitly mentioned behaviours in the interface will be tested.
2. Passing the starter tests does not guarantee full marks; further testing is encouraged.
3. You may not use any libraries other than those specified (`date-fns`, `date-fns-holiday-us`, `prompt-sync`).
