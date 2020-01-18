"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        巧用切片
        64 ms
        :param s:
        :return:
        """
        l = []
        res = []
        for x in s:
            if x not in l:
                l.append(x)
            else:
                res.append(len(l))
                i = l.index(x)
                l = l[i+1:]
                l.append(x)
        res.append(len(l))
        return max(res) if res else 0

def main():
    s = Solution()
    str = 'pwwkew'

    l = s.lengthOfLongestSubstring(str)
    print(l)
if __name__ == '__main__':
    main()