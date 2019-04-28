class Solution:

    def climbStairs(self, n: int) -> int:
        result_list = [1, 2]
        for i in range(2, n):
            result_list.append(result_list[i - 1] + result_list[i - 2])
        return result_list[n - 1]
    # solution 1
    # -----------------------------------
    # result_map = {}
    # def __init__(self):
    #     self.result_map[1] = 1
    #     self.result_map[2] = 2

    # def climbStairs(self, n: int) -> int:
    #     if n in self.result_map:
    #         return self.result_map[n]
    #     self.result_map[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
    #     return self.result_map[n]
    # -----------------------------------
    # solution 2
    # -----------------------------------
    # def climbStairsRecursive(self, n: int) -> int:
    #     if n is 0:
    #         return 0
    #     if n is 1:
    #         return 1
    #     if n is 2:
    #         return 2
    #     return self.climbStairs(n - 1) + self.climbStairs(n - 2)
    # -----------------------------------


sol = Solution()
print(sol.climbStairs(4))
print(sol.climbStairs(8))

# 1 : 1
# 2 : (1 1) (2)
# 3 : (1 1 1) (1 2) (2 1)
# 4 : (1 1 1 1) /    (1 1 2) (1 2 1) (2 1 1)    / (2 2)
# 5 : (1 1 1 1 1) / (1 1 1 2)  ( 1 1 2 1 ) (1 2 1 1) ( 2 1 1 1) / (2 2 1) (1 2 2)
# 6 : (1 1 1 1 1 1) / (1 1 1 1 2) (1 1 1 2 1 ) (1 1 2 1 1 ) (1 2 1 1 1) (2 1 1 1 1) / (2 2 1 1) (
# 2 1 2 1) (1 2 1 2
