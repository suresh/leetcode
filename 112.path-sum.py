#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:

    #     if root is None:
    #         return False
       
    #     if (root.left is None and root.right is None):
    #         return (targetSum == root.val)
                
    #     return (self.hasPathSum(root.left, targetSum-root.val)) or (self.hasPathSum(root.right, targetSum-root.val))
    
    def __init__(self):
        self.hasPath = False
        self.targetSum = 0
        
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        self.targetSum = targetSum
        self.DFS(root, 0)
        return self.hasPath
        
    def DFS(self, curr, currSum):
        if not curr:
            return
        
        if self.hasPath:
            return
        
        currSum += curr.val
        
        if not curr.left and not curr.right:
            if currSum == self.targetSum:
                self.hasPath = True
            return
        
        self.DFS(curr.left, currSum)
        self.DFS(curr.right, currSum)
    
# @lc code=end

