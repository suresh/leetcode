#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:

        visited = set()
        temp = head

        while temp:
            # check if the node is already visited
            if temp in visited:
                return True
            # add the node to visited
            visited.add(temp)
            temp = temp.next

        return False    
# @lc code=end

