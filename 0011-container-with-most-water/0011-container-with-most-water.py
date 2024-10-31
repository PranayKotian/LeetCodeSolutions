class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        #Two Pointer Solution
        #Time: O(n) Space: O(1)
        
        res = 0
        l = 0 
        r = len(height)-1
        while l < r:
            res = max(res, (r-l)*min(height[r],height[l]))
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return res
        
        #Brute Force Solution
        #Time: O(n^2) Space: O(1)
        #Check all combinations of containers