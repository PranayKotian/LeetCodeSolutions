class Solution:
    def reverseBits(self, n: int) -> int:
        
        #Solution 1: Remainder Calculation
        #Time: O(32) Space: O(1)
        
        res = 0
        for i in range(31,-1,-1):
            digit = n%2
            res += 2**(i)*digit
            n = n//2
        return res