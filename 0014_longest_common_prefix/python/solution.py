import sys
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) <= 0:
            return ""
        result = ""
        min_len = sys.maxsize
        for word in strs:
            if min_len > len(word):
                min_len = len(word)

        for i in range(0, min_len):
            current_char = strs[0][i]
            is_same = True
            for j in range(1, len(strs)):
                if not current_char == strs[j][i]:
                    is_same = False
                    break
            if not is_same:
                return result
            else:
                result += current_char

        return result


sol = Solution()
print(sol.longestCommonPrefix([]))
print(sol.longestCommonPrefix(["flower","flower","flower"]))
print(sol.longestCommonPrefix(["dog","racecar","car"]))
