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
        prev_char = ''
        # char_arr = list(s).reverse()
        # for i in range(0, len(char_arr)):
        #     current_int = self.roman_int_map[list[i]]
        #     j = i + 1

        for i in range(0, len(s)):
            current_int = self.roman_int_map[s[i]]
            # if current_int > sum:
            #     sum = current_int - sum
            # else:
            #     sum += current_int
            prev_char = s[i]
        return sum


sol = Solution()
print(sol.romanToInt("LVIII"))
