#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        
        def isMirror(node1: TreeNode, node2: TreeNode):
            if node1 is None and node2 is None:
                return True
        
            # check if sub-tree is reverse
            if node1 is not None and node2 is not None:
                if node1.val == node2.val:
                    return (isMirror(node1.left, node2.right) and isMirror(node1.right, node2.left))
                
            return False
        
        return isMirror(root, root)
# @lc code=end

