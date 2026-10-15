# Complexity Analysis

| Approach | Time | Space |
|---|---|---|
| Brute force | O(n^2) | O(1) |
| Sorting + two pointers | O(n log n) | O(n) |
| Hash map | O(n) | O(n) |

## Brute force
Two nested loops test all n(n-1)/2 pairs. No extra memory, but the work grows
quadratically: 10x more input means about 100x more time.

## Sorting + two pointers
Sorting dominates at O(n log n). We sort (value, index) pairs so the original
indices survive, then walk two pointers inward in O(n). If the sum is too small
the left pointer moves up; if too large the right pointer moves down.

## Hash map
For each number we ask "have I already seen `target - num`?" A dict lookup is
O(1) on average, so one pass is enough. We trade O(n) memory for speed.
Checking before inserting guarantees an element is never paired with itself.
