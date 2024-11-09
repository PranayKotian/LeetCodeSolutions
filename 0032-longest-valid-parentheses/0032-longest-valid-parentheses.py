class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        #Stack Solution
        #Time: O(n) Space: O(n)
        
        stack = [-1]
        res = 0
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                if len(stack) == 1:
                    stack[0] = i
                else:
                    stack.pop()
                    res = max(res, i-stack[-1])
        return res