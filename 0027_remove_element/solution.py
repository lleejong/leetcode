from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        size = len(nums)
        if size == 0:
            return 0

        cursor = 0
        while cursor < len(nums):
            if not nums[cursor] == val:
                cursor += 1
            else:
                nums.pop(cursor)

        return len(nums)
