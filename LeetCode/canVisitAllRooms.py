#https://leetcode.com/problems/keys-and-rooms/
#Title: 841. Keys and Rooms
#Difficulty: Medium
#Language: Python
#Author: Pranay Kotian

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        #number of rooms
        n = len(rooms)
        visited = set()
        
        def dfs(r):
            visited.add(r)
            keys = rooms[r]
            
            for k in keys:
                if k not in visited:
                    dfs(k)
        
        dfs(0)
        
        if len(visited) != n:
            return False
        return True