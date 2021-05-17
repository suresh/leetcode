#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:

    def maxSubArray(self, nums: List[int]) -> int:

        # Approach 1 - go through array one time to find max
        max_sum_i = max_sum = nums[0]

        for i in range(1, len(nums)):
            max_sum_i = max(max_sum_i+nums[i], nums[i])
            max_sum = max(max_sum, max_sum_i)

        return max_sum

        # # Approach 2 - Divide and Conquer
        # return self.max_sum_helper(nums, 0, len(nums)-1)

    def max_sum_helper(self, nums, l, r):

        if l > r:
            return -2147483647

        m = (l+r) // 2  # find midpoint

        left_max = sum_nums = 0
        for i in range(m-1, l-1, -1):
            sum_nums += nums[i]
            left_max = max(left_max, sum_nums)

        right_max = sum_nums = 0
        for i in range(m+1, r+1):
            sum_nums += nums[i]
            right_max = max(right_max, sum_nums)

        left_half = self.max_sum_helper(nums, l, m-1)
        right_half = self.max_sum_helper(nums, m+1, r)

        return max(left_max + nums[m] + right_max, max(left_half, right_half))

# @lc code=end
