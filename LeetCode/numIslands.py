#https://leetcode.com/problems/number-of-islands/
#Title: 200. Number of Islands
#Difficulty: Medium
#Language: Python
#Author: Pranay Kotian

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        h = len(grid)
        w = len(grid[0])
        out = 0
        
        def dfs(y,x):
            if y < 0 or x < 0 or y >= h or x >= w or grid[y][x] != "1":
                return
            
            grid[y][x] = "2"
            
            dfs(y+1,x)
            dfs(y-1,x)
            dfs(y,x+1)
            dfs(y,x-1)
        
        for y in range(h):
            for x in range(w):
                if grid[y][x] == "1": 
                    out += 1
                    dfs(y,x)
                    
        return out