class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        #Recursive w/ Caching
        #Time: O(n^2) Space: O(n) 
        
        word_set = set(wordDict)
        
        @cache
        def check_word(word):
            if word in word_set:
                return True
            
            for i in range(len(word)):
                if word[:i+1] in word_set:
                    if check_word(word[i+1:]):
                        return True
            return False
        
        return check_word(s)