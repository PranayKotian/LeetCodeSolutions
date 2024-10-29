# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        #One Pass Solution
        #Time: O(n) Space: O(1)
        
        prev = ListNode(0, head)
        res = prev
        while head:
            if head.val == val:
                prev.next = head.next
                head = head.next
            else:
                head, prev = head.next, head
        return res.next
        