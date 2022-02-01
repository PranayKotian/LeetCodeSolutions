#https://leetcode.com/problems/unique-paths/
#Title: 62. Unique Paths
#Difficulty: Medium
#Language: Python3
#Author: Pranay Kotian

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
            
        arr = [[1 for i in range(n)] for j in range(m)]
        
        for y in range(1,m):
            for x in range(1,n):
                arr[y][x] = arr[y-1][x] + arr[y][x-1]
        
        return arr[m-1][n-1]