class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def valid(i,j,val):
            for r in range(9): #checks column
                if board[r][j] == val:
                    return False
            for c in range(9): #checks row
                if board[i][c] == val:
                    return False
            
            sqrRow = (i//3)*3
            sqrCol = (j//3)*3
            for r in range(sqrRow,sqrRow+3):
                for c in range(sqrCol, sqrCol+3):
                    if board[r][c] == val:
                        return False
            return True
        
        def solve(grid):
            for r in range(9):
                for c in range(9):
                    if grid[r][c] == ".":
                        for n in ["1","2","3","4","5","6","7","8","9"]:
                            if valid(r,c,n):
                                grid[r][c] = n
                                if solve(grid):
                                    return True
                                grid[r][c] = "."
                        return False
            return True
        
        solve(board)