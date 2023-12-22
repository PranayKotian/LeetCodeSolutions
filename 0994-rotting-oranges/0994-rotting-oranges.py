class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        #O(n*m)        
        ROWS = len(grid)
        COLS = len(grid[0])
        
        count = 0
        prev = sum([row.count(1) for row in grid])+1
        cur = prev-1
        
        def rot(r,c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] != 1:
                return
            grid[r][c] = 1.5
        
        def convert():
            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] == 1.5:
                        grid[r][c] = 2
        
        while prev != cur:
            prev = sum([row.count(1) for row in grid])
            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] == 2:
                        rot(r+1,c)
                        rot(r-1,c)
                        rot(r,c+1)
                        rot(r,c-1)
            cur = sum([row.count(1) for row in grid])
            convert() 
            count += 1
        
        if cur == 0:
            return count-1
        return -1
            