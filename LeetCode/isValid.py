#https://leetcode.com/problems/valid-parentheses/
#Title: Valid Parentheses
#Difficulty: East
#Language: Python3
#Author: Pranay Kotian

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if (i == ")"):
                if stack[-1] == "(":
                    del stack[-1]
                
            if (i == "}"):
                if stack[-1] == "(":
                    del stack[-1]
                
            if (i == "]"):
                if stack[-1] == "(":
                    del stack[-1]