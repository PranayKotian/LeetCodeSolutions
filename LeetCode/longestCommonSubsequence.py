#https://leetcode.com/problems/longest-common-subsequence/
#Title: Longest Common Subsequence
#Difficulty: Medium
#Language: Python3
#Author: Pranay Kotian

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        #intiialize empty 2D array of width and height of the text lengths
        rows, cols = (len(text1) + 1, len(text2) + 1)
        arr = [[0 for a in range(cols)] for b in range(rows)]
        
        for i in range(1, rows):
            for j in range(1, cols):
                if (text1[i-1] == text2[j-1]):
                    arr[i][j] = 1 + arr[i-1][j-1]
                else:
                    if arr[i-1][j] > arr[i][j-1]:
                        arr[i][j] =  arr[i-1][j]
                    else:
                        arr[i][j] =  arr[i][j-1]
        
        return arr[rows-1][cols-1]

        '''
        Runtime: 376 ms, faster than 90.77% of Python3 online submissions for Longest Common Subsequence.
        Memory Usage: 22.8 MB, less than 40.69% of Python3 online submissions for Longest Common Subsequence.
        '''