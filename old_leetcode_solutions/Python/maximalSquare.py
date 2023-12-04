#https://leetcode.com/problems/last-stone-weight-ii/
#Title: 1049. Last Stone Weight II
#Difficulty: Medium
#Language: Python3
#Author: Pranay Kotian

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        h = len(matrix)
        w = len(matrix[0])
        
        cache = [[0 for i in range(w)] for j in range(h)]
        
        for i in range(w):
            if matrix[h-1][i] == "1":
                cache[h-1][i] = 1
        for j in range(h):
            if matrix[j][w-1] == "1":
                cache[j][w-1] = 1
        
        for y in range(h-2,-1,-1):
            for x in range(w-2,-1,-1):
                bot = cache[y+1][x]
                btr = cache[y+1][x+1]
                rgt = cache[y][x+1]
                
                if matrix[y][x] == "0":
                    cache[y][x] = 0
                else:
                    cache[y][x] = min(bot,btr,rgt) + 1
                    
        return max(max(cache, key=max))**2