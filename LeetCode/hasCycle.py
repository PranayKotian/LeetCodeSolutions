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
        
        #SLOW/FAST POINTER SOLUTION
        #if the pointers ever meet that means there is a loop
        #if both pointers reach the end that means there is no loop
        slow = fast = head
        
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if (slow == fast):
                return True
        return False

        """
        Time: O(n), Space: O(1)
        Runtime: 56 ms, faster than 59.08% of Python3 online submissions for Linked List Cycle.
        Memory Usage: 17.5 MB, less than 92.68% of Python3 online submissions for Linked List Cycle.
        """

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
        