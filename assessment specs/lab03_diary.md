### Interface: Functions

#### clear
- **Description**: Removes all entries in the diary and returns an empty object.
- **Input**: `()`
- **Output**: `{}`
- **Errors**: N/A
- **Difficulty**: ⭐

#### addDiaryEntry
- **Description**: Creates a new diary entry and returns an object containing a unique `entryId`.
- **Input**: `(title, content)`
- **Output**: `{ entryId }`
- **Errors**: Returns `{ error }` if:
  - `title` is an empty string.
  - `content` is an empty string.
- **Difficulty**: ⭐

#### viewDiaryEntry
- **Description**: Returns the full details of a diary entry corresponding to the given `entryId`.
- **Input**: `(entryId)`
- **Output**: `{ entry }` where:
  - `entry` is an object containing `{ entryId, title, content, timestamp }`.
- **Errors**: Returns `{ error }` if:
  - `entryId` does not refer to an existing diary entry.
- **Difficulty**: ⭐

#### listDiaryEntries
- **Description**: Returns brief details about all diary entries.
  - Entries should appear in the order they were created (e.g., `[e1, e2, e3]`).
- **Input**: `()`
- **Output**: `{ entries }` where:
  - `entries` is an array of objects, each containing `{ entryId, title }`.
- **Errors**: N/A
- **Difficulty**: ⭐

#### editDiaryEntry
- **Description**: Edits the title and content of a diary entry and returns an empty object.
  - You do not need to update the timestamp.
- **Input**: `(entryId, title, content)`
- **Output**: `{}`
- **Errors**: Returns `{ error }` if:
  - `entryId` does not refer to an existing diary entry.
  - `title` is an empty string.
  - `content` is an empty string.
- **Difficulty**: ⭐⭐

#### searchDiary
- **Description**: Searches the diary for all entries where the title or content contains the given substring.
  - Entries should appear in the order they were created (e.g., `[e1, e2, e3]`).
- **Input**: `(substring)`
- **Output**: `{ entries }` where:
  - `entries` is an array of objects, each containing `{ entryId, title }`.
- **Errors**: Returns `{ error }` if:
  - `substring` is an empty string.
- **Difficulty**: ⭐⭐

---

### Data Types

#### Variable Types
- **`entryId`**: `number` (integer).
- **`title`**: `string`.
- **`content`**: `string`.
- **`timestamp`**: `number` (integer UNIX timestamp in seconds).
- **`substring`**: `string`.
- **`entries`**: Array of objects, where each object contains `{ entryId, title }`.
- **`entry`**: Object containing `{ entryId, title, content, timestamp }`.

---

### Tasks

1. Implement all functions in `diary.js` as per the descriptions above.
2. Ensure all returned values conform to the provided interfaces.
3. Design the database as needed; it is black-boxed to auto-marking.

---

### Testing

#### Running Your Code
To test your implementation:
```shell
$ npm test diary.test.js
```
This will execute your test suite.

#### Debugging
- Write comprehensive tests in `diary.test.js` for each function.
- Use the `clear` function at the beginning of each test to ensure independence.

---

### Submission

1. Use `git` to `add`, `commit`, and `push` your changes to your master branch.
2. Verify your code is uploaded to the GitLab repository.
3. No further action is required after pushing to the master branch; submissions will be auto-collected.

---

### Notes

1. Only explicitly mentioned behaviours in the interface will be tested.
2. Passing the starter tests does not guarantee full marks; further testing is encouraged.
3. External libraries/modules are **not allowed** unless specified.
