"""
给定一个未经排序的整数数组，找到最长且连续的的递增序列，并返回该序列的长度。

 

示例 1:

输入: [1,3,5,4,7]
输出: 3
解释: 最长连续递增序列是 [1,3,5], 长度为3。
尽管 [1,3,5,7] 也是升序的子序列, 但它不是连续的，因为5和7在原数组里被4隔开。
示例 2:

输入: [2,2,2,2,2]
输出: 1
解释: 最长连续递增序列是 [2], 长度为1。
 

注意：数组长度不会超过10000。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-continuous-increasing-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
class Solution:
    # DP
    # Time Complexity:O(n)
    # Space Complexity:O(n)
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n<2:
            return n
        dp = [1]*n
        for i in range(1,n):
            if nums[i]>nums[i-1]: #判断每个元素，只与前一个元素有关
                dp[i] = dp[i-1]+1
        return max(dp)

s = Solution()
print(s.findLengthOfLCIS([1,3,5,4,7]))
