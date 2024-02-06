class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        #Solution 1: Dynamic Programming
        #Time: O(n*m) Space: O(n*m)
        
        ROWS = len(matrix)
        COLS = len(matrix[0])
        cache = {}
        
        def dfs(r,c,prev):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or matrix[r][c] <= prev:
                return 0
            if (r,c) not in cache:
                cur=matrix[r][c]
                cache[(r,c)] = 1 + max(dfs(r+1,c,cur),dfs(r-1,c,cur),dfs(r,c+1,cur),dfs(r,c-1,cur))
            return cache[(r,c)]
        
        for i in range(ROWS):
            for j in range(COLS):
                dfs(i,j,-1)
        
        return max(cache.values())