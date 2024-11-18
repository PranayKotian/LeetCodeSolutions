class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        #Brute Force Backtracking Solution
        #Time: O(2^n) Space: O(n)
        
        res = []
        def generate(cur: str, openParens: int, closeParens: int):
            if len(cur) == n*2:
                res.append(cur)
                return
            if openParens < n:
                generate(cur+"(", openParens+1, closeParens)
            if closeParens < openParens:
                generate(cur+")", openParens, closeParens+1)
        generate("", 0, 0)
        return res