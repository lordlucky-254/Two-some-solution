def two_sum(nums: list[int], target: int) -> list[int]:
    """Sort (value, index) pairs, then move two pointers inward.

    Time O(n log n), space O(n).
    """
    pairs = sorted((value, index) for index, value in enumerate(nums))
    left, right = 0, len(pairs) - 1
    while left < right:
        total = pairs[left][0] + pairs[right][0]
        if total == target:
            return sorted([pairs[left][1], pairs[right][1]])
        if total < target:
            left += 1
        else:
            right -= 1
    return []
