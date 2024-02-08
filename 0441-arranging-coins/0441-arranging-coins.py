class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        #Solution 1: Brute Force
        #Time: O(k) Space: O(1)
        
        res = 0
        stair = 1
        while n >= 0:
            n -= stair
            stair += 1
            res += 1
        return res-1