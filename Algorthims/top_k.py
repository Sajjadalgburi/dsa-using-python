import enum
from typing import List

"""
1. use a hashmap to keep track of how many times a value occurs
2. we will initilize an empty output array = []
3. i will also intilize a max variable to keep track of the maximum value in the map
4. i will iterate through map values and update the max variable to be the current max in the map
5. if, i found a max, i append to output and delete the key to find a new max
6. return the output at the end
"""


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1

        for number, count in count.items():
            freq[count].append(number)

        print(freq)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


solution = Solution()
print(solution.topKFrequent([1, 1, 1, 1, 2, 2, 3], 2))  # Output: [1, 2]
