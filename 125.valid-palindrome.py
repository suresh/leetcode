#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
import string


class Solution:
    def isPalindrome(self, s: str) -> bool:

        # clean up string
        s = s.replace(' ', '').lower()
        s = s.translate(str.maketrans(dict.fromkeys(string.punctuation)))

        if s == s[::-1]:
            return True
        else:
            return False

# @lc code=end
