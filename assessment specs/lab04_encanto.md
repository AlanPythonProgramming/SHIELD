### Interface: Functions

#### createMadrigal
- **Description**: Creates and returns a Madrigal member with a name, age, and an optional gift.
- **Input**: `(name: string, age: number, gift?: string)`
- **Output**: `Madrigal` (object containing `{name: string, age: number, gift?: string}`)
- **Errors**: N/A
- **Difficulty**: ⭐⭐

#### createSong
- **Description**: Creates and returns a Song with a name and singers (a string or an array of strings). If singers is an array, it will contain at least two elements.
- **Input**: `(name: string, singers: string | string[])`
- **Output**: `Song` (object containing `{name: string, singers: string | string[]}`)
- **Errors**: N/A
- **Difficulty**: ⭐

#### extractNamesMixed
- **Description**: Given a list containing a mixture of Madrigal and Song items, returns the names of these items in the order they were given.
- **Input**: `(array: (Madrigal | Song)[])`
- **Output**: `string[]`
- **Errors**: N/A
- **Difficulty**: ⭐

#### extractNamesPure
- **Description**: Given a list containing only Madrigal items or only Song items, returns the names of these items in the order they were given.
- **Input**: `(array: Madrigal[] | Song[])`
- **Output**: `string[]`
- **Errors**: N/A
- **Difficulty**: ⭐

#### madrigalIsSinger
- **Description**: Checks if the given Madrigal is a singer in the given Song. 
- **Input**: `(madrigal: Madrigal, song: Song)`
- **Output**: `boolean`
- **Errors**: N/A
- **Difficulty**: ⭐

#### sortedMadrigals
- **Description**: Returns a sorted array of Madrigals based on:
  1. `age` (ascending order).
  2. `name` (lexicographical order if ages are equal).
- **Input**: `(madrigals: Madrigal[])`
- **Output**: `Madrigal[]` (sorted array)
- **Errors**: N/A
- **Difficulty**: ⭐⭐

#### filterSongsWithMadrigals
- **Description**: Given an array of Madrigals and an array of Songs, returns all Songs that include any of the Madrigals as singers.
- **Input**: `(madrigals: Madrigal[], songs: Song[])`
- **Output**: `Song[]`
- **Errors**: N/A
- **Difficulty**: ⭐⭐

#### getMostSpecialMadrigal
- **Description**: Determines the Madrigal who has sung the most songs. If there is a tie, the Madrigal that appears first in the array is returned.
- **Input**: `(madrigals: Madrigal[], songs: Song[])`
- **Output**: `Madrigal`
- **Errors**: N/A
- **Difficulty**: ⭐⭐⭐

---

### Data Types

#### Variable Types
- **`Madrigal`**: Object containing `{name: string, age: number, gift?: string}`
- **`Song`**: Object containing `{name: string, singers: string | string[]}`
- **`string | string[]`**: Union type representing either a string or an array of strings.

---

### Tasks

1. Implement all functions in `src/madrigal.ts` as per the descriptions above.
2. Ensure all returned values conform to the provided interfaces.
3. Use type annotations as described in the Interface.

---

### Testing

#### Using jest
1. Uncomment the pre-written tests in `src/madrigal.test.ts`.
2. Run the tests with:
   ```shell
   $ npm t
   ```

#### Type-checking with tsc
1. Use the command:
   ```shell
   $ npm run tsc
   ```
   This will validate your type annotations.

#### Running ts-node
1. Run `src/main.ts` directly with:
   ```shell
   $ npm run ts-node src/main.ts
   ```
   Ensure the output matches the expected result.

---

### Submission

1. Use `git` to `add`, `commit`, and `push` your changes to your master branch.
2. Verify your code is uploaded to the GitLab repository.
3. No further action is required after pushing to the master branch; submissions will be auto-collected.

---

### Notes

1. All functions should be implemented as [pure functions](https://en.wikipedia.org/wiki/Pure_function).
2. Passing the pre-written tests does not guarantee full marks; ensure your implementation adheres strictly to the specifications.
3. External libraries/modules beyond those specified are **not allowed**.
