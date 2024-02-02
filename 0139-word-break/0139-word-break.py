class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        #DP Solution w/o Recursion
        valid = [False]*(len(s)+1)
        valid[0] = True
        
        for i in range(len(s)):
            for w in wordDict:
                if w == s[i:i+len(w)] and valid[i]:
                    valid[i+len(w)] = True
        return valid[-1]
        
        """
        #Recursive DP solution w/ cheater memoization
        @lru_cache(None)
        def dfs(w):
            if w in wordDict:
                return True
            for word in wordDict:
                if w[:len(word)] == word:
                    if dfs(w[len(word):]):
                        return True
            return False
        
        return dfs(s)
        """