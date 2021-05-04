#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        l, r = 0, 0
        if root.left is not None:
            l = self.maxDepth(root.left)
        if root.right is not None:
            r = self.maxDepth(root.right)


        return max(l+1, r+1)
# @lc code=end

