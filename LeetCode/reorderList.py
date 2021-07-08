#https://leetcode.com/problems/reorder-list/
#Title: 143. Reorder List
#Difficulty: Medium
#Language: Python3
#Author: Pranay Kotian

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #find middle node
        midNode = fast = head
        while fast.next and fast.next.next:
            midNode = midNode.next
            fast = fast.next.next
        
        #reverse second half
        cur = midNode.next
        prev = None
        
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        midNode.next = None
        #prev is now at the end of the portion of the linked list
        # to be reversed (it is reversed starting from prev)
        
        #reorder list
        head1, head2 = head, prev
        
        while head2:
            head1 = head1.next
            head.next = head2
            head = head.next
            head2 = head2.next
            head.next = head1
            head = head.next
        
        # while head2:
        #     tmp = head1.next
        #     head1.next = head2
        #     head1 = head2
        #     head2 = tmp
        
        """
        Both average 120-140ms runtime, first has better memory usage
        
        Runtime: 128 ms, faster than 11.40% of Python3 online submissions for Reorder List.
        Memory Usage: 23.4 MB, less than 45.69% of Python3 online submissions for Reorder List.
        """