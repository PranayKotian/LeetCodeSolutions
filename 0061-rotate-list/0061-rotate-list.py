# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        #Merge Linked Lists Solution
        #Time: O(n) Space: O(1)
        
        if not head:
            return None
        
        p1 = head
        len_list = 0
        while p1:
            len_list += 1
            p1 = p1.next
        k = k%len_list
        
        if k == 0:
            return head

        p2 = head
        for i in range(len_list-1-k):
            p2 = p2.next
        
        p2.next, p2 = None, p2.next
        res = p2
        for i in range(k-1):
            p2 = p2.next
        p2.next = head
        
        return res