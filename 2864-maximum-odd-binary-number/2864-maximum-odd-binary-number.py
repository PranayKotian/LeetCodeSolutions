class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        
        #Greedy Solution
        #Time: O(n) Space: O(n)
        
        numOnes = -1
        for c in s:
            if c == "1":
                numOnes += 1
                
        res = ""
        for i in range(numOnes):
            res += "1"
        for i in range(len(s)-numOnes-1):
            res += "0"
        res += "1"
        return res