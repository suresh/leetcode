#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        result = 0

        for i in range(len(prices)-1):
            profit = prices[i+1] - prices[i]

            if profit > 0: result += profit

        return result
        
# @lc code=end

