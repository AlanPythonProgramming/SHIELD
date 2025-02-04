### Interface: Functions

#### profileCreate
- **Description**: Creates a person's profile for the current time.
  - The profile should have exactly three properties: `name`, `age`, and `createdAt`.
  - The `updatedAt` property should **not** be in the returned object.
  - `age` is calculated by subtracting `birthYear` from the current year.
- **Input**: `(nameFirst, nameLast, birthYear)`
- **Output**: `PersonProfile` (example below):
  ```json
  {
    "name": "Feliks Zemdegs",
    "age": 28,
    "createdAt": 1715151808
  }
  ```
- **Errors**: N/A
- **Difficulty**: ⭐⭐

#### profileCompareAge
- **Description**: Compares the age of two profiles.
  - Returns:
    - Any positive number if `profile1`'s age is greater than `profile2`'s age.
    - Any negative number if `profile1`'s age is less than `profile2`'s age.
    - `0` if both ages are the same.
- **Input**: `(profile1, profile2)`
- **Output**: `number`
- **Errors**: N/A
- **Difficulty**: ⭐

#### profileUpdateName
- **Description**: Updates the name of a given profile and sets or updates the `updatedAt` property.
  - If `updatedAt` does not exist, it should be created.
  - Example:
    ```json
    {
      "name": "The Chosen One",
      "age": 34,
      "createdAt": 1715153483,
      "updatedAt": 1715153612
    }
    ```
- **Input**: `(profile)`
- **Output**: `undefined` (do not use `return`).
- **Errors**: N/A
- **Difficulty**: ⭐

#### profileHasUpdate
- **Description**: Checks if the profile has the `updatedAt` property.
  - Returns `true` if the property exists, and `false` otherwise.
- **Input**: `(profile)`
- **Output**: `boolean`
- **Errors**: N/A
- **Difficulty**: ⭐

#### profileSerialise
- **Description**: Converts a profile object into a JSON-serialized string.
- **Input**: `(profile)`
- **Output**: `string`
- **Errors**: N/A
- **Difficulty**: ⭐

#### profileDeserialise
- **Description**: Converts a JSON-serialized profile string back into the original object.
- **Input**: `(profile)`
- **Output**: `PersonProfile`
- **Errors**: N/A
- **Difficulty**: ⭐

---

### Data Types

#### Variable Types
- **`PersonProfile`**:
  ```ts
  {
    name: string,         // e.g., "Feliks Zemdegs"
    age: number,          // e.g., 28
    createdAt: number,    // UNIX timestamp in seconds
    updatedAt?: number    // UNIX timestamp in seconds (optional)
  }
  ```
- **`name`**: `string`
- **`birthYear`**: `number` (integer)
- **`age`**: `number` (integer)
- **`createdAt`**: `number` (integer UNIX timestamp in seconds)
- **`updatedAt`**: `number` (integer UNIX timestamp in seconds)

---

### Tasks

1. Implement all functions in `objects.js` as per the descriptions above.
2. Ensure all returned values conform to the provided interfaces.

---

### Testing

#### Running Your Code
To test your implementation:
```shell
$ node objects.js
```
This will execute the code, including the `console.log` statements at the bottom of `objects.js`.

#### Debugging
- Extend testing by adding your own cases with `console.log`.

---

### Submission

1. Use `git` to `add`, `commit`, and `push` your changes to your master branch.
2. Verify your code is uploaded to the GitLab repository.
3. No further action is required after pushing to the master branch; submissions will be auto-collected.

---

### Notes

1. Only explicitly mentioned behaviours in the interface will be tested.
2. Passing the starter tests does not guarantee full marks; further testing is encouraged.
3. External libraries/modules are **not allowed**.
