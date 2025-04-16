class Solution(object):
    def maxArea(self, height):

        # pointer to point at the left side
        left = 0

        # pointer for the end
        right = len(height) - 1

        max_water = 0

        while left < right:
            # how do we find width?
            width = right - left

            # find out the height to be the minimum between the two heights so that water does not overflow
            h = min(height[left], height[right])

            # calculate the area of the container
            area = h * width

            # update the max_water to be the new max if there is one
            max_water = max(area, max_water)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water


s = Solution()
print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # Output: 49
