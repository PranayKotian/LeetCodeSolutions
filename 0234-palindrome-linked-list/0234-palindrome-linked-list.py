# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        #Solution 1: Two pass solution
        #Time: O(n) Space: N/A
        
        
        #Solution 2: One pass solution
        #Time: O(n) Space: O(n)
        
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        
        return arr == arr[::-1]