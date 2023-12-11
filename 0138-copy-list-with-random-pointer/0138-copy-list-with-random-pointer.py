"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        
        oldHeadPointer = head
        oldToNew = {}
        oldToNew[head] = Node(head.val)
        res = oldToNew[head]
        
        while head.next:
            head = head.next
            oldToNew[head] = Node(head.val)
        
        for node in oldToNew:
            if node.next is None:
                oldToNew[node].next = None
            else:
                oldToNew[node].next = oldToNew[node.next]
            if node.random is None:
                oldToNew[node].random = None
            else:
                oldToNew[node].random = oldToNew[node.random]
        
        return res
            