### Interface

#### Core Functionality

You will transform the existing check-ins service into a **RESTful web API** by implementing routes in `src/server.ts` using [Express](https://www.npmjs.com/package/express). The following routes need to be implemented:

1. **Route:** `GET /events/list`
   - **Description**: Lists all events with their details.
   - **Input**: None.
   - **Output**: JSON array of events with the following structure:
     ```json
     [
       {
         "eventId": number,
         "eventName": string,
         "visitorCount": number,
         "checkoutTime": string (ISO format)
       }
     ]
     ```

2. **Route:** `POST /events/create`
   - **Description**: Creates a new event.
   - **Input**: JSON body with the structure:
     ```json
     {
       "eventName": string
     }
     ```
   - **Output**: JSON object:
     ```json
     {
       "eventId": number
     }
     ```

3. **Route:** `PUT /events/:eventId/checkout`
   - **Description**: Marks an event as checked out.
   - **Input**: `eventId` as a URL parameter.
   - **Output**: JSON object:
     ```json
     {
       "message": "Event checked out successfully."
     }
     ```

4. **Route:** `DELETE /events/:eventId`
   - **Description**: Deletes an event.
   - **Input**: `eventId` as a URL parameter.
   - **Output**: JSON object:
     ```json
     {
       "message": "Event deleted successfully."
     }
     ```

5. **Route:** `POST /events/:eventId/visitor`
   - **Description**: Adds a visitor to an event.
   - **Input**: `eventId` as a URL parameter.
   - **Output**: JSON object:
     ```json
     {
       "message": "Visitor added successfully."
     }
     ```

---

### Tasks

1. **Read the API Requirements:**
   - Use `swagger.yaml` to understand the input/output structure of each route.
   - Refer to the pre-written functions in `src/checkins.ts` to understand existing logic.

2. **Write Tests:**
   - Open `src/checkins.test.ts`.
   - Complete all `test.todo` placeholders.
   - Add additional tests to cover edge cases.
   - Run tests with:
     ```shell
     $ npm test
     ```

3. **Implement Routes:**
   - Modify `src/server.ts` to include the required routes.
   - Use Express middleware for JSON parsing and CORS handling.

4. **Test Your Implementation:**
   - Run the server with:
     ```shell
     $ npm run ts-node src/server.ts
     ```
   - Use tools like Postman or curl to send HTTP requests.
   - Validate responses manually if necessary.

5. **Continuous Integration:**
   - Ensure your `.gitlab-ci.yml` file includes steps for:
     - `npm install`
     - `npm test`
     - `npm run lint`

---

### Tips

- **JSON Body Parsing:** Use `req.body` for POST and PUT requests.
- **URL Parameters:** Use `req.params` and cast types explicitly if needed.
- **Query Parameters:** Use `req.query` and cast types explicitly.
- **Error Handling:** Ensure your server returns meaningful error messages with appropriate status codes (e.g., 400, 404).
- **Testing:** Only test the HTTP layer. Avoid testing implementation details like the data store.

---

### Submission

1. Use `git` to `add`, `commit`, and `push` your changes to your master branch.
2. Verify your code is uploaded to the GitLab repository.
3. No further action is required after pushing to the master branch; submissions will be auto-collected.

---

### Notes

1. Passing all provided tests does not guarantee full marks; ensure your implementation adheres strictly to the API specifications.
2. You may not use external libraries beyond those specified in `package.json`.
