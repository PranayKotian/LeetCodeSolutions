#https://leetcode.com/problems/as-far-from-land-as-possible/
#Title: 1162. As Far from Land as Possible
#Difficulty: Medium
#Language: Python
#Author: Pranay Kotian

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
            
            #0 can be treated as unsearched
            #iterate through land cells (1)
            # all adjacent cells have a distance from land of 1
            # repeat until max distance from land is found
            
            maxdis = 0
            h = len(grid) 
            w = len(grid[0])
            
            queue = []
            
            for y in range(h):
                for x in range(w): 
                    if grid[y][x] == 1:
                        queue.append([y,x])
            
            while queue:
                y,x = queue.pop(0)
                
                for a,b in [(1,0),(-1,0),(0,1),(0,-1)]:
                    ny = y + a
                    nx = x + b
                    if ny<0 or nx<0 or ny>=h or nx>=w or grid[ny][nx] != 0:
                        continue
                    grid[ny][nx] = grid[y][x] + 1
                    maxdis = max(maxdis, grid[ny][nx])
                    queue.append([ny,nx])
            
            return maxdis - 1