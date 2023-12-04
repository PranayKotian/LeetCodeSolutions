#https://leetcode.com/problems/number-of-enclaves/
#Title: 1020. Number of Enclaves
#Difficulty: Medium
#Language: Python
#Author: Pranay Kotian

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        #1. Convert all 1s connected to border to 2s
        LEN = len(grid)
        WID = len(grid[0])
        
        def dfs(y,x):
            if (y < 0 or x < 0 or y >= LEN or x >= WID) or (grid[y][x] != 1):
                return
            
            grid[y][x] = 2
            dfs(y-1,x)
            dfs(y+1,x)
            dfs(y,x-1)
            dfs(y,x+1)
        
        for i in range(LEN):
            for j in range(WID):
                if i in [0, LEN-1] or j in [0, WID-1]:
                    dfs(i,j)
        
        #2. Return the number of 1s remaining in the matrix
        out = 0
        for y in range(LEN):
            for x in range(WID):
                if grid[y][x] == 1:
                    out += 1
        return out