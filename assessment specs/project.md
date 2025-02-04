### Overview
**Toohak** is a quiz game platform designed to engage students through interactive quizzes during lectures and tutorials. Admins create and manage quizzes, while players can join sessions without signing up to compete. The platform's backend follows a predefined API interface to ensure compatibility with future frontend development.

---

### Core Objectives

- Build a **backend JavaScript server** to manage quizzes, users, and sessions.
- Implement user registration, authentication, and quiz lifecycle management.
- Enable quiz sessions, player participation, and scoring.
- Ensure secure, scalable, and persistent data handling.

---

### Functional Requirements

#### **User Management**
1. **Register Admin User** (`POST /v1/admin/auth/register`): Register a new admin user with email, password, and names.
2. **Login Admin User** (`POST /v1/admin/auth/login`): Login with email and password to manage quizzes.
3. **Logout Admin User** (`POST /v1/admin/auth/logout`): Logout the current admin session.
4. **Get Admin Details** (`GET /v1/admin/user/details`): Retrieve details of the currently logged-in admin user.
5. **Update Admin Details** (`PUT /v1/admin/user/details`): Update the details of the logged-in admin user.
6. **Update Password** (`PUT /v1/admin/user/password`): Change the password of the logged-in admin user.

#### **Quiz Management**
1. **List Quizzes** (`GET /v1/admin/quiz/list`): Retrieve a list of quizzes owned by the admin.
2. **Create Quiz** (`POST /v1/admin/quiz`): Create a new quiz.
3. **Update Quiz Name** (`PUT /v1/admin/quiz/{quizid}/name`): Update the name of a quiz.
4. **Update Quiz Description** (`PUT /v1/admin/quiz/{quizid}/description`): Update the description of a quiz.
5. **Delete Quiz** (`DELETE /v1/admin/quiz/{quizid}`): Send a quiz to trash.
6. **Restore Quiz** (`POST /v1/admin/quiz/{quizid}/restore`): Restore a quiz from trash.
7. **Manage Trash**:
   - View Trash (`GET /v1/admin/quiz/trash`)
   - Empty Trash (`DELETE /v1/admin/quiz/trash/empty`)

#### **Question Management**
1. **Create Question** (`POST /v1/admin/quiz/{quizid}/question`): Add a question to a quiz.
2. **Update Question** (`PUT /v1/admin/quiz/{quizid}/question/{questionid}`): Modify details of a question.
3. **Delete Question** (`DELETE /v1/admin/quiz/{quizid}/question/{questionid}`): Remove a question from a quiz.
4. **Move Question** (`PUT /v1/admin/quiz/{quizid}/question/{questionid}/move`): Reposition a question in the quiz.
5. **Duplicate Question** (`POST /v1/admin/quiz/{quizid}/question/{questionid}/duplicate`): Duplicate an existing question.

#### **Session Management**
1. **Start Quiz Session** (`POST /v1/admin/quiz/{quizid}/session/start`): Start a new session for a quiz.
2. **Update Session State** (`PUT /v1/admin/quiz/{quizid}/session/{sessionid}`): Modify the state of an active session.
3. **Get Session Status** (`GET /v1/admin/quiz/{quizid}/session/{sessionid}`): Retrieve the status of a specific session.
4. **Get Session Results**:
   - View Results (`GET /v1/admin/quiz/{quizid}/session/{sessionid}/results`)
   - Download Results as CSV (`GET /v1/admin/quiz/{quizid}/session/{sessionid}/results/csv`)

#### **Player Interaction**
1. **Player Join Session** (`POST /v1/player/join`): Allow a player to join a session.
2. **Player Status** (`GET /v1/player/{playerid}`): View the player's current status.
3. **Answer Questions** (`PUT /v1/player/{playerid}/question/{questionposition}/answer`): Submit answers for active questions.
4. **View Results**:
   - Question Results (`GET /v1/player/{playerid}/question/{questionposition}/results`)
   - Session Results (`GET /v1/player/{playerid}/results`)
5. **Chat Management**:
   - View Chat Messages (`GET /v1/player/{playerid}/chat`)
   - Send Chat Message (`POST /v1/player/{playerid}/chat`)

#### **Data Management**
1. **Clear State** (`DELETE /v1/clear`): Reset the application state to initial conditions.
2. **Persist Data**: Implement persistence for user and quiz data using JSON serialization.

