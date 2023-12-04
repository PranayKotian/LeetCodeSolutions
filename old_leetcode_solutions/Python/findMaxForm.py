#https://leetcode.com/problems/ones-and-zeroes/
#Title: 474. Ones and Zeroes
#Difficulty: Medium
#Language: Python3
#Author: Pranay Kotian

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        arr = [[0 for i in range(m+1)] for j in range(n+1)]
        
        for s in strs:
            n1 = s.count("1")
            n0 = s.count("0")
            
            for y in range(n,n1-1,-1):
                for x in range(m,n0-1,-1):
                    arr[y][x] = max(arr[y][x], arr[y-n1][x-n0]+1)
            
        return arr[n][m]