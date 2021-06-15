#https://leetcode.com/problems/word-break/
#Title: Word Break
#Difficulty: Medium
#Language: Python3
#Author: Pranay Kotian

class Solution:
    memo = {}
    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        stringLen = len(s)
                
        if s in wordDict:
            self.memo.clear()
            return True
        
        for i in range(1, stringLen):
            if s[0:i] in wordDict:
                tempStr = s[i:stringLen]
                if tempStr not in self.memo.keys():
                    self.memo[tempStr] = self.wordBreak(tempStr, wordDict)  
                if (self.memo[tempStr]):
                    self.memo.clear()
                    return True
        
        self.memo.clear()
        return False