#https://leetcode.com/problems/merge-two-sorted-lists/
#Title: Merge Two Sorted Lists
#Difficulty: Easy
#Language: Python3
#Author: Pranay Kotian

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = n = ListNode(0)
        while l1 and l2:
            if (l1.val > l2.val):
                n.next = ListNode(l2.val)
                n = n.next
                l2 = l2.next
            else: #(l2.val > l1.val) or l2.val == l1.val
                n.next = ListNode(l1.val)
                n = n.next
                l1 = l1.next
        while l1:
            n.next = ListNode(l1.val)
            n = n.next
            l1 = l1.next
        while l2:
            n.next = ListNode(l2.val)
            n = n.next
            l2 = l2.next
                
        return root.next

        """
        root = n = ListNode(0)
        while l1 or l2:
            if l1 and l2:
                if (l1.val > l2.val):
                    n.next = ListNode(l2.val)
                    n = n.next
                    l2 = l2.next
                elif (l2.val > l1.val):
                    n.next = ListNode(l1.val)
                    n = n.next
                    l1 = l1.next
                else:
                    n.next = ListNode(l1.val)
                    n = n.next
                    n.next = ListNode(l2.val)
                    n = n.next
                    l1 = l1.next
                    l2 = l2.next

            elif l1:
                n.next = ListNode(l1.val)
                n = n.next
                l1 = l1.next
            elif l2:
                n.next = ListNode(l2.val)
                n = n.next
                l2 = l2.next
                
        return root.next
        """