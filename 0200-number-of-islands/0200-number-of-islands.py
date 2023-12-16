class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])
        
        def markIsland(r,c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] != "1":
                return
            grid[r][c] = "2"
            markIsland(r+1,c)
            markIsland(r-1,c)
            markIsland(r,c+1)
            markIsland(r,c-1)
        
        res = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    res += 1
                    markIsland(i, j)
        
        return res