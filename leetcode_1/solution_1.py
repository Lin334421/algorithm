from typing import List
"""

给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_ = {}
        for i, nums in enumerate(nums):
            if target-nums in map_:
                return [map_[target-nums],i]
            else:
                map_[nums] = i



s = Solution()
print(s.twoSum(nums = [3,2,4], target = 6))