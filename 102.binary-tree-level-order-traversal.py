#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        if root is None:
            return []

#         result: List[List[int]] = []
#         visit = [root]

#         while visit:
#             next_visit = []
#             visited_val = []

#             for curr in visit:
#                 visited_val.append(curr.val)

#                 if curr.left: next_visit.append(curr.left)
#                 if curr.right: next_visit.append(curr.right)

#             visit = next_visit
#             result.append(visited_val)

        result: List[List[int]] = []
        level = [root]

        while root and level:
            result.append([node.val for node in level])
            temp = [(node.left, node.right) for node in level]
            level = [node for t in temp for node in t if node]

        return result
# @lc code=end
