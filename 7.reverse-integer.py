#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        
        retval = int(str(abs(x))[::-1])
        
        if(retval.bit_length()>31):
            return 0
    
        if x<0:
            return -1*retval
        else:
            return retval
# @lc code=end

