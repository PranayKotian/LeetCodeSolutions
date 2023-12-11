# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        #Optimal solution: O(n) time O(1) space
        #Find middle 
        if not head: return []
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        #Reverse second half
        prev, cur = None, slow.next
        while cur:
            cur.next, cur, prev = prev, cur.next, cur
        slow.next = None
        
        #Merge two halves
        head1, head2 = head, prev
        count = 0
        while head2:
            head1.next, head1, head2 = head2, head2, head1.next