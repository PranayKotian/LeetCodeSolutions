#https://leetcode.com/problems/linked-list-cycle/
#Title: 141. Linked List Cycle
#Difficulty: Easy
#Language: Python3
#Author: Pranay Kotian

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        #HASH TABLE SOLUTION
        """
        seen = set()
        cur = head
        
        while cur:
            if cur not in seen:
                seen.add(cur)
                cur = cur.next
            else:
                return True
        return False
        """
    
        """
        Time: O(n), Space: O(n)
        Runtime: 48 ms, faster than 93.81% of Python3 online submissions for Linked List Cycle.
        Memory Usage: 18.2 MB, less than 6.91% of Python3 online submissions for Linked List Cycle.
        """
        