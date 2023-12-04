#https://leetcode.com/problems/out-of-boundary-paths/
#Title: 576. Out of Boundary Paths
#Difficulty: Medium
#Language: Python
#Author: Pranay Kotian

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        
        @lru_cache(None)
        def movetrace(y,x,moves):
            if y<0 or x<0 or y==m or x==n:
                return 1
            if moves == 0:
                return 0

            a = movetrace(y+1,x,moves-1)
            b = movetrace(y-1,x,moves-1)
            c = movetrace(y,x+1,moves-1)
            d = movetrace(y,x-1,moves-1)
        
            return a + b + c + d
        
        return movetrace(startRow, startColumn, maxMove) % (10**9+7)