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
        
        #O(n) time O(n) space solution
        q = deque()
        while head:
            q.append(head)
            head = head.next
                
        cur = q.popleft()
        res = cur
        count = 0
        while q:
            if count%2 == 0: 
                curnext = q.pop()    
            else: 
                curnext = q.popleft()
            cur.next = curnext
            cur = curnext
            count += 1
        cur.next = None
        
        #Alternate solution: O(n) time O(1) space
        #Find middle
        #Reverse second half 
        #Merge two halves