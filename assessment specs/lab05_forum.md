### Interface: Routes

#### `GET /`
- **Description**: Returns a welcome message.
- **Input**: None.
- **Output**:
  ```json
  {
    "message": "Welcome to the Forum API!"
  }
  ```
- **Errors**: N/A

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
- **Errors**: Returns `{ error }` with status code 400 if `message` is exactly "echo".

#### `POST /post/create`
- **Description**: Creates a new forum post.
- **Input**: JSON body:
  ```json
  {
    "sender": "string",
    "title": "string",
    "content": "string"
  }
  ```
- **Output**:
  ```json
  {
    "postId": "number"
  }
  ```
- **Errors**: Returns `{ error }` with status code 400 if any of `sender`, `title`, or `content` is an empty string.

#### `POST /post/:postid/comment`
- **Description**: Adds a comment to a forum post.
- **Input**: JSON body:
  ```json
  {
    "sender": "string",
    "comment": "string"
  }
  ```
- **Output**:
  ```json
  {
    "commentId": "number"
  }
  ```
- **Errors**: Returns `{ error }` with status code 400 if `postid` does not exist or if any of `sender` or `comment` is an empty string.

#### `GET /post/:postid`
- **Description**: Fetches all details about a specific post.
- **Input**: None.
- **Output**:
  ```json
  {
    "post": {
      "postId": "number",
      "sender": "string",
      "title": "string",
      "content": "string",
      "timeSent": "number",
      "comments": [
        {
          "commentId": "number",
          "sender": "string",
          "comment": "string",
          "timeSent": "number"
        }
      ]
    }
  }
  ```
- **Errors**: Returns `{ error }` with status code 400 if `postid` does not exist.

#### `PUT /post/:postid`
- **Description**: Edits an existing post.
- **Input**: JSON body:
  ```json
  {
    "sender": "string",
    "title": "string",
    "content": "string"
  }
  ```
- **Output**:
  ```json
  {}
  ```
- **Errors**: Returns `{ error }` with status code 400 if `postid` does not exist or if any of `sender`, `title`, or `content` is an empty string.

#### `GET /posts/list`
- **Description**: Lists all forum posts in reverse chronological order.
- **Input**: None.
- **Output**:
  ```json
  {
    "posts": [
      {
        "postId": "number",
        "sender": "string",
        "title": "string",
        "timeSent": "number"
      }
    ]
  }
  ```
- **Errors**: N/A

#### `DELETE /clear`
- **Description**: Clears all data from the forum.
- **Input**: None.
- **Output**:
  ```json
  {}
  ```
- **Errors**: N/A

---

### Data Types

#### Variable Types
- **`error`**: `string` (relevant error message).
- **`postId`, `commentId`**: `number` (integer).
- **`sender`, `title`, `content`, `comment`**: `string`.
- **`timeSent`**: `number` (UNIX timestamp in seconds).
- **`comments`**: Array of objects, where each object contains `{commentId, sender, comment, timeSent}`.
- **`post`**: Object containing `{postId, sender, title, timeSent, content, comments}`.
- **`posts`**: Array of objects, where each object contains `{postId, sender, title, timeSent}`.

---

### Tasks

1. **Test Implementation**:
   - Write comprehensive tests in `src/forum.test.ts` to cover all routes.
   - Ensure edge cases and error handling are tested.

2. **Route Implementation**:
   - Implement the routes in `src/server.ts` based on the descriptions above.
   - Use helper functions from `src/forum.ts` to abstract logic.

3. **Continuous Integration**:
   - Update `.gitlab-ci.yml` to include testing and linting steps.

---

### Submission

1. Use `git` to `add`, `commit`, and `push` your changes to your master branch.
2. Verify your code is uploaded to the GitLab repository.
3. No further action is required after pushing to the master branch; submissions will be auto-collected.

---

### Notes

1. Only explicitly mentioned behaviors in the route descriptions will be tested.
2. Passing all provided tests does not guarantee full marks; ensure your implementation adheres strictly to the specifications.
3. External libraries beyond those specified in `package.json` are **not allowed**.
