class Solution:
    def reverse(self, x: int) -> int:
        if not self.isValidRange(x):
            return 0
        is_positive = (x > 0)
        if not is_positive:
            x *= -1
        result = 0
        stack = []
        while x > 0:
            stack.append(x % 10)
            x = (int)(x / 10)

        stack.reverse()
        while len(stack) > 0:
            result = (result * 10) + stack.pop()

        if not is_positive:
            result *= -1
        if not self.isValidRange(result):
            return 0
        return result

    def isValidRange(self, x: int) -> bool:
        if (-pow(2, 31) >= x) | (x >= (pow(2, 31) - 1) ):
            return False
        else:
            return True
