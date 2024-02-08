class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        #Solution 2: Math
        #Time: O(1) Space: O(1)
        return floor((-1 + sqrt(1+8*n))/2)
        
        """
        #Solution 1: Brute Force
        #Time: O(k) Space: O(1)
        
        res = 0
        stair = 1
        while n >= 0:
            n -= stair
            stair += 1
            res += 1
        return res-1
        """