#https://leetcode.com/problems/remove-nth-node-from-end-of-list/
#Title: 19. Remove Nth Node From End of List
#Difficulty: Medium
#Language: Python3
#Author: Pranay Kotian

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        temp = ListNode(0)
        temp.next = head
        output = temp
        
        #finds the length of the linked list
        count = 0
        while head:
            count += 1
            head = head.next
        
        #edge case for length of 1
        if count == 1:
            return None
        
        #moves temp to position before Node to be removed
        count = count - n
        for i in range(count):
            temp = temp.next
        
        #skips the Node to be removed
        temp.next = temp.next.next
        
        #returns the linked list without the removed Node
        return output.next

        """
        Runtime: 36 ms, faster than 49.48% of Python3 online submissions for Remove Nth Node From End of List.
        Memory Usage: 14.2 MB, less than 46.70% of Python3 online submissions for Remove Nth Node From End of List.
        """