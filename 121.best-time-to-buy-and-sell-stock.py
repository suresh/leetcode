#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # get prices
        maxP, minP  = 0, float('inf')
                
        for p in prices:
            minP = min(minP, p)
            maxP = max(maxP, p-minP)

        return maxP
# @lc code=end

