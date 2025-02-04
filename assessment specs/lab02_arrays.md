### Interface: Functions

#### arraySum
- **Description**: Computes the sum of the given integer array.
  - If the array is empty, the sum is `0`.
- **Input**: `(array)`
- **Output**: `number`
- **Errors**: N/A
- **Difficulty**: ⭐

#### arrayProduct
- **Description**: Computes the product of the given integer array.
  - If the array is empty, the product is `1`.
- **Input**: `(array)`
- **Output**: `number`
- **Errors**: N/A
- **Difficulty**: ⭐

#### arrayMin
- **Description**: Finds the smallest number in the array.
- **Input**: `(array)`
- **Output**: `number` or `null` (if the array is empty)
- **Errors**: Returns `null` if the array is empty.
- **Difficulty**: ⭐

#### arrayMax
- **Description**: Finds the largest number in the array.
- **Input**: `(array)`
- **Output**: `number` or `null` (if the array is empty)
- **Errors**: Returns `null` if the array is empty.
- **Difficulty**: ⭐

#### arrayContains
- **Description**: Determines if the array contains a particular integer element.
- **Input**: `(array, item)`
- **Output**: `boolean`
- **Errors**: N/A
- **Difficulty**: ⭐

#### arrayReversed
- **Description**: Creates a new array that is the reversed version of the original array.
  - The original array should not be modified.
- **Input**: `(array)`
- **Output**: `number[]` or `Array<number>`
- **Errors**: N/A
- **Difficulty**: ⭐

#### arrayHead
- **Description**: Returns the first element in the array.
- **Input**: `(array)`
- **Output**: `number` or `null` (if the array is empty)
- **Errors**: Returns `null` if the array is empty.
- **Difficulty**: ⭐

#### arrayTail
- **Description**: Returns all elements in the array except the first (head).
  - If the input array contains one element, an empty array is returned.
- **Input**: `(array)`
- **Output**: `number[]` or `Array<number>` or `null` (if the array is empty)
- **Errors**: Returns `null` if the array is empty.
- **Difficulty**: ⭐

#### arraysMultiply
- **Description**: Multiplies the elements at each index from two arrays and stores the result in a third array.
  - If the two arrays differ in length, excess elements of the larger array are added to the result.
- **Input**: `(array1, array2)`
- **Output**: `number[]` or `Array<number>`
- **Errors**: N/A
- **Difficulty**: ⭐⭐

#### arraysCommon
- **Description**: Creates a third array containing elements common to two arrays.
  - Each element in the first array can map to at most one element in the second array, and vice versa.
  - Duplicated elements in each array are treated as separate entities.
  - The order is determined by the first array.
- **Input**: `(array1, array2)`
- **Output**: `number[]` or `Array<number>`
- **Errors**: N/A
- **Difficulty**: ⭐⭐⭐

---

### Data Types

#### Variable Types
- **`array`**: `number[]` (same as `Array<number>`, an array of integers like `[1, 2, 3]`)
- **`item`**: `number` (specifically integer)

---

### Tasks

1. Implement all functions in `array.js` as per the descriptions above.
2. Ensure all returned values conform to the provided interfaces.
3. Do not modify the input arrays in functions that explicitly require immutability.

---

### Testing

#### Running Your Code
To test your implementation:
```shell
$ node array.js
```
This will execute the code, including the provided starter test cases.

#### Debugging
- Extend testing by adding your own cases with `console.log` or assertions.

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
