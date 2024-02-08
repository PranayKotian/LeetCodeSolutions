# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #Solution 1: Standard Node Removal
        #Time: O(n) Space: O(1)
        
        dummy = ListNode(-101, head)
        prev = dummy
        while head:
            if head.val == prev.val:
                prev.next = head.next
            else:
                prev = head
            head = head.next
        return dummy.next