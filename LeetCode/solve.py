#https://leetcode.com/problems/surrounded-regions/
#Title: 130. Surrounded Regions
#Difficulty: Medium
#Language: Python
#Author: Pranay Kotian

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        h = len(board)
        w = len(board[0])

                
        def dfs(y,x):
            board[y][x] = 'T'
                
            if (x-1 >= 0) and (x-1 <= w-1):
                if board[y][x-1] == 'O':
                    dfs(y,x-1)
            if (x+1 >= 0) and (x+1 <= w-1):
                if board[y][x+1] == 'O':
                    dfs(y,x+1)
            if (y-1 >= 0) and (y-1 <= h-1):
                if board[y-1][x] == 'O':
                    dfs(y-1,x)
            if (y+1 >= 0) and (y+1 <= h-1):
                if board[y+1][x] == 'O':
                    dfs(y+1,x)
                    
        for y in range(h):
            if y == 0 or y == h - 1:
                for x in range(w):
                    if board[y][x] == 'O':
                        dfs(y,x)
            else:
                for x in range(0, w, w-1):
                    if board[y][x] == 'O':
                        dfs(y,x)
        
        for i in range(h):
            for j in range(w):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'