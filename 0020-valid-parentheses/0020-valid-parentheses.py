class Solution:
    def isValid(self, s: str) -> bool:
        
        #Stack Solution
        #Time: O(n) Space: O(n)
        
        parens = {")": "(", "}": "{", "]": "["}
        stack = []
        for char in s:
            if char not in parens:
                stack.append(char)
            else: 
                if not stack or stack[-1] != parens[char]:
                    return False
                stack.pop()
        return stack == []