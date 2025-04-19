class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int

        Blocks;
        each block is a postive number and has width of 1

        Question;
        how much water can the elevation map trap

        Thoughts;
        in order to trap water a condition must be met
        1. there has to be blocks to the right and left of the water
        2. water cannot overflow, meaning, we need to calculate the min height between the two pointers

        Input:
        An array of int represeting block heights

        Output:
        how much water can be stored

        We can use the TWO POINTER approach
        1. have left pointer poin at the first index, second pointer point to left + 1
        """

        left, right = 0, 1

        # our water output
        water = 0

        # iterate through the entire array
        while right < len(height):
            if left - 1 >= 0:
                # width is the distance between the two blocks
                w = left + right

                # grab the min height between the two blocks
                h = min(height[left], height[right + 1])

                trap = w * h
                water = water + trap

            else:
                left += 1
                right += 1

        # return the water
        return water


s = Solution()
s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])  # Output: 6
