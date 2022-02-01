#https://leetcode.com/problems/unique-paths-ii/
#Title: 63. Unique Paths II
#Difficulty: Medium
#Language: Python3
#Author: Pranay Kotian

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        h = len(obstacleGrid)
        w = len(obstacleGrid[0])
        
        for y in range(h):
            for x in range(w):
                if obstacleGrid[y][x] == 1: 
                    obstacleGrid[y][x] = 0
                else:
                    obstacleGrid[y][x] = 1
        
        print(obstacleGrid)
        
        for y in range(1, h):
            obstacleGrid[y][0] *= obstacleGrid[y-1][0]
        for x in range(1, w):
            obstacleGrid[0][x] *= obstacleGrid[0][x-1]
            
        for y in range(1,h):
            for x in range(1,w):
                if obstacleGrid[y][x] == 1:
                    obstacleGrid[y][x] = obstacleGrid[y-1][x] + obstacleGrid[y][x-1]
        
        print(obstacleGrid)
        
        return obstacleGrid[h-1][w-1]