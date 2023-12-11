# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        #Solution 1: conversions
        #pass through both lists
        #convert to int
        #add the ints
        #convert to linked list
        
        s1 = str(l1.val)
        while l1.next:
            l1 = l1.next
            s1 = str(l1.val) + s1
        s2 = str(l2.val)
        while l2.next:
            l2 = l2.next
            s2 = str(l2.val) + s2
        total = int(s1) + int(s2)
        
        res = ListNode()
        p1 = res
        for c in str(total)[::-1]:
            p1.next = ListNode(int(c))
            p1 = p1.next
        return res.next
        
        #Solution 2: ??