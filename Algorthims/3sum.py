class Solution(object):
    def threeSum(self, nums):
        nums = sorted(nums)
        results = []

        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i-1]:
                continue

            start = i + 1
            end = len(nums) - 1

            while start < end:
                sum = nums[i] + nums[start] + nums[end]

                if sum == 0:
                    results.append([nums[i], nums[start], nums[end]])
                    start += 1
                    end -= 1

                    # Skip duplicates for start and end
                    while start < end and nums[start] == nums[start - 1]:
                        start += 1
                    while start < end and nums[end] == nums[end + 1]:
                        end -= 1
                elif sum < 0:
                    start += 1
                else:
                    end -= 1

        return results


s = Solution()

print(s.threeSum([-1, 0, 1, 2, -1, -4]))  # Output: [[-1, -1, 2], [-1, 0, 1]]
