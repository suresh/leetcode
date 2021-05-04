#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = maxLength = 0
        usedChar = {}

        for i, c in enumerate(s):
            if c in usedChar and start <= usedChar[c]:
                start = usedChar[c] + 1
            else:
                maxLength = max(maxLength, i-start+1)
            usedChar[c] = i
        
        return maxLength
# @lc code=end

