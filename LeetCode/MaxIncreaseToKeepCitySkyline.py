//https://leetcode.com/problems/max-increase-to-keep-city-skyline/
//Title: Max Increase to Keep City Skyline
//Difficulty: Medium
//Language: Python3
//Author: Pranay Kotian

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        topBotMax = []
        leftRightMax = []
        
        max1 = 0
        max2 = 0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] > max1:
                    max1 = grid[i][j]
                if grid[j][i] > max2:
                    max2 = grid[j][i]
            leftRightMax.append(max1)
            max1 = 0
            topBotMax.append(max2)
            max2 = 0
        
        maxAdd = 0
        for i in range(rows):
            for j in range(cols):
                if topBotMax[j] > leftRightMax[i]:
                    maxAdd += leftRightMax[i] - grid[i][j]
                else:
                    maxAdd += topBotMax[j] - grid[i][j]
        return maxAdd
                