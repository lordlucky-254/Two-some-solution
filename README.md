# Two Sum: From Brute Force to O(n)

![tests](../../actions/workflows/tests.yml/badge.svg)

Three Python solutions to **LeetCode #1, Two Sum**, one of the most attempted
problems among CS students, with tests, benchmarks and complexity analysis.

## Problem

Given an array of integers `nums` and an integer `target`, return the indices
of the two numbers that add up to `target`. Each input has exactly one solution
and you may not use the same element twice.

```
Input:  nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
```

## Approaches

| Approach | File | Time | Space | Idea |
|---|---|---|---|---|
| Brute force | `src/brute_force.py` | O(n^2) | O(1) | Check every pair |
| Sorting + two pointers | `src/two_pointers.py` | O(n log n) | O(n) | Sort (value, index), move pointers inward |
| Hash map | `src/hash_map.py` | O(n) | O(n) | Look up `target - num` among values already seen |

Details in [docs/complexity_analysis.md](docs/complexity_analysis.md).

## Quick start

```bash
git clone <your-repo-url>
cd two-sum-solutions
pip install -r requirements.txt
pytest
python benchmarks/benchmark.py
```

## Benchmark results

Worst case (the answer is in the last two positions), single run on my machine:

| n | brute_force | two_pointers | hash_map |
|---|---|---|---|
| 10 | 0.005 ms | 0.010 ms | 0.005 ms |
| 1,000 | 19.173 ms | 0.829 ms | 0.198 ms |
| 10,000 | 1889.486 ms | 8.456 ms | 3.211 ms |
| 100,000 | skipped | 65.530 ms | 20.058 ms |

Brute force is skipped at 100,000 elements because it would take minutes.

## Key takeaways

- **Time/space tradeoff:** the hash map spends O(n) memory to remove an entire loop.
- **Why hash maps help:** average O(1) lookups turn "search for a partner" from a scan into a single step.
- **Sorting loses indices** unless you carry them along, which is why the two-pointer version sorts (value, index) pairs.

## Project structure

```
src/          the three solutions
tests/        pytest suite run against all solvers
benchmarks/   timing script
docs/         complexity write-up
.github/      CI workflow
```

## Ideas to extend

- Two Sum II (sorted input), 3Sum, 4Sum
- Solutions in Java, C++ or JavaScript
- Return all valid pairs instead of one

## License

MIT
