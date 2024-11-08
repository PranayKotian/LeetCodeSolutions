class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        #Dynamic Programming Solution
        #Time: O(n*m) Space: O(n*m)
        
        #m rows
        #n columns
        
        paths = [[1 for i in range(n)] for i in range(m)]
        for r in range(1,m):
            for c in range(1,n):
                paths[r][c] = paths[r-1][c] + paths[r][c-1]
        return paths[-1][-1]