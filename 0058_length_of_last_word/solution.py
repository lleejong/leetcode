class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        cnt = 0
        while i >= 0:
            if s[i] == ' ':
                if cnt > 0:
                    return cnt
                else:
                    cnt = 0
            else:
                cnt += 1
            i -= 1
        return cnt


sol = Solution()
print(sol.lengthOfLastWord('Hello World '))
print(sol.lengthOfLastWord('a '))
