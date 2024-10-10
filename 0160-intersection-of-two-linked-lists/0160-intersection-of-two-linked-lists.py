# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        """
        #Elegant Constant Memory Solution
        #Time: O(a+b) Space: O(1)
        l1, l2 = headA, headB
        while l1 != l2:
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA
        return l1 #will either return intersection point or both lists will have gone to null
        """
        
        #Constant Memory Solution
        #Time: O(a+b) Space: O(1)
        
        a = headA
        b = headB
        aLen = bLen = 1
        while headA.next:
            aLen += 1
            headA = headA.next
        while headB.next:
            bLen += 1
            headB = headB.next
        if headA != headB:
            return None
        
        if aLen > bLen:
            for i in range(aLen-bLen):
                a = a.next
        elif bLen > aLen:
            for i in range(bLen-aLen):
                b = b.next
        
        while a != b:
            a = a.next
            b = b.next
        return a 
        
        """
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
        """