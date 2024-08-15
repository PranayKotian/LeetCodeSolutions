class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        #Copy Matrix Solution 
        #Time: O(n) Space: O(n)
        
        arr = []
        for row in matrix:
            arr += row
        
        index = 0
        for c in range(len(matrix[0])-1,-1,-1):
            for r in range(0, len(matrix)):
                matrix[r][c] = arr[index]
                index += 1