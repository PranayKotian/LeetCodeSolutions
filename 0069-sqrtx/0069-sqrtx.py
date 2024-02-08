class Solution:
    def mySqrt(self, x: int) -> int:
        
        #Solution 1: Binary Search
        #Time: O(logn) Space: O(1)
        
        res = 0
        l = 1
        r = x
        while l <= r:
            m = (l+r)//2
            if m**2 > x:
                r = m-1
            elif m**2 < x:
                res = m
                l = m+1
            else:
                return m
        return res