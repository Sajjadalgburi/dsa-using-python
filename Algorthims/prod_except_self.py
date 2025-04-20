class Solution(object):
    def productExceptSelf(self, nums):
        # initilize a res array of ones based on the length of the nums input
        res = [1] * (len(nums))
        # example nums len is 4 = [1, 1, 1, 1]

        prefix = 1  # this is all the product of values to the left of the array

        for i in range(len(nums)):
            # we put the prefix in the position i such as nums = pref 1 , [1, 2, 3, 4] => res[1, 1, 1, 1] in iteration one
            # says that at index 0 put the prefix
            res[i] = prefix

            # now, we need to calculate a new prefix by multiplying the prefix by the nums at i
            # iteration one nums[0] is 1. so 1 * 1 is 1. now prefix is still 1
            prefix *= nums[i]

        postfix = 1  # this is all the product of values to the right of the array

        # after the first for-loop is finished, our res looks like this -> [1, ]
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix  # multiply the postfix by the position at res[i]
            postfix *= nums[i]  # multiply the postfix by the input array nums

        return res


s = Solution()
print(s.productExceptSelf([1, 2, 3, 4]))  # Output: [24,12,8,6]
