class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        
        #Constant Space Soltuion
        #Time: O(n) Space: O(1)
        
        res = ""
        openParens = 0
        for char in s:
            if char == "(":
                if openParens > 0:
                    res += char
                openParens += 1
            else:
                if openParens > 1:
                    res += char
                openParens -= 1
        return res