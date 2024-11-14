class Solution:
    def isValid(self, s: str) -> bool:
        
        #Stack Solution
        #Time: O(n) Space: O(n)
        
        stack = []
        for char in s:
            if char in ["(", "{", "["]:
                stack.append(char)
            else: 
                if not stack:
                    return False
                if char == ")": 
                    if stack[-1] != "(":
                        return False
                elif char == "}":
                    if stack[-1] != "{":
                        return False
                else: #char == "]":
                    if stack[-1] != "[":
                        return False
                stack.pop()
        return stack == []