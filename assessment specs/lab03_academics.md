### Interface: Functions

#### academicCreate
- **Description**: Creates a new academic and returns an object containing a unique academic ID.
- **Input**: `(name, hobby)`
- **Output**: `{ academicId }`
- **Errors**: Returns `{ error }` if:
  - `name` is an empty string.
  - `hobby` is an empty string.
- **Difficulty**: ⭐

#### courseCreate
- **Description**: Creates a new course and returns an object containing a unique course ID.
  - The academic who creates the course is both a staff member and a course member.
- **Input**: `(academicId, name, description)`
- **Output**: `{ courseId }`
- **Errors**: Returns `{ error }` if:
  - `academicId` does not refer to an existing academic.
  - `name` is not in the format of 4 uppercase letters followed by 4 digits (e.g., "COMP1531").
- **Difficulty**: ⭐

#### academicDetails
- **Description**: Returns details about a specified academic.
- **Input**: `(academicId, academicToViewId)`
  - `academicId`: The requester’s ID (must be valid).
  - `academicToViewId`: The ID of the academic whose details are being requested.
- **Output**: `{ academic }`
- **Errors**: Returns `{ error }` if:
  - `academicId` does not refer to an existing academic.
  - `academicToViewId` does not refer to an existing academic.
- **Difficulty**: ⭐

#### courseDetails
- **Description**: Returns details about a specified course.
- **Input**: `(academicId, courseId)`
- **Output**: `{ course }`
- **Errors**: Returns `{ error }` if:
  - `academicId` does not refer to an existing academic.
  - `courseId` does not refer to an existing course.
  - `academicId` is not a member of the course.
- **Difficulty**: ⭐⭐⭐

#### academicsList
- **Description**: Returns brief details about all academics.
- **Input**: `(academicId)`
- **Output**: `{ academics }`
- **Errors**: Returns `{ error }` if:
  - `academicId` does not refer to an existing academic.
- **Difficulty**: ⭐

#### coursesList
- **Description**: Returns brief details about all courses.
- **Input**: `(academicId)`
- **Output**: `{ courses }`
- **Errors**: Returns `{ error }` if:
  - `academicId` does not refer to an existing academic.
- **Difficulty**: ⭐⭐

#### courseEnrol
- **Description**: Enrolls an academic in a course.
  - The academic can be enrolled as a staff member or a regular member, depending on the `isStaff` parameter.
- **Input**: `(academicId, courseId, isStaff)`
- **Output**: `{}`
- **Errors**: Returns `{ error }` if:
  - `academicId` does not refer to an existing academic.
  - `courseId` does not refer to an existing course.
  - `academicId` is already a member or staff of the course.
- **Difficulty**: ⭐⭐⭐

#### clear
- **Description**: Resets the database to its initial (empty) state and returns an empty object.
- **Input**: `()`
- **Output**: `{}`
- **Errors**: N/A
- **Difficulty**: ⭐

---

### Data Types

#### Variable Types
- **`academicId`**: `number` (integer)
- **`courseId`**: `number` (integer)
- **`name`**: `string`
- **`hobby`**: `string`
- **`description`**: `string`
- **`isStaff`**: `boolean`
- **`academic`**: Object containing keys `{ academicId, name, hobby }`
- **`course`**: Object containing keys `{ courseId, name, description, allMembers, staffMembers }`
- **`academics`**: Array of objects, where each object contains `{ academicId, academicName }`
- **`courses`**: Array of objects, where each object contains `{ courseId, courseName }`

---

### Tasks

1. Implement all functions in `academics.js` as per the descriptions above.
2. Ensure all returned values conform to the provided interfaces.
3. Design the database as needed; it is black-boxed to auto-marking.

---

### Testing

#### Running Your Code
To test your implementation:
```shell
$ npm test academics.test.js
```
This will execute your test suite.

#### Debugging
- Write comprehensive tests in `academics.test.js` for each function.
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