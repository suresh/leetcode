#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        carry = 0
        head = None
        temp = None

        while (l1 is not None or l2 is not None):

            s = carry

            if l1 is not None:
                s += l1.val
                l1 = l1.next
            if l2 is not None:
                s += l2.val
                l2 = l2.next

            carry = s // 10
            s = s % 10

            node = ListNode(s)

            if temp is None:
                temp = head = node
            else:
                temp.next = node
                temp = temp.next

        if carry > 0:
            temp.next = ListNode(carry)

        return head

# @lc code=end
