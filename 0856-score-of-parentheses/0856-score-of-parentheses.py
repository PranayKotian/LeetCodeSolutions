class Solution:
    def scoreOfParentheses(self, s: str) -> int:

        #Stack Solution
        #Time: O(n) Space: O(n)
        
        stack = []
        for char in s:
            if char == "(":
                stack.append(char)
            else: 
                val = 1 if stack[-1] == "(" else stack.pop()*2
                stack.pop()
                if stack and stack[-1] != "(":
                    stack[-1] += val
                else:
                    stack.append(val)
        return stack[0]