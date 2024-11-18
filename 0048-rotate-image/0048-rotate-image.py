class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        #Matrix Manipulations Solution
        #Time: O(n) Space: N/A
        
        #Mirror matrix
        n = len(matrix)
        #Transpose matrix
        matrix.reverse()
        for r in range(n):
            for c in range(r+1,n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        