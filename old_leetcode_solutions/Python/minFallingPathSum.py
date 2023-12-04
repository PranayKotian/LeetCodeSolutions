#https://leetcode.com/problems/minimum-falling-path-sum/
#Title: 931. Minimum Falling Path Sum
#Difficulty: Medium
#Language: Python3
#Author: Pranay Kotian

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        h = len(matrix)
        w = len(matrix[0])
        
        directions = [(-1,-1),(-1,0),(-1,1)]
        
        for y in range(1,h):
            for x in range(0,w):
                
                minval = 10**100
                
                for a,b in directions:
                    ny = y + a
                    nx = x + b
                    if ny<0 or nx<0 or ny>=h or nx>=w:
                        continue
                    minval = min(minval, matrix[ny][nx])
                
                matrix[y][x] += minval
        
        res = matrix[h-1][0]
        for x in range(1,w):
            res = min(res, matrix[h-1][x])
        
        return res