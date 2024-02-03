class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        #DP solution
        #Time: O(n*m) Space: O(n*m)
        
        n = len(text1)
        m = len(text2)
        
        arr = [[0 for _ in range(n+1)] for _ in range(m+1)]
        
        for r in range(1,m+1):
            for c in range(1,n+1):
                if text1[c-1] == text2[r-1]:
                    arr[r][c] = arr[r-1][c-1] + 1
                else:
                    arr[r][c] = max(arr[r-1][c], arr[r][c-1])
        
        return arr[-1][-1]