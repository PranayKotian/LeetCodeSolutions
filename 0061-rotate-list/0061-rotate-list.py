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
        
        last_elm = head
        len_list = 1
        while last_elm.next:
            len_list += 1
            last_elm = last_elm.next
        k = k%len_list
        
        if k == 0:
            return head
        
        last_elm.next = head
        first_elm = head
        for i in range(len_list-1-k):
            first_elm = first_elm.next
        first_elm.next, first_elm = None, first_elm.next
        
        return first_elm