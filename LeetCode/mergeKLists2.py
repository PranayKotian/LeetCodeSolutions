#https://leetcode.com/problems/merge-k-sorted-lists/
#Title: 23. Merge k Sorted Lists
#Difficulty: Hard
#Language: Python3
#Author: Pranay Kotian

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        if (len(lists) == 0 or not lists):
            return None
        
        while len(lists) > 1:
            tempLists = []
            
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                
                if (i+1) < len(lists):
                    list2 = lists[i+1]
                else:
                    list2 = None
                    
                #condensed to:
                #list2 = lists[i+1] if (i+1) < len(lists) else None
                
                tempLists.append(self.mergeTwoLists(list1, list2))
            lists = tempLists
        
        return lists[0]
        
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        temp = cur = ListNode(0)
        
        while l1 and l2:
            if (l1.val < l2. val):
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        
        cur.next = l1 or l2
        return temp.next