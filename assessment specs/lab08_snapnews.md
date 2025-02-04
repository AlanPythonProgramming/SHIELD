### Tasks

#### Task 1: Add v2 API Endpoints

- Implement all `/v2/` routes as described in the provided `swagger.yaml`. The changes include:
  - Move `lab08snapnewstoken` from query strings to headers for security.
  - Maintain backward compatibility for `/v1/` routes.

#### Task 2: Implement New Routes

- Implement the following new `/v1/` routes:
  - `DELETE /v1/announcements/{announcementid}/schedule`
  - `POST /v1/announcements/{announcementid}/schedule/abort`

#### Task 3: Update `/v1/clear`

- Ensure `/v1/clear` clears all active timers by calling `clearTimeout`.
- Refer to `src/snapnews.ts` for the `clear()` function implementation.

---

### Routes

#### `DELETE /v1/announcements/{announcementid}/schedule`
- **Description**: Schedules an announcement for deletion after a specified delay.
- **Input**:
  - Path Parameter:
    ```json
    {
      "announcementid": "number"
    }
    ```
  - Query Parameter:
    ```json
    {
      "secondsFromNow": "number"
    }
    ```
- **Output**:
  ```json
  {}
  ```
- **Errors**:
  - Throws `HTTPError` with status `400` if `secondsFromNow` is not strictly positive.

#### `POST /v1/announcements/{announcementid}/schedule/abort`
- **Description**: Aborts the scheduled deletion of an announcement.
- **Input**:
  - Path Parameter:
    ```json
    {
      "announcementid": "number"
    }
    ```
- **Output**:
  ```json
  {}
  ```
- **Errors**:
  - Throws `HTTPError` with status `400` if no active timer exists for the announcement.

---

### Implementation Details

#### Schedule and Timer
- Use `setTimeout` and `clearTimeout` for scheduling and cancelling tasks.
- Use the following patterns to handle errors inside timer callbacks to prevent server crashes:
  ```typescript
  const timer = setTimeout(() => {
    try {
      performActionThatMayThrowException();
    } catch (err) {
      console.error('Error in timer callback:', err);
    }
  }, delay);
  ```

#### Backward Compatibility
- Maintain functionality for all `/v1/` routes.
- Implement `/v2/` routes with `lab08snapnewstoken` moved to headers.

---

### Testing

#### Run Tests
- Use the provided test suite in `src/snapnews.test.ts` to ensure correctness:
  ```shell
  $ npm test
  ```

#### Measure Coverage
- Measure server-side code coverage using `nyc`:
  ```shell
  $ npm run ts-node-coverage src/server.ts
  ```
- Verify coverage results by opening `coverage/lcov-report/index.html`.

---

### Submission

1. Use `git` to `add`, `commit`, and `push` your changes to your master branch.
2. Verify your code is uploaded to the GitLab repository.
3. No further action is required after pushing to the master branch; submissions will be auto-collected.

---

### Notes

1. Handle edge cases, such as invalid timers or announcement IDs.
2. Ensure that all tests pass and code achieves 100% coverage.
3. Avoid external libraries beyond those specified in `package.json`.
