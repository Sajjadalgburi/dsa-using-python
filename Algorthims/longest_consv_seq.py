from typing import List


def longestConsecutive(nums: List[int]) -> int:
    items = set(nums)
    longest = 0
    # finding the start of a sequence by doing num - 1.
    # if that is in the set then we have a new start of a seq. if not then we have our start

    for num in items:
        if (num - 1) not in items:
            length = 1
            while (num + length) in items:
                length += 1
            longest = max(length, longest)

    return longest


print(longestConsecutive([2, 20, 4, 10, 3, 4, 5]))  # Output: 4
# print(longestConsecutive([0, 3, 2, 5, 4, 6, 1, 1]))  # Output: 7
