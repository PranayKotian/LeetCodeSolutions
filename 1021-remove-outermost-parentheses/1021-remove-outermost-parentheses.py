class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        
        #Constant Space Soltuion
        #Time: O(n) Space: O(1)
        
        openParens = 0
        res = []
        for char in s[1:]:
            if char == "(":
                if openParens >= 0:
                    res.append(char)
                openParens += 1
            else:
                if openParens != 0:
                    res.append(char)
                openParens -= 1
        return "".join(res)