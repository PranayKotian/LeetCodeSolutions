class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #Solution 1:
            #DFS all border Os and mark as dontflip
            #All others Os will be floipped
        
        ROWS = len(board)
        COLS = len(board[0])
        
        def dfs(r,c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != "O":
                return
            
            board[r][c] = "2"
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        for y in range(ROWS):
            dfs(y,0)
            dfs(y,COLS-1)
        for x in range(COLS):
            dfs(0,x)
            dfs(ROWS-1,x)
        
        for y in range(ROWS):
            for x in range(COLS):
                if board[y][x] == "2":
                    board[y][x] = "O"
                else:
                    board[y][x] = "X"
        
        return board