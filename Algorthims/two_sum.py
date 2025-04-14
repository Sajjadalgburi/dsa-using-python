from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i, val in enumerate(nums):
            map[val] = i

        for i, val in enumerate(nums):
            diff = target - val
            if diff in map:
                return [i, map[diff]]


s = Solution()
# print(s.twoSum([3, 4, 5, 6], 7)) [0, 1]
# print(s.twoSum([4, 5, 6], 10))  # [0, 2]
print(s.twoSum([2, 5, 5, 11], 10))  # [1, 2]
