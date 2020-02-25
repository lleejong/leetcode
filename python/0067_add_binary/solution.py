from typing import Tuple


class Solution:
    def __binarysum__(self, a: int, b: int) -> Tuple[int, int]:
        total = a + b
        if total is 2:
            return 1, 0
        elif total is 1:
            return 0, 1
        else:
            return 0, 0

    def __binarysum_with_carry_in__(self, a: int, b: int, carry_in: int) -> Tuple[int, int]:
        total = a + b + carry_in
        if total is 3:
            return 1, 1
        elif total is 2:
            return 1, 0
        elif total is 1:
            return 0, 1
        else:
            return 0, 0

    def addBinary(self, a: str, b: str) -> str:
        bigger = ''
        other = ''
        if len(a) > len(b):
            bigger = a
            other = b
        else:
            bigger = b
            other = a
        cursor_bigger = len(bigger) - 1
        cursor_other = len(other) - 1
        carry_in = 0
        result = ''
        while cursor_other >= 0:
            carry_in, carry_out = self.__binarysum_with_carry_in__(int(bigger[cursor_bigger]), int(other[cursor_other]),
                                                                   carry_in)
            result = str(carry_out) + result
            cursor_bigger -= 1
            cursor_other -= 1

        while cursor_bigger >= 0:
            carry_in, carry_out = self.__binarysum__(int(bigger[cursor_bigger]), carry_in)
            result = str(carry_out) + result
            cursor_bigger -= 1
        if carry_in > 0:
            result = str(carry_in) + result
        return result


sol = Solution()
# print(sol.addBinary('11', '1'))
print(sol.addBinary('1010', '1011'))
