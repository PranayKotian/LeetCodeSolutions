#https://leetcode.com/problems/knight-probability-in-chessboard/
#Title: 688. Knight Probability in Chessboard
#Difficulty: Medium
#Language: Python
#Author: Pranay Kotian

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        
        #find the probability of moving off the board at the starting position
        #multiply that by the probability of moving off the board at all resulting positions
        
        DIR = [(-2,-1),(-2,1),(2,-1),(2,1),(1,2),(-1,2),(1,-2),(-1,-2)]
        #cache = [[[-1]*(k+1) for _ in range(n)] for _ in range(n)]
        
        @lru_cache(None)
        def knightmove(moves,y,x):
            if y<0 or x<0 or y>=n or x>=n or moves==0:
                return 1
            
            on = 0
            temp = 0
            
            # if cache[y][x][moves] != -1:
            #     return cache[y][x][moves]
            
            for a,b in DIR:
                ny = y+a
                nx = x+b
                if ny<0 or nx<0 or ny>=n or nx>=n:
                    continue
                on += 1
                temp += knightmove(moves-1,ny,nx)
            
            if on != 0:
                ans = (on/8) * (temp/on)
            else:
                ans = on/8
            
            #cache[y][x][moves] = ans
            return ans
            
        return knightmove(k,row,column)