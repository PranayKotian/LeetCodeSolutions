class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        #Solution 2: Binary Search
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
        
        """
        #Solution 1: Brute Force
        #Time: O(sqrt(n)) Space: O(1)
        
        for i in range(1,num+1):
            if i**2 == num:
                return True
            if i**2 > num:
                return False
        """