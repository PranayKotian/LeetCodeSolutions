# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        #Four Pointers Linekd Lists Solution
        #Time: O(n) Space: O(1)
        
        res = start = prev = ListNode(0, head)
        lead = head
        count = 0
        while lead:
            lead = lead.next
            count += 1
            if count%k==0:
                head.next, prev, head = lead, head, head.next
                for i in range(k-1):
                    head.next, prev, head = prev, head, head.next
                start.next = prev
                for i in range(k-1):
                    prev = prev.next
                start = prev
        return res.next