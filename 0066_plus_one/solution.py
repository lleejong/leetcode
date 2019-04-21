from typing import List, Tuple


class Solution:
    def __overflow__(self, a: int, b: int) -> Tuple[int, int]:
        sum = a + b
        if sum > 9:
            return 1, sum - 10
        else:
            return 0, sum

    def plusOne(self, digits: List[int]) -> List[int]:
        cursor = len(digits) - 1
        carry_in = 1
        while cursor >= 0:
            carry_in, carry_out = self.__overflow__(digits[cursor], carry_in)
            if carry_in > 0:
                digits[cursor] = carry_out
                cursor -= 1
            else:
                digits[cursor] = carry_out
                break
        if carry_in > 0:
            digits.insert(0, carry_in)
        return digits


sol = Solution()
print(sol.plusOne([1, 2, 3]))
print(sol.plusOne([4, 3, 2, 1]))
print(sol.plusOne([9, 9, 9, 9]))
