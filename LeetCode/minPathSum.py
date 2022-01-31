#https://leetcode.com/problems/minimum-path-sum/
#Title: 64. Minimum Path Sum
#Difficulty: Medium
#Language: Python3
#Author: Pranay Kotian

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        h = len(grid)
        w = len(grid[0])
        
        for i in range(1,w):
            grid[0][i] += grid[0][i-1]
        for i in range(1,h):
            grid[i][0] += grid[i-1][0]    
        
        for i in range(1,h):
            for j in range(1,w):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        
        return grid[h-1][w-1]