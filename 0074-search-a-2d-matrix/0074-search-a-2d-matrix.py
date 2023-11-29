class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        l = 0
        r = ROWS*COLS-1

        #[r][c] format for 2D matrix
        while l <= r:
            idx = (l+r)//2
            x = idx % COLS #column value
            y = idx // COLS #row value

            if matrix[y][x] == target:
                return True
            if matrix[y][x] > target:
                r = idx-1
            else: #matrix[y][x] < target
                l = idx + 1
        return False