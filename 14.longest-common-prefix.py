#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if strs == []:
            return ''

        # find the smallest string
        s = min(strs, key=len)
        sub_list = [s[:i+1] for i in range(len(s))]
        num = len(strs)
        # l = list(zip(*strs))

        res = ''
        for sub in sub_list:
            r = [e for e in strs if e.startswith(sub)]
            if len(r) == num:
                res = sub
            else:
                break
        # for i in l:
        #     if len(set(i)) == 1:
        #         res += i[0]
        #     else:
        #         break

        return res
# @lc code=end
