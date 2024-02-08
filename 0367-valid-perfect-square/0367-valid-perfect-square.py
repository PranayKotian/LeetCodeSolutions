class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        #Solution 1: Binary Search
        #Time: O(logn) Space: O(1)
        
        l = 1
        r = num
        while l <= r:
            m = (l+r)//2
            if m**2 > num:
                r = m-1
            elif m**2 < num:
                l = m+1
            else:
                return True
        return False