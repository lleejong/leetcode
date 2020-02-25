class Solution:
    roman_int_map = {}

    def __init__(self):
        self.roman_int_map['I'] = 1
        self.roman_int_map['V'] = 5
        self.roman_int_map['X'] = 10
        self.roman_int_map['L'] = 50
        self.roman_int_map['C'] = 100
        self.roman_int_map['D'] = 500
        self.roman_int_map['M'] = 1000

    def romanToInt(self, s: str) -> int:
        sum = 0

        for i in range(0, len(s) - 1):
            if self.roman_int_map[s[i]] >= self.roman_int_map[s[i + 1]]:
                sum += self.roman_int_map[s[i]]
            else:
                sum -= self.roman_int_map[s[i]]

        sum += self.roman_int_map[s[len(s) - 1]]
        return sum

sol = Solution()
print(sol.romanToInt("LVIII"))
