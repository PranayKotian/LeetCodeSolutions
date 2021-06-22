#https://leetcode.com/problems/unique-paths/
#Title: Unique Paths
#Difficulty: Medium
#Language: Python3
#Author: Pranay Kotian

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        arr2D = [[1 for i in range(n)] for _ in range(m)]

        for h in range(1,m):
            for w in range(1,n):
                arr2D[h][w] = arr2D[h-1][w] + arr2D[h][w-1]
        
        return arr2D[m-1][n-1]
    
        """
        Runtime: 32 ms, faster than 65.58% of Python3 online submissions for Unique Paths.
        Memory Usage: 14.5 MB, less than 13.69% of Python3 online submissions for Unique Paths.
        """