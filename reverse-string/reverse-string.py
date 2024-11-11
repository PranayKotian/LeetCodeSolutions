class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        #Two Pointer Solution
        #Time: O(n) Space: N/A
        
        l = 0
        r = len(s)-1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1 
        
        '''
        #Python Solution
        s.reverse()
        '''