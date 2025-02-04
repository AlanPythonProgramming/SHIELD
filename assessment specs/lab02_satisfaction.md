### Interface: Functions

#### sortedFastFood
- **Description**: Sorts an array of fast food restaurants in **descending order** based on:
  1. `customerService`
  2. `foodVariety`
  3. `valueForMoney`
  4. `timeToMake`
  5. `taste`
  6. `name` (in **ascending lexicographical order**, case-insensitive)
- **Input**: `(fastFoodArray)`
- **Output**: `fastFoodArray` (sorted array)
- **Errors**: N/A
- **Difficulty**: ⭐⭐⭐

#### sortedSatisfaction
- **Description**: Sorts an array of fast food restaurants based on their overall **satisfaction** (highest first).
  - Satisfaction is calculated using the formula:
    ```math
    \text{satisfaction} =
    \frac{
        \text{customerService}
        + \text{foodVariety}
        + \text{valueForMoney}
        + \text{timeToMake}
        + \text{taste}
    }{5}
    ```
  - If two restaurants have the same satisfaction score, their names are sorted in **ascending lexicographical order** (case-insensitive).
- **Input**: `(fastFoodArray)`
- **Output**: `satisfactionArray` (sorted array with satisfaction values)
- **Errors**: N/A
- **Difficulty**: ⭐⭐⭐

---

### Satisfaction Formula
The satisfaction of a restaurant is the average score of the following:
- `customerService`
- `foodVariety`
- `valueForMoney`
- `timeToMake`
- `taste`

You do not need to round the satisfaction value.

---

### Data Types

#### Variable Types
- **`fastFoodArray`**: `Array` of objects, where each object contains the following keys:
  - `name`: `string`
  - `customerService`: `number`
  - `foodVariety`: `number`
  - `valueForMoney`: `number`
  - `timeToMake`: `number`
  - `taste`: `number`
- **`restaurantName`**: `string`
- **`satisfactionArray`**: `Array` of objects, where each object contains the following keys:
  - `restaurantName`: `string`
  - `satisfaction`: `number`
- **`satisfaction`**: `number`

---

### Tasks

1. Implement both `sortedFastFood` and `sortedSatisfaction` in `satisfaction.js` as per the descriptions above.
2. Ensure all returned values conform to the provided interfaces.
3. Do not modify the input arrays in functions that explicitly require immutability.

---

### Testing

#### Running Your Code
To test your implementation:
```shell
$ node satisfaction.js
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
