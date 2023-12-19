class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        
        def dfs(r,c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or grid[r][c] != 1:
                return 0
            
            grid[r][c] = 2
            a1 = dfs(r+1,c)
            a2 = dfs(r-1,c)
            a3 = dfs(r,c+1)
            a4 = dfs(r,c-1)
            
            return 1 + a1 + a2 + a3 + a4
        
        maxArea = 0
        for x in range(ROWS):
            for y in range(COLS):
                if grid[x][y] == 1:
                    maxArea = max(maxArea, dfs(x,y))
    
        return maxArea