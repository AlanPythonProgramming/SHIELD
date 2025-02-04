### Interface: Routes

#### `GET /`
- **Description**: Returns a welcome message.
- **Input**: None.
- **Output**:
  ```json
  {
    "message": "Welcome to the Quiz API!"
  }
  ```
- **Errors**: None.

#### `GET /echo/echo`
- **Description**: Echoes back the provided message.
- **Input**: Query parameter:
  ```json
  {
    "message": "string"
  }
  ```
- **Output**:
  ```json
  {
    "message": "string"
  }
  ```
- **Errors**: Throws `HTTPError` with status `400` if `message` is exactly "echo".

#### `DELETE /clear`
- **Description**: Clears all data and active timers.
- **Input**: None.
- **Output**:
  ```json
  {}
  ```
- **Errors**: None.

#### `POST /quiz/create`
- **Description**: Creates a new quiz.
- **Input**: Headers:
  ```json
  {
    "lab08quizsecret": "bruno's fight club"
  }
  ```
  Body:
  ```json
  {
    "quizTitle": "string",
    "quizSynopsis": "string"
  }
  ```
- **Output**:
  ```json
  {
    "quizId": "number"
  }
  ```
- **Errors**:
  - Throws `HTTPError` with status `401` if `lab08quizsecret` is invalid.
  - Throws `HTTPError` with status `400` if `quizTitle` or `quizSynopsis` is empty.

#### `GET /quiz/:quizid`
- **Description**: Retrieves details of a quiz.
- **Input**: Headers:
  ```json
  {
    "lab08quizsecret": "bruno's fight club"
  }
  ```
- **Output**:
  ```json
  {
    "quiz": {
      "quizId": "number",
      "quizTitle": "string",
      "quizSynopsis": "string",
      "questions": "array"
    }
  }
  ```
- **Errors**:
  - Throws `HTTPError` with status `401` if `lab08quizsecret` is invalid.
  - Throws `HTTPError` with status `400` if `quizid` does not exist.

#### `PUT /quiz/:quizid`
- **Description**: Edits a quiz.
- **Input**: Headers:
  ```json
  {
    "lab08quizsecret": "bruno's fight club"
  }
  ```
  Body:
  ```json
  {
    "quizTitle": "string",
    "quizSynopsis": "string"
  }
  ```
- **Output**:
  ```json
  {}
  ```
- **Errors**:
  - Throws `HTTPError` with status `401` if `lab08quizsecret` is invalid.
  - Throws `HTTPError` with status `400` if `quizid` does not exist or if `quizTitle`/`quizSynopsis` is empty.

#### `DELETE /quiz/:quizid`
- **Description**: Deletes a quiz.
- **Input**: Headers:
  ```json
  {
    "lab08quizsecret": "bruno's fight club"
  }
  ```
- **Output**:
  ```json
  {}
  ```
- **Errors**:
  - Throws `HTTPError` with status `401` if `lab08quizsecret` is invalid.
  - Throws `HTTPError` with status `400` if `quizid` does not exist.

#### `GET /quizzes/list`
- **Description**: Lists all quizzes.
- **Input**: Headers:
  ```json
  {
    "lab08quizsecret": "bruno's fight club"
  }
  ```
- **Output**:
  ```json
  {
    "quizzes": [
      {
        "quizId": "number",
        "quizTitle": "string"
      }
    ]
  }
  ```
- **Errors**:
  - Throws `HTTPError` with status `401` if `lab08quizsecret` is invalid.

---

### Data Types

| Variable Name         | Type                                         |
|-----------------------|----------------------------------------------|
| `lab08quizsecret`     | `string`                                    |
| `quizId`              | `number`                                    |
| `quizTitle`           | `string`                                    |
| `quizSynopsis`        | `string`                                    |
| `questions`           | Array of objects containing `{ questionId, questionString, questionType, answers }` |
| `quizzes`             | Array of objects containing `{ quizId, quizTitle }` |

---

### Tasks

1. **Implement Routes**:
   - Write the necessary logic for all routes described above in `src/server.ts`.
   - Use helper functions where applicable to keep routes clean.

2. **Test Implementation**:
   - Run the provided test suite with:
     ```shell
     $ npm test
     ```
   - Add additional tests as needed to ensure 100% coverage.

3. **Code Coverage**:
   - Run your server with coverage enabled:
     ```shell
     $ npm run ts-node-coverage src/server.ts
     ```
   - Ensure all lines are covered.

4. **Submission**:
   - Commit and push your changes to GitLab.

---

### Notes

1. Ensure unique IDs for quizzes and questions.
2. Handle edge cases, such as invalid IDs or empty strings.
3. External libraries beyond those specified in `package.json` are **not allowed**.
