"""
给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:

输入: [10,9,2,5,3,7,101,18]
输出: 4
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
说明:

可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。
进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-increasing-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
# class Solution:
#     #DP
#     #Time complexity:O(n^2)
#     #Space complexity:O(n)
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         if not nums:
#             return 0
#         n = len(nums)
#         dp = [1]*n   # dp[i[表示以第i个数字结尾的最长上升子序列的长度，1个数字显然是长度为1的上升子序列。
#         for i in range(1,n):
#             for j in range(i):
#                 if nums[i]>nums[j]:
#                     dp[i] = max(dp[i], dp[j]+1)  #转移方程
#         return max(dp)


class Solution:
    # 以贪心和二分作为子过程
    # 参考： https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/dong-tai-gui-hua-er-fen-cha-zhao-tan-xin-suan-fa-p/
    #Time complexity:O(nlogn)
    #Space complexity:O(n)
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n<2:
            return n
        tail = [nums[0]]
        for i in range(1,n):
            #可以直接接在末尾的情况
            if nums[i]>tail[-1]:
                tail.append(nums[i])
                continue

            #使用二分查找，在有序数组tail中插入
            # 找到第一个大于nums[i]的元素，在之前插入
            left = 0
            right = len(tail)-1
            while left<right:
                mid = (left+right) >> 1
                if tail[mid]<nums[i]:
                    left = mid+1
                else:
                    right = mid
            tail[left] = nums[i]
        return len(tail)




s = Solution()
print(s.lengthOfLIS([10,9,2,5,3,7,101,18]))
