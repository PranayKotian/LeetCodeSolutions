#https://leetcode.com/problems/coloring-a-border/
#Title: 1034. Coloring A Border
#Difficulty: Medium
#Language: Python
#Author: Pranay Kotian

class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        
        def dfs(y,x):
            if y<0 or x<0 or y>=h or x>=w or grid[y][x] != origColor:
                return
                
            recolor = False
            for a,b in directions:
                ny = y + a
                nx = x + b
                if (ny<0 or nx<0 or ny>=h or nx>=w) or (grid[ny][nx] != origColor and grid[ny][nx] != -2):
                    recolor = True

            if recolor:
                recolorgrid[y][x] = -1
            grid[y][x] = -2
            
            dfs(y+1,x)
            dfs(y-1,x)
            dfs(y,x+1)
            dfs(y,x-1)
        
        h = len(grid)
        w = len(grid[0])
        origColor = grid[row][col]
        recolorgrid = [[0 for i in range(w)] for j in range(h)]
        print(recolorgrid)
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        
        dfs(row,col)
        
        for y in range(h):
            for x in range(w):
                if recolorgrid[y][x] == -1:
                    grid[y][x] = color
                elif grid[y][x] == -2:
                    grid[y][x] = origColor
        
        return grid