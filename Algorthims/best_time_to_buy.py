# Sliding Window Variable Size

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """


# prices = [7,1,5,3,6,4]
s = Solution()
"""
We buy on the second day prices[1] and sell on the prices[4]
profit is = 6 - 1 = 5


return the profit

approach:
keep track of the min and update the min if nessecary

"""
s.maxProfit([7, 1, 5, 3, 6, 4])  # Output: 5
