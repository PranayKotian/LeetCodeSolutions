class Solution:
    def scoreOfParentheses(self, s: str) -> int:

        #Wonky Stack Solution
        #Time: O(n) Space: O(n)
        
        stack = []
        for char in s:
            print(stack)
            if char == "(":
                stack.append(char)
            else: #char == ")"
                if stack[-1] == "(":
                    stack.pop()
                    if stack and stack[-1] != "(":
                        stack[-1] += 1
                    else:
                        stack.append(1)
                else: #top of stack is a score
                    val = stack.pop() * 2
                    stack.pop()
                    if stack and stack[-1] != "(":
                        stack[-1] += val
                    else:
                        stack.append(val)
        return stack[0]