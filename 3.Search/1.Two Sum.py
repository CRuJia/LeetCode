"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

 

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
class Solution:
    # 现排序，然后使用指针对撞
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = list(enumerate(nums))
        nums.sort(key=lambda x: x[1])
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i][1] + nums[j][1] > target:
                j -= 1
            elif nums[i][1] + nums[j][1] < target:
                i += 1
            else:
                if nums[j][0] < nums[i][0]:
                    nums[j], nums[i] = nums[i], nums[j]
                return nums[i][0], nums[j][0]

s = Solution()
print(s.twoSum([2, 7, 11, 15],13))
