class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        Question:
        Return the number of days that you have to wait after 
        the current day (ith) to get a warmer temperature

        Return:
        An array of answers which you have to wait to get a warmer temperature

        To find a temp that is hotter than todays temp;
        future temp > todays temp

        """

        ans = []

        for i in range(len(temperatures)):
            days = 0
            for j in range(i + 1, len(temperatures)):
                days += 1
                if temperatures[i] < temperatures[j]:
                    ans.append(days)
                    break
            else:
                ans.append(0)

        return ans


"""
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
"""
s = Solution()
print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
