#https://leetcode.com/problems/number-of-closed-islands/
#Title: 1254. Number of Closed Islands
#Difficulty: Medium
#Language: Python
#Author: Pranay Kotian

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        
        #iterate through border 
        # eliminate all islands connected to the border (0 --> B)
        #iterate through inner grid, count all islands 
        # find 0, DFS/BFS through island (0--> I), increment output
        
        h = len(grid)
        w = len(grid[0])
        out = 0
        
        def dfs(y,x):
            if y < 0 or x < 0 or y >= h or x >= w or grid[y][x] != 0:
                return
            
            grid[y][x] = 2
            
            dfs(y+1,x)
            dfs(y-1,x)
            dfs(y,x+1)
            dfs(y,x-1)
        
        for y in range(h):
            for x in range(w):
                if (y in [0, h-1] or x in [0, w-1]) and grid[y][x] == 0:
                    dfs(y,x)
                    
        for y in range(1, h-1):
            for x in range(1, w-1):
                if grid[y][x] == 0:
                    out += 1
                    dfs(y,x)
                
        return out 