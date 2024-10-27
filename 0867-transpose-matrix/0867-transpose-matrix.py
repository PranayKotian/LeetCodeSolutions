class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        #Transpose Matrix Solution
        #Time: O(n) Space: O(1)
        
        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        res = []
        
        for c in range(COLS):
            res.append([])
            for r in range(ROWS):
                res[-1].append(matrix[r][c])
        
        return res