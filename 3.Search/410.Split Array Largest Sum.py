"""
给定一个非负整数数组和一个整数 m，你需要将这个数组分成 m 个非空的连续子数组。设计一个算法使得这 m 个子数组各自和的最大值最小。

注意:
数组长度 n 满足以下条件:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)
示例:

输入:
nums = [7,2,5,10,8]
m = 2

输出:
18

解释:
一共有四种方法将nums分割为2个子数组。
其中最好的方式是将其分为[7,2,5] 和 [10,8]，
因为此时这两个子数组各自的和的最大值为18，在所有情况中最小。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/split-array-largest-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
class Solution:
    """
    这其实就是二分查找里的按值二分了，可以看出这里的元素就无序了。但是我们的目标是找到一个合适的最小和，换个角度理解我们要找的值在最小值max(nums)和sum(nums)内，而这两个值中间是连续的。是不是有点难理解，那么看代码吧
辅助函数的作用是判断当前的“最小和”的情况下，区间数是多少，来和m判断
这里的下界是数组的最大值是因为如果比最大值小那么一个区间就装不下，数组的上界是数组和因为区间最少是一个，没必要扩大搜索的范围
    """
    def splitArray(self, nums: List[int], m: int) -> int:
        def helper(mid):
            res = tmp = 0
            for num in nums:
                if tmp+num<=mid:
                    tmp+=num
                else:
                    res+=1
                    tmp = num
            return res+1

        left, right = max(nums), sum(nums)
        while left<right:
            mid = (left+right)//2
            if helper(mid)>m:
                left = mid+1
            else:
                right = mid
        return left


# class Solution:
#     #DP
#     #TODO
#     def splitArray(self, nums: List[int], m: int) -> int:
#         n = len(nums)
#         dp = [[1e18] * (m + 1) for _ in range(n + 1)]
#         sub = [0]
#         for i in nums:
#             sub.append(sub[-1] + i)
#
#         dp[0][0] = 0
#         for i in range(1, n + 1):
#             for j in range(1, min(i, m) + 1):
#                 for k in range(i):
#                     dp[i][j] = min(dp[i][j], max(dp[k][j - 1], sub[i] - sub[k]))
#
#         return dp[n][m]

s = Solution()
print(s.splitArray([7,2,5,10,8],2))