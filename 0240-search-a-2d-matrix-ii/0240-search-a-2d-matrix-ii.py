class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        #Diagonal Search
        #Time: O(n+m) Space: O(1)
        
        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        r = ROWS-1
        c = 0
        
        while c < COLS and r >= 0:
            val = matrix[r][c]
            if val == target:
                return True
            elif val > target:
                r -= 1
            else:
                c += 1
        return False
        
        
        #Binary Search Brute Force Solution
        #Time: O(mlogn) or O(nlogm) Space: O(1)
        
        
        