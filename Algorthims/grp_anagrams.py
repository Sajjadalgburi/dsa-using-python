from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        map = dict()

        for char in strs:
            anagram = ''.join(sorted(list(char)))
            if anagram in map:
                map[anagram].append(char)
            else:
                map[anagram] = [char]

        return list(map.values())


s = Solution()


# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
print(s.groupAnagrams(["act", "pots", "tops", "cat", "stop", "hat"]))
