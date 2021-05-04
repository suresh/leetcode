#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:

        def traverse(l, r):
            if l > r:
                return

            m = (l + r)//2

            node = TreeNode(nums[m])
            node.left = traverse(l, m - 1)
            node.right = traverse(m + 1, r)

            return node

        return traverse(0, len(nums) - 1)
# @lc code=end
