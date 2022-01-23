#https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
#Title: Minimum Add to Make Parentheses Valid
#Difficulty: Medium
#Language: Python3
#Author: Pranay Kotian

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        arr = []
        for i in s:
            arr.append(i)
        
        repeat = True
        while repeat:
            repeat = False
            
            maxlen = len(arr) - 2
            c = 0
            while c <= maxlen:
                if arr[c] == "(" and arr[c+1] == ")":
                    del arr[c]
                    del arr[c]
                    repeat = True
                else:
                    c += 1
                maxlen = len(arr) - 2
        
        return len(arr)
    
        # Runtime: 64 ms, faster than 5.56% of Python3 online submissions for Minimum Add to Make Parentheses Valid.
        # Memory Usage: 14.3 MB, less than 10.32% of Python3 online submissions for Minimum Add to Make Parentheses Valid.
            