class Solution:
    def hammingWeight(self, n: int) -> int:
        
        #Solution 2: Bit Manipulation (Optimized)
        #Time: O(32) Space: O(1)
        res = 0
        while n:
            res += 1
            n &= (n-1)
        return res
        
        """
        #Solution 1: Bit Manipulation
        #Time: O(32) Space: O(1)
        res = 0
        while n:
            res += n%2
            n = n >> 1 #Bit shift to the right by one
            #n = n//2
        return res
        """