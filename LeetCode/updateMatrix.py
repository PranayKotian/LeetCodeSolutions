#https://leetcode.com/problems/01-matrix/
#Title: 542. 01 Matrix
#Difficulty: Medium
#Language: Python
#Author: Pranay Kotian

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        #mark all 1 cells as -1 (untouched)
        #add all zero cells to the queue
        #make all cells adjacent to these cells 0 + 1
        # make all cells adjacent to these cells 1 + 1
        
        
        h = len(mat)
        w = len(mat[0])
        
        queue = []
        
        for y in range(h):
            for x in range(w):
                if mat[y][x] == 1:
                    mat[y][x] = -1
                else:
                    queue.append((y,x))
        
        while queue:
            y,x = queue.pop(0)
            
            for c,r in [(1,0),(-1,0),(0,1),(0,-1)]:
                ny = y + c
                nx = x + r
                if ny < 0 or nx < 0 or ny >= h or nx >= w or mat[ny][nx] != -1:
                    continue
                mat[ny][nx] = mat[y][x] + 1
                queue.append((ny,nx))
        return mat