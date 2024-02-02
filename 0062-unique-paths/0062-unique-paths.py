class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #2D DP Solution
        #Time: O(n*m) Space: O(n*m)
        
        arr = [[1 for i in range(m)] for j in range(n)]
        
        for i in range(1,m):
            for j in range(1,n):
                arr[j][i] = arr[j-1][i] + arr[j][i-1]
        
        return arr[-1][-1]