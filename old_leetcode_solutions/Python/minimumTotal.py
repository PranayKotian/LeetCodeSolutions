#https://leetcode.com/problems/triangle/
#Title: 120. Triangle
#Difficulty: Medium
#Language: Python3
#Author: Pranay Kotian

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        numLevels = len(triangle)
        
        for i in range(1,numLevels):
            prelevel = triangle[i-1]
            for j in range(len(triangle[i])):
                if j == len(prelevel):
                    minadd = prelevel[j-1]
                elif j == 0:
                    minadd = prelevel[0]
                else:
                    minadd = prelevel[j]
                    minadd = min(minadd, prelevel[j-1])
                    
                triangle[i][j] += minadd

        return min(triangle[numLevels-1])