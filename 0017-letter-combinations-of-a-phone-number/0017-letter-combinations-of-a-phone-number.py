class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        numToLetter = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        
        res = []
        
        def dfs(cur, i):
            if i == len(digits):
                res.append(cur)
                return
            for c in numToLetter[digits[i]]:
                dfs(cur+c, i+1)
            
        if digits:
            dfs("", 0)
        return res