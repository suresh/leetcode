#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = Counter(nums)

        return counter.most_common()[-1][0]
# @lc code=end