#### **V2 Routes**
1. **Enhanced Security**:
   - Move authentication tokens to headers for all routes.
2. **New Route: Search Quizzes** (`GET /v2/admin/quiz/search`):
   - **Input**: Query parameter `name` (string).
   - **Output**: List of quizzes matching the name filter.
3. **Enhanced Results**:
   - Add `averageScore` to session results endpoints.
4. **Pagination**:
   - Add `page` and `limit` query parameters to list endpoints (e.g., `/v2/admin/quiz/list`).

#### **V3 Routes**
1. **Batch Operations**:
   - **Create Questions in Batch** (`POST /v3/admin/quiz/{quizid}/questions/batch`):
     - Input: Array of question objects.
     - Output: Success or failure report for each question.
   - **Delete Quizzes in Batch** (`DELETE /v3/admin/quiz/batch`):
     - Input: Array of `quizId`s.
     - Output: Success or failure report for each quiz.
2. **Analytics**:
   - **Get Quiz Analytics** (`GET /v3/admin/quiz/{quizid}/analytics`):
     - Output: Engagement metrics such as total participants, average score, and time spent.
   - **Get Player Insights** (`GET /v3/admin/player/{playerid}/insights`):
     - Output: Player-specific performance across quizzes.

---

### Server-Side Implementation

#### Middleware
1. **Authentication Middleware**:
   - Validate admin tokens for `/v1/admin` routes.
   - Handle token expiration and invalidation.

2. **Error Handling Middleware**:
   - Catch unhandled exceptions and return structured error responses.
   - Include HTTP status codes and detailed messages.

3. **Request Validation Middleware**:
   - Validate incoming request bodies and query parameters.
   - Return `400 Bad Request` for invalid data.

#### Data Persistence
- Store user, quiz, question, and session data in JSON files.
- Implement periodic backups to avoid data loss.

---

### Testing Specifications

#### Unit Tests
- Write unit tests for all helper functions and middlewares.
- Use mocks for external dependencies (e.g., file system operations).

#### Integration Tests
- Test each route with valid and invalid inputs.
- Ensure expected HTTP status codes and responses.
- Use `supertest` for HTTP request simulation.

#### Load Testing
- Simulate concurrent user sessions using tools like `Artillery`.
- Monitor server performance and identify bottlenecks.

#### Coverage
- Achieve 100% code coverage for all routes and middleware.
- Use `nyc` for coverage reports.

#### Running Tests
- Run all tests with:
  ```shell
  $ npm test
  ```
- Generate coverage reports:
  ```shell
  $ npm run coverage
  ```

---

### Data Models
#### Users
- `userId`: Integer.
- `name`: String (First + Last Name).
- `email`: String.
- `numSuccessfulLogins`: Integer.
- `numFailedPasswordsSinceLastLogin`: Integer.

#### Quizzes
- `quizId`: Integer.
- `name`: String.
- `description`: String.
- `timeCreated`: Timestamp.
- `timeLastEdited`: Timestamp.
- `questions`: Array of question objects.

#### Questions
- `questionId`: Integer.
- `question`: String.
- `timeLimit`: Integer (seconds).
- `points`: Integer.
- `answerOptions`: Array of answer objects.

#### Sessions
- `sessionId`: Integer.
- `state`: Enum (LOBBY, QUESTION_COUNTDOWN, QUESTION_OPEN, QUESTION_CLOSE, ANSWER_SHOW, FINAL_RESULTS, END).
- `players`: Array of player objects.
- `results`: Object containing player scores.

---

### Development Guidelines

- **Versioning**: Use `/v1`, `/v2`, and `/v3` routes for backward compatibility.
- **Error Handling**: Return clear error messages with appropriate HTTP status codes (400, 401, 403).
- **Security**: Implement secure password hashing and session management using tokens.
- **Testing**: Write integration tests for all HTTP endpoints covering success and failure scenarios.
- **Continuous Integration**: Add linting and testing stages to the CI pipeline.

---

### Additional Notes

1. **Frontend Compatibility**: Ensure the backend aligns with frontend expectations as outlined in the specification.
2. **Iteration Goals**: Prioritize tasks based on iteration requirements (e.g., basic functionality in Iteration 1, persistence in Iteration 2).
3. **Deployment**: Deploy to a public server (e.g., Vercel) and test the live implementation.
