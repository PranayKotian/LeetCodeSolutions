#https://leetcode.com/problems/shortest-path-in-binary-matrix/
#Title: 1091. Shortest Path in Binary Matrix
#Difficulty: Medium
#Language: Python
#Author: Pranay Kotian

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        
        queue = [(0,0)]
        visited = 1
        directions = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]
        
        while queue:
            for i in range(len(queue)):
                y,x = queue.pop(0)
                grid[y][x] = visited
                for a,b in directions:
                    ny = y + a
                    nx = x + b
                    if(ny<0 or nx<0 or ny>=n or nx>= n) or grid[ny][nx] != 0:
                        continue
                    grid[ny][nx] = 'Z'
                    queue.append((ny,nx))
            visited += 1
            
        if grid[n-1][n-1] == 0:
            return -1
        return grid[n-1][n-1]