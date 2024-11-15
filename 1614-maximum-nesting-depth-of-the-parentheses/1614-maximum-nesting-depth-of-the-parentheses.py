class Solution:
    def maxDepth(self, s: str) -> int:
        
        #Count Parens Solution
        #Time: O(n) Space: O(1)
        
        res = 0
        openParens = 0
        for char in s:
            if char == "(":
                openParens += 1
                res = max(res,openParens)
            elif char == ")":
                openParens -= 1
        return res