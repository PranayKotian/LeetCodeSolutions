class Solution:
    def numDecodings(self, s: str) -> int:
        #DP Solution
        #Time: O(n) Space: O(2)
        
        validNums = set([str(i) for i in range(1,27)])
        twoBack = 1
        oneBack = 1 if s[0] in validNums else 0
        
        for i in range(1,len(s)):
            cur = 0
            if s[i] in validNums:
                cur += oneBack
            if s[i-1:i+1] in validNums:
                cur += twoBack
            twoBack = oneBack
            oneBack = cur
        
        return oneBack