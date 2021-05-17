#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # pointer to current node
        current = head

        while (current is not None and current.next is not None):
            if current.next.val == current.val:
                current.next = current.next.next
            else:
                current = current.next
            
        return head


# @lc code=end

