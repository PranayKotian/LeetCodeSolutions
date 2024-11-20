class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        #Recursive Solution w/ Caching
        #Time: O(n^2) Space: O(n) 
        
        @cache
        def check_word(word):
            if word in wordDict:
                return True
            for i in range(len(word),0,-1):
                if word[:i] in wordDict:
                    if check_word(word[i:]):
                        return True
            return False
        
        return check_word(s)