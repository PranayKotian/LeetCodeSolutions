# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #Floyd's Algorithm Constant Memory Solution
        #Time: O(n) Space: O(1)
        
        if head is None:
            return None
        
        start = ListNode(0, head)
        slow = head
        fast = head.next
        
        while slow != fast:
            if fast is None or fast.next is None:
                return None
            slow = slow.next
            fast = fast.next.next
        while start != fast:
            start = start.next
            fast = fast.next
        return start
        
        """
        #Set Solution
        #Time: O(n) Space: O(n)
        
        bag = set()
        while head:
            if head in bag:
                return head
            bag.add(head)
            head = head.next
        return None
        """