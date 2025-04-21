from typing import List


class Solution(object):
    def findMaxAverage(self, nums: List[int], k: int):
        """
        Goal:
        Find the subarray whose length == k which has the maximum average

        approach:
        will use a sliding window because I have to find a subarray of k length
        1. find any edge cases. if length if input array is less than k then return soething
        2. to find average i will use the built in sum method to find the sum of the k elements in arr such as k=2 [1, 2, 3] =  1 + 2 = 3

        """
        # step 1
        if len(nums) == 1:
            return float(nums[0])

        # step 2 is to find the intial average total in the window of k
        total = float(sum(nums[:k]))
        maxTotal = total

        # step 3 is to iterate through the nums of a
        # fixed size window and pretty much just keep updating the highest average compared to our initial average
        for i in range(len(nums) - k):
            total -= nums[i]
            total += nums[i + k]
            maxTotal = max(maxTotal, total)

        # return the maximum average we can find in the input arr
        return float(maxTotal / k)


s = Solution()
print(s.findMaxAverage([1, 12, -5, -6, 50, 3], 4))
