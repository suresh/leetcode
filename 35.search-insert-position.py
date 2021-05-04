#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        l = [n for n, i in enumerate(nums) if i <= target]

        if l:
            if target in nums:
                pos = l[-1]
            else:
                pos = l[-1] + 1
        else:
            pos = 0

        return pos

# @lc code=end
