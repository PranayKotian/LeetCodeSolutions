class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        #Iterate through grid2
        #If grid2 square is island and grid1 is island
        # subisland += 1
        # dfs on grid2 to mark entire island
        
        subIslands = 0
        ROWS = len(grid1)
        COLS = len(grid1[0])
        
        def dfs(r,c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid2[r][c] == 0 or grid2[r][c] == 2:
                return True
            if grid1[r][c] == 0:
                return False
            grid2[r][c] = 2
            p1 = dfs(r+1,c)
            p2 = dfs(r-1,c)
            p3 = dfs(r,c+1)
            p4 = dfs(r,c-1)
            
            return p1 and p2 and p3 and p4
            
        for i in range(ROWS):
            for j in range(COLS):
                if grid1[i][j] == 1 and grid2[i][j] == 1:
                    if dfs(i,j):
                        subIslands += 1

        return subIslands