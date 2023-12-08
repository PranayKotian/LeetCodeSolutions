# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1: return list2
        if not list2: return list1
        if list1.val > list2.val:
            res = list2
            list2 = list2.next
        else:
            res = list1
            list1 = list1.next
        cur = res
        
        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                cur = cur.next
                list1 = list1.next
            else: #list2.val <= list1.val:
                cur.next = list2
                cur = cur.next
                list2 = list2.next
        if list1:
            cur.next = list1 
        if list2:
            cur.next = list2
        return res
    
    '''
    [1,2,4]
    [1,3,4]
    '''