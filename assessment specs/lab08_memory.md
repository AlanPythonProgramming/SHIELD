### Interface: Functions

#### getGameInfo
- **Description**: Returns the current game’s score, mistakes remaining, and clues remaining.
- **Input**: None.
- **Output**:
  ```json
  {
    "score": number,
    "mistakesRemaining": number,
    "cluesRemaining": number
  }
  ```
- **Errors**: None.
- **Difficulty**: ⭐

#### addWord
- **Description**: Adds a word to the game’s dictionary if it doesn’t already exist and increases the score. Decrements mistakesRemaining if the word exists.
- **Input**: `(word: string)`
- **Output**: None.
- **Errors**:
  - Throws an error if the game is inactive.
  - Throws an error if the word already exists in the dictionary.
- **Difficulty**: ⭐⭐

#### removeWord
- **Description**: Removes a word from the game’s dictionary if it exists and increases the score. Decrements mistakesRemaining if the word doesn’t exist.
- **Input**: `(word: string)`
- **Output**: None.
- **Errors**:
  - Throws an error if the game is inactive.
  - Throws an error if the word doesn’t exist in the dictionary.
- **Difficulty**: ⭐⭐

#### viewDictionary
- **Description**: Returns the list of words in the dictionary in chronological order. Consumes a clue during active games.
- **Input**: None.
- **Output**:
  ```json
  ["string", ...]
  ```
- **Errors**:
  - Throws an error if there are no clues remaining during an active game.
- **Difficulty**: ⭐⭐

#### resetGame
- **Description**: Resets the game to its initial state.
- **Input**: None.
- **Output**: None.
- **Errors**: None.
- **Difficulty**: ⭐

#### saveGame
- **Description**: Saves the current game to a file named `memory_[name].json`.
- **Input**: `(name: string)`
- **Output**: None.
- **Errors**:
  - Throws an error if the name is an empty string.
  - Throws an error if the name contains non-alphanumeric characters.
  - Throws an error if a game with the same name already exists.
- **Difficulty**: ⭐⭐⭐

#### loadGame
- **Description**: Loads a saved game from a file named `memory_[name].json`.
- **Input**: `(name: string)`
- **Output**: None.
- **Errors**:
  - Throws an error if the name is an empty string.
  - Throws an error if the name contains non-alphanumeric characters.
  - Throws an error if no saved game matches the given name.
- **Difficulty**: ⭐⭐⭐

---

### Data Types

#### Variable Types
- **`score`**: `number`
- **`mistakesRemaining`**: `number`
- **`cluesRemaining`**: `number`
- **`dictionary`**: `string[]`
- **`name`**: `string`
- **`word`**: `string`

---

### Tasks

1. **Implement Functions**:
   - Implement all functions in `src/memory.ts`.
   - Ensure compliance with the specifications.

2. **Write Tests**:
   - Write comprehensive tests in `src/memory.test.ts`.
   - Test for error cases using `expect.toThrow`.

3. **Continuous Integration**:
   - Update `.gitlab-ci.yml` to include testing and linting steps.

4. **Play the Game**:
   - Implement the functions to play the game by running:
     ```shell
     $ npm start
     ```

---

### Submission

1. Use `git` to `add`, `commit`, and `push` your changes to your master branch.
2. Verify your code is uploaded to the GitLab repository.
3. No further action is required after pushing to the master branch; submissions will be auto-collected.

---

### Notes

1. Only explicitly mentioned behaviors in the function specifications will be tested.
2. Passing all provided tests does not guarantee full marks; ensure strict adherence to the specifications.
3. Files must be saved in the root directory (e.g., `memory_example.json`).
