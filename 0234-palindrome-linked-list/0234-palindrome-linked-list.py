# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        #Constant Space Solution
        #Time: O(n) Space: O(1)
        #Fast & slow pointer + reverse first half of linked list
        
        nodes = 0
        cur = head
        while cur:
            nodes += 1
            cur = cur.next
        
        prev = None
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow.next, prev, slow = prev,slow,slow.next
        
        if nodes%2 == 1:
            slow = slow.next
        while prev and slow:
            if slow.val != prev.val:
                return False
            prev = prev.next
            slow = slow.next
        
        return True
        
        #Extra Space Solution
        #Time: O(n) Space: O(n)
        #Store linked list in array, check if array is palindrome (arr == arr[::-1])