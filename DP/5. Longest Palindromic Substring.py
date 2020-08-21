"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    ## DP
    # Time complexity:O(n^2)
    # Space complexity:O(n^2)
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_l = 1
        start = 0
        dp = [[False] * n for _ in range(n)]
        for j in range(1, n):
            for i in range(j):
                if s[i] == s[j]:
                    if j - i < 3: #1位数或者2位数的情况，此时为回文字符串
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                if dp[i][j]:
                    cur_l = j - i + 1
                    if cur_l > max_l:
                        max_l = cur_l
                        start = i

        return s[start:start + max_l]

s = Solution()
print(s.longestPalindrome('cbbd'))