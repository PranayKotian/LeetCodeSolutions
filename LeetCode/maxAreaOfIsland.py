#https://leetcode.com/problems/max-area-of-island/
#Title: 695. Max Area of Island
#Difficulty: Medium
#Language: Python
#Author: Pranay Kotian

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        h = len(grid)
        w = len(grid[0])
        
        def dfs(y,x):
            if y < 0 or x < 0 or y >= h or x >= w or grid[y][x] != 1:
                return 0
            grid[y][x] = 2
            return 1 + dfs(y+1,x) + dfs(y-1,x) + dfs(y,x+1) + dfs(y,x-1)
            
        maxsize = 0
        
        for y in range(h):
            for x in range(w):
                if grid[y][x] == 1:
                    maxsize = max(maxsize, dfs(y,x))
        
        return maxsize