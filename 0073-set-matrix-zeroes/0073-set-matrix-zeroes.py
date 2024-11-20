class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        #Constant Space Solution
        #Time: O(nm) Space: O(1)
        
        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        first_row = False
        first_col = False
        
        for r in range(ROWS):
            if matrix[r][0] == 0:
                first_col = True
                break
        for c in range(COLS):
            if matrix[0][c] == 0:
                first_row = True
                
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        for r in range(1,ROWS):
            for c in range(1,COLS):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        if first_row:
            for c in range(COLS):
                matrix[0][c] = 0
        if first_col: 
            for r in range(ROWS):
                matrix[r][0] = 0
        
        """
        #Rows + Columns Solution
        #Time: O(nm) Space: O(n+m)
        
        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        zero_rows = set()
        zero_cols = set()
        
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    zero_rows.add(r)
                    zero_cols.add(c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if r in zero_rows or c in zero_cols:
                    matrix[r][c] = 0
        """