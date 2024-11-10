# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #Set Solution
        #Time: O(n) Space: O(n)
        
        bag = set()
        while head:
            if head in bag:
                return head
            bag.add(head)
            head = head.next
        return None