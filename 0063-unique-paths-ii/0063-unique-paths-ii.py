class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        #Solution 1: 2D Dynamic Programming Solution
        #Time: O(n*m)
        #Memo: O(n*m)
        
        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])
        
        arr = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        
        for r in range(ROWS):
            if obstacleGrid[r][0] == 1:
                break
            arr[r][0] = 1
        for c in range(COLS):
            if obstacleGrid[0][c] == 1:
                break
            arr[0][c] = 1
        
        for r in range(1,ROWS):
            for c in range(1,COLS):
                if obstacleGrid[r][c] == 0:
                    arr[r][c] = arr[r-1][c] + arr[r][c-1]
        
        return arr[-1][-1]