#
#Title: 
#Difficulty:
#Language: Python3
#Author: Pranay Kotian

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        root = n = ListNode(0)
        arr = []
        
        #Adds all values from linked lists into array
        for i in range(len(lists)):
            while lists[i]:
                arr.append(lists[i].val)
                lists[i] = lists[i].next
        
        #Sorts values
        arr.sort()
        
        #Adds sorted values into linked list
        for i in arr:
            n.next = ListNode(i)
            n = n.next
        
        #Returns sorted linked list
        return root.next