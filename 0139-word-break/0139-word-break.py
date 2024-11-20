class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        #Recursive Solution w/ Caching
        #Time: O(n^2) Space: O(n) 
        
        word_set = set(wordDict)
        
        @cache
        def check_word(word):
            if word in word_set:
                return True
            for i in range(len(word),0,-1):
                if word[:i] in word_set:
                    if check_word(word[i:]):
                        return True
            return False
        
        return check_word(s)