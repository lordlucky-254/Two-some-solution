"""Compare the three solutions as input size grows.

Run from the repo root:  python benchmarks/benchmark.py
"""
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src import brute_force, hash_map, two_pointers  # noqa: E402

SIZES = [10, 1_000, 10_000, 100_000]
BRUTE_FORCE_LIMIT = 10_000  # O(n^2) at 100k takes minutes


def worst_case(n: int) -> tuple[list[int], int]:
    """Answer sits in the last two slots, so nothing can exit early."""
    nums = list(range(1, n - 1)) + [n * 10, n * 10 + 1]
    return nums, n * 20 + 1


def timeit(fn, nums, target) -> float:
    start = time.perf_counter()
    fn(nums, target)
    return time.perf_counter() - start


def main() -> None:
    solvers = [
        ("brute_force", brute_force.two_sum),
        ("two_pointers", two_pointers.two_sum),
        ("hash_map", hash_map.two_sum),
    ]
    print("| n | " + " | ".join(name for name, _ in solvers) + " |")
    print("|---|" + "---|" * len(solvers))
    for n in SIZES:
        nums, target = worst_case(n)
        cells = []
        for name, fn in solvers:
            if name == "brute_force" and n > BRUTE_FORCE_LIMIT:
                cells.append("skipped")
            else:
                cells.append(f"{timeit(fn, nums, target) * 1000:.3f} ms")
        print(f"| {n:,} | " + " | ".join(cells) + " |")


if __name__ == "__main__":
    main()
