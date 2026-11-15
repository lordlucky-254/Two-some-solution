# Two Sum: edge-case practice

Use this short exercise after running the solution tests. For each input, predict the returned indices (or `[]`) before checking the implementations.

| `nums` | `target` | What it checks |
|---|---:|---|
| `[4, 4]` | `8` | Equal values at distinct indices are valid. |
| `[4]` | `8` | One item cannot be reused. |
| `[0, 0, 3]` | `0` | Zero values and distinct positions. |
| `[-8, 3, 5]` | `-3` | Negative target and mixed signs. |
| `[1, 2, 3, 4]` | `20` | No solution. |
| `[2, 7, 11, 15]` | `9` | A pair near the beginning. |

## Questions

1. Why must a solution return indices rather than just the two values?
2. In the hash-map approach, why is the current item checked against previously seen values before it is added?
3. Why must the sorting approach keep each original index attached to its value?
4. What is the extra-space cost of each approach, and what work causes it?

Run the test suite with `pytest`. When adding a new case, check that it validates the required sum and distinct indices rather than relying on one exact index order when multiple answers are possible.
