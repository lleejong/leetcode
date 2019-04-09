class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        haystack_len = len(haystack)
        needle_len = len(needle)

        if needle_len == 0:
            return 0

        if haystack_len < needle_len:
            return -1

        for i in range(0, haystack_len):
            j = 0
            if not (haystack_len - i) >= needle_len:
                return -1
            while j < needle_len:
                if haystack[i + j] == needle[j]:
                    j += 1
                else:
                    break
            if j == needle_len:
                return i
            else:
                i += j
        return -1

sol = Solution()
print(sol.strStr("a", "a"))
print(sol.strStr("hello", "ll"))
print(sol.strStr("aaaaa", "bba"))