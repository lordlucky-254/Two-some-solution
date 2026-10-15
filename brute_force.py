def two_sum(nums: list[int], target: int) -> list[int]:
    """Check every pair. Time O(n^2), space O(1)."""
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []
