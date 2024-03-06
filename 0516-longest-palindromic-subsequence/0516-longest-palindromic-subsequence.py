class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        #Solution 1: Longest Common Subsequence Solution
        #Time: O(n^2) Space: O(n)
        
        s1 = s
        s2 = s[::-1]
        n = len(s)
        
        arr = [[0 for i in range(n+1)] for j in range(n+1)]
        
        for i in range(1,n+1):
            for j in range(1,n+1):
                if s1[i-1] == s2[j-1]:
                    arr[i][j] = arr[i-1][j-1] + 1
                else:
                    arr[i][j] = max(arr[i][j-1], arr[i-1][j])
        
        return arr[-1][-1]