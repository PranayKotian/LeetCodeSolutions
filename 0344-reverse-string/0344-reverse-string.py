class Solution:
    def reverseString(self, s: List[str]) -> None:
        
        #Solution 1: Two Pointer
        #Time: O(n) Space: O(1) 
        l = 0
        r = len(s)-1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1