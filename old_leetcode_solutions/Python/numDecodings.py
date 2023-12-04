#https://leetcode.com/problems/decode-ways/
#Title: 91. Decode Ways
#Difficulty: Medium
#Language: Python3
#Author: Pranay Kotian

class Solution:
    def numDecodings(self, s: str) -> int:
        dict = {"1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26"}
        
        n = len(s)
        arr = [0 for _ in range(n+1)]
        arr[0], arr[1] = 1, 1
        
        if (s[0] not in dict):
            return 0
        
        for i in range(2,n+1):
            if s[i-1] in dict:
                arr[i] += arr[i-1]
            if s[i-2]+s[i-1] in dict:
                arr[i] += arr[i-2]
        
        return arr[n]

        """
        Runtime: 32 ms, faster than 68.64% of Python3 online submissions for Decode Ways.
        Memory Usage: 14.1 MB, less than 84.67% of Python3 online submissions for Decode Ways.
        """