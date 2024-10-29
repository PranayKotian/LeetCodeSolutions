# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #Node Removal Solution
        #Time: O(n) Space: N/A
        
        temp = ListNode(-101, head)
        prev = temp
        while head:
            if head.val == prev.val:
                prev.next = head.next
            else:
                prev = head
            head = head.next
        return temp.next