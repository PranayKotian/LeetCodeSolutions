#https://leetcode.com/problems/add-two-numbers/
#Title: Add Two Numbers
#Difficulty: Medium
#Language: Python3
#Author: Pranay Kotian

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        #Sums the two numbers in the linked lists into an integer
        sumLink = 0
        mag = 1 
        while l1 or l2:
            if l1:
                sumLink += mag * l1.val
                l1 = l1.next
            if l2:
                sumLink += mag * l2.val
                l2 = l2.next
            mag *= 10
        
        #Converts integer to linked list to return
        root = n = ListNode(0)
        #root points to the first element of the linked list
        # therefore root.next will return the linked list (not including the initial node w/ 0)
        for i in str(sumLink)[::-1]:
            n.next = ListNode(int(i))
            n = n.next
        
        return root.next