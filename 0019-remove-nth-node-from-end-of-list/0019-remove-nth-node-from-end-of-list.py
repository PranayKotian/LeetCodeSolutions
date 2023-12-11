# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:        
        n1 = head
        count = 1
        while n1.next:
            count += 1
            n1 = n1.next
        
        if count == n:
            return head.next
        
        res = head
        for i in range(count-n-1):
            head = head.next
        head.next = head.next.next
        
        return res