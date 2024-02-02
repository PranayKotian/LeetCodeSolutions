class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
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
        
        '''
        #Recursive DP Solution
        #Time: too inefficient without memoization Space:
        
        if s in wordDict:
            return True
        for i in range(1,len(s)):
            if s[i:] in wordDict:
                if self.wordBreak(s[:i], wordDict):
                    return True
        return False
        '''