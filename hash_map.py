def two_sum(nums: list[int], target: int) -> list[int]:
    """One pass with a hash map of value -> index. Time O(n), space O(n)."""
    seen: dict[int, int] = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
