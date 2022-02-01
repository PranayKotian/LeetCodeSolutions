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
        
        #QUEUE IMPLEMENTATION 
        q = deque()
        dummy = ListNode(0)
        dummy.next = head
        cur = head
        
        while cur:
            q.append(cur)
            cur = cur.next
        
        cur = dummy
        even = False
        while q:
            node = q.pop() if even else q.popleft()
            node.next = None
            cur.next = node
            cur = node
            even ^= True
        