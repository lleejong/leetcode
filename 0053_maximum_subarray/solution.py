from typing import List

class Solution:
    # prefix sum
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        total = 0
        min_sum = 0
        for i, value in enumerate(nums):
            total += value
            max_sum = max(max_sum, total - min_sum)
            min_sum = min(total, min_sum)
        return max_sum

    # TODO: dp algorithm

sol = Solution()
print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

