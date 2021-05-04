#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 0

        def height(root: TreeNode):
            if root is None:
                return -1

            left_depth, right_depth = height(root.left), height(root.right)
            self.ans = max(self.ans, 2+left_depth+right_depth)
            return 1 + max(left_depth, right_depth)

        height(root)
        return self.ans


# @lc code=end
