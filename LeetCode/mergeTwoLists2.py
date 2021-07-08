#https://leetcode.com/problems/merge-two-sorted-lists/
#Title: 21. Merge Two Sorted Lists
#Difficulty: Easy
#Language: Python3
#Author: Pranay Kotian

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur = ListNode(0)
        temp = cur
        
        while l1 and l2:
            if (l1.val > l2.val):
                cur.next = l2
                cur = l2
                l2 = l2.next
            else:
                cur.next = l1
                cur = l1
                l1 = l1.next
       
        if l1 == None:
            cur.next = l2
        else:
            cur.next = l1
        
        return temp.next

        """
        Runtime: 32 ms, faster than 92.22% of Python3 online submissions for Merge Two Sorted Lists.
        Memory Usage: 14.1 MB, less than 83.97% of Python3 online submissions for Merge Two Sorted Lists.
        """