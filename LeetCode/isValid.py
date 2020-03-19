#https://leetcode.com/problems/valid-parentheses/
#Title: Valid Parentheses
#Difficulty: Easy
#Language: Python3
#Author: Pranay Kotian

class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        
        #If closed paraentheses matches open parantheses at the top of the stack
        # delete that parantheses from the stack
        # else, add paraentheses to stack 
        # Valid parantheses if stack is empty in the end
        for i in s:
            
            #Checks if stack is empty
            if (i == ")" or i == "}" or i == "]") and len(stack) == 0:
                return False
            
            if (i == ")") and (stack[-1] == "("):
                del stack[-1]
            elif (i == "}") and (stack[-1] == "{"):
                del stack[-1]
            elif (i == "]") and (stack[-1] == "["):
                del stack[-1]
            else:
                stack.append(i)
        
        if len(stack) == 0:
            return True
        else:
            return False

        '''
        Runtime: 24 ms, faster than 90.46% of Python3 online submissions for Valid Parentheses.
        Memory Usage: 12.9 MB, less than 99.13% of Python3 online submissions for Valid Parentheses.
        '''
