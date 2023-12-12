# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        #Solution 2: generate answer while passing through l1, l2
        carry = 0
        head = res = ListNode()
        while l1 or l2 or carry:
            cur = carry
            if l1:
                cur += l1.val
                l1 = l1.next
            if l2:
                cur += l2.val
                l2 = l2.next
            carry, cur = divmod(cur, 10)
            head.next = ListNode(cur)
            head = head.next
        return res.next