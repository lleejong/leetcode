from typing import List


class Solution:
    # time complexity O(n2), space complexity O(1)
    # Time Submitted Status Runtime Memory Language
    # 11 minutes ago	Accepted	6012 ms	13.7 MB	python3
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                sum = nums[i] + nums[j]
                if sum == target:
                    return [i, j]
        return []

    # time complexity O(n), space complexity O(n)
    # using map
    # Time Submitted Status Runtime Memory Language
    # a few seconds ago	Accepted	36 ms	14.2 MB	python3
    def twoSumImproved(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(0, len(nums)):
            remain = target - nums[i]
            if remain in dic:
                return [dic[remain], i]
            dic[nums[i]] = i
        return []
