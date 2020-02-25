from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 0:
            return 0

        if size == 1:
            return 1

        prev_num = nums[0]
        cursor = 1


        while cursor < len(nums):
            if not prev_num == nums[cursor]:
                prev_num = nums[cursor]
                cursor += 1
            else:
                nums.pop(cursor)

        return len(nums)

sol = Solution()

print(sol.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
