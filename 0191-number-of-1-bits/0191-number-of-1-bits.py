class Solution:
    def hammingWeight(self, n: int) -> int:
        
        #Solution 1: Bit Manipulation
        #Time: O(n) Space: O(1)
        res = 0
        while n:
            res += n%2
            n = n//2
        return res