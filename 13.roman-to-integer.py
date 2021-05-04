#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        sym_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
                   'D': 500, 'M': 1000, }

        # dbl_map = {'IV': 'IIII', 'IX': 'VIIII', 'XL': 'XXXX', 'XC': 'LXXXX',
        #            'CD': 'CCCC', 'CM': 'DCCCC'}
        # num = []

        # for k in dbl_map.keys():
        #     s = s.replace(k, dbl_map[k])
        s = s.replace('IV', 'IIII').replace('IX', 'VIIII').replace(
            'XL', 'XXXX').replace('XC', 'LXXXX')
        s = s.replace('CD', 'CCCC').replace('CM', 'DCCCC')

        s_list = list(s)
        num = [sym_map[e] for e in s_list]
        return sum(num)

# @lc code=end
