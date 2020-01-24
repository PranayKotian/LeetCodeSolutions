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
        
        sumLink = 0
        mag = 1 
        while (not (l1 == None)) or (not (l2 == None)):
            if not (l1 == None):
                sumLink += mag * l1.val
                l1 = l1.next
            if not (l2 == None):
                sumLink += mag * l2.val
                l2 = l2.next
            
            mag *= 10
        
        root = n = ListNode(0)
        for i in str(sumLink)[::-1]:
            n.next = ListNode(int(i))
            n = n.next
        
        return root.next