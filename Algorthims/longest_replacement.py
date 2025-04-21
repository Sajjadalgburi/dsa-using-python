class Solution(object):
    def characterReplacement(self, s: str, k: int):
        """
        Question:
        find the longest sbustring containng the same letter after changing things around k times

        return:
        length of the substring after preforming the above operation
        """

        count = {}
        left = 0
        res = 0
        maxF = 0
        for right in range(len(s)):

            if s[right] not in count:
                count[s[right]] = 1

            count[s[right]] += 1
            maxF = max(maxF, count[s[right]])
            window_len = (right - left + 1)
            if window_len - maxF > k:
                count[s[left]] -= 1
                l += 1
            else:
                res = max(res, window_len)
        return res


s = Solution()

print(s.characterReplacement("ABAB", 2))
