#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
from collections import OrderedDict
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        sub_list = list({s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)})
        sub_list.sort(key=len, reverse=True)

        for sub in sub_list:
            if sub == sub[::-1]:
                return sub
# @lc code=end

