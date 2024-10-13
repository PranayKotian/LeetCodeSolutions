class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        
        #Greedy Solution
        #Time: O(n) Space: O(n)
        
        numOnes = -1
        for c in s:
            if c == "1":
                numOnes += 1
                
        res = "1" * (numOnes) + "0" * (len(s)-numOnes-1) + "1"
        return res