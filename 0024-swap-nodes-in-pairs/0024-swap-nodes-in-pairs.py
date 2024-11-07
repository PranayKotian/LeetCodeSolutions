# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #Linked List Solution
        #Time: O(n) Space: O(0)
        
        start = res = ListNode(0, head)
        
        while head and head.next:
            temp = head.next
            start.next = temp
            head.next = temp.next
            temp.next = head
            start = head
            head = head.next
            
        return res.next