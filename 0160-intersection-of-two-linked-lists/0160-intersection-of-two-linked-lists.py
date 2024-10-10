# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        #Set Solution
        #Time: O(a+b) Space: O(a)
        
        bag = set()
        while headA:
            bag.add(headA)
            headA = headA.next 
        
        while headB:
            if headB in bag:
                return headB
            headB = headB.next
        return None