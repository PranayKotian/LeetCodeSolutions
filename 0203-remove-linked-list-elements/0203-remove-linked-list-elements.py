# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        #Solution 2: Standard Linked List Node Removal (w/ Dummy Node)
        #Time: O(n) Space: N/A
        
        temp = ListNode(0, head)
        prev = temp
        while head:
            if head.val == val:
                prev.next = head.next
            else:
                prev = head
            head = head.next
        return temp.next