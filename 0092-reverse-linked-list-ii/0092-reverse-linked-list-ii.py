# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        #One Pass Solution
        #Time: O(n) Space: O(1) 
        
        res = head = ListNode(0, head)
        for i in range(left-1):
            head = head.next
        
        start = prev = head
        for i in range(right-left+2):
            prev = prev.next
        head = head.next
        
        for i in range(right-left+1):
            head.next, prev, head = prev, head, head.next
        start.next = prev
        
        return res.next