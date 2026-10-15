import random

import pytest

from src import brute_force, hash_map, two_pointers

SOLVERS = [brute_force.two_sum, two_pointers.two_sum, hash_map.two_sum]


@pytest.mark.parametrize("solver", SOLVERS)
@pytest.mark.parametrize(
    "nums,target,expected",
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([-1, -2, -3, -4], -6, [1, 3]),
        ([0, 4, 3, 0], 0, [0, 3]),
        ([1, 5, 9, 14], 23, [2, 3]),
    ],
)
def test_known_cases(solver, nums, target, expected):
    assert sorted(solver(nums, target)) == expected


@pytest.mark.parametrize("solver", SOLVERS)
def test_no_solution_returns_empty(solver):
    assert solver([1, 2, 3], 100) == []


@pytest.mark.parametrize("solver", SOLVERS)
def test_does_not_reuse_same_element(solver):
    # 5 + 5 = 10 would reuse the single 5, so there is no valid answer.
    assert solver([5, 1, 2], 10) == []


@pytest.mark.parametrize("solver", SOLVERS)
def test_random_inputs_are_valid(solver):
    rng = random.Random(42)
    for _ in range(200):
        nums = [rng.randint(-50, 50) for _ in range(rng.randint(2, 30))]
        i, j = rng.sample(range(len(nums)), 2)
        target = nums[i] + nums[j]
        a, b = solver(nums, target)
        assert a != b
        assert nums[a] + nums[b] == target
