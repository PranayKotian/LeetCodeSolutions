class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        #Two Pass Solution
        #Time: O(n*m) Space: O(n+m)
        
        rows = set()
        cols = set()
        
        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    rows.add(r)
                    cols.add(c)
        
        for r in rows:
            for c in range(COLS):
                matrix[r][c] = 0
        for c in cols:
            for r in range(ROWS):
                matrix[r][c] = 0