#https://leetcode.com/problems/reverse-linked-list/
#Title: 206. Reverse Linked List
#Difficulty: Easy
#Language: Python3
#Author: Pranay Kotian

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        '''
        create an empty linked list
        get to the last element in the linked list
        go backwards and add to the empty list
        '''
        
        #prev is our new empty linked list
        prev = None
        
        #while head != None
        # loop ends once val of head == None
        
        while head:
            #curr assigned to the head value
            curr = head
            #head values moves up the linked list to the next value
            head = head.next
            #pointer for the curr value points to the previous value
            curr.next = prev
            #prev value shifted to the curr value
            prev = curr
        
        #the result is all the pointers will have flipped direction
        # prev will end on the last node which will point all the way backwards to the None value we initially assigned to prev
        
        return prev

        """
        Runtime: 36 ms, faster than 67.52% of Python3 online submissions for Reverse Linked List.
        Memory Usage: 15.7 MB, less than 42.80% of Python3 online submissions for Reverse Linked List.
        """

        """
        WITHOUT THE COMMENTS:
        Runtime: 28 ms, faster than 96.66% of Python3 online submissions for Reverse Linked List.
        Memory Usage: 15.5 MB, less than 92.35% of Python3 online submissions for Reverse Linked List.
        """