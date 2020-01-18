"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: "cbbd"
Output: "bb"
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""

class Solution:
    # def longestPalindrome(self, s: str) -> str:
    #     """
    #     优先考虑最长回文串
    #     5008 ms
    #     :param s:
    #     :return:
    #     """
    #     if len(s)<=1:
    #         return s
    #     for length in range(len(s),0,-1):
    #         for i in range(0,len(s)-length+1):
    #             now_s = s[i:i+length]
    #             if now_s == now_s[::-1]:
    #                 return now_s
    def longestPalindrome(self, s: str) -> str:
        """
        48 ms
        :param s:
        :return:
        """
        if len(s)<2 or s == s[::-1]:
            return s
        # 定义起始索引和最大字符串长度，odd奇，even偶数
        start, maxlen = 0, 1

        for i in range(1,len(s)):
            odd = s[i-maxlen-1:i+1] # 去i及i前面的max+2个
            even = s[i-maxlen:i+1]
            if i-maxlen-1 >=0 and odd == odd[::-1]:
                start = i-maxlen-1
                maxlen +=2
                continue
            if i-maxlen>=0 and even == even[::-1]:
                start = i-maxlen
                maxlen+=1

        return s[start:start+maxlen]


def main():
    s = Solution()
    str = 'cbbd'

    l = s.longestPalindrome(str)
    print(l)

if __name__ == '__main__':
    main()