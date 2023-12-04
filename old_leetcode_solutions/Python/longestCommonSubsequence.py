#https://leetcode.com/problems/longest-common-subsequence/
#Title: 1143. Longest Common Subsequence
#Difficulty: Medium
#Language: Python
#Author: Pranay Kotian

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        arr = [[0 for i in range(len(text1)+1)] for j in range(len(text2)+1)]
        
        for j in range(1,len(text2)+1):
            for i in range(1,len(text1)+1):
                if text2[j-1] == text1[i-1]:
                    arr[j][i] = arr[j-1][i-1] + 1
                else:
                    arr[j][i] = max(arr[j-1][i], arr[j][i-1])
        
        return arr[len(text2)][len(text1)]