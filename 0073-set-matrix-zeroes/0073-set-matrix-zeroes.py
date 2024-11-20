class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
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
        