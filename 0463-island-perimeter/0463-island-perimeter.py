class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        #Solution 1: Recursive DFS
        #Time: O(n*m) Space: O(1)
        
        ROWS = len(grid)
        COLS = len(grid[0])
        
        def dfs(r,c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0:
                return 1
            if grid[r][c] == 2:
                return 0
            grid[r][c] = 2
            return dfs(r-1,c) + dfs(r+1,c) + dfs(r,c-1) + dfs(r,c+1)
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    return dfs(i,j)
                    