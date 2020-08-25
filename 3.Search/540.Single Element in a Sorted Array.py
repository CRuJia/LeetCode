"""
给定一个只包含整数的有序数组，每个元素都会出现两次，唯有一个数只会出现一次，找出这个数。

示例 1:

输入: [1,1,2,3,3,4,4,8,8]
输出: 2
示例 2:

输入: [3,3,7,7,10,11,11]
输出: 10
注意: 您的方案应该在 O(log n)时间复杂度和 O(1)空间复杂度中运行。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/single-element-in-a-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0,len(nums)-1
        while left<right:
            mid = (left + right)//2
            if nums[mid] == nums[mid^1]:
                left = mid+1
            else:
                right = mid
        return nums[left]
"""
在这里巧用抑或（^）操作，如果mid是偶数，那么和1抑或的话，得到的就是mid+1，如果mid是奇数，得到的就是mid-1。
如果相等的话，那么唯一元素就在这之后了，往后找就行了，否则就在这之前。
"""


s = Solution()
print(s.singleNonDuplicate([1,1,2,3,3,4,4,8,8]))

