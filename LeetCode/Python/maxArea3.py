#https://leetcode.com/problems/container-with-most-water/
#Title: Container With Most Water
#Difficulty: Medium
#Language: Python3
#Author: Pranay Kotian

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        '''
        maxArea = min(height1, height2) * width (i - j)
        '''
        
        l = 0
        r = len(height) - 1
        maxArea = min(height[r], height[l]) * (r - l)
        
        while r > 1:            
            if (height[r] > height[l]):
                l += 1
            else:
                r -= 1
            maxArea = max(maxArea, min(height[r], height[l]) * (r - l))

        return maxArea

        """
        Runtime: 796 ms, faster than 16.91% of Python3 online submissions for Container With Most Water.
        Memory Usage: 27.5 MB, less than 45.54% of Python3 online submissions for Container With Most Water.

        using python functions like min and max make the solution a lot less efficient (compared to maxArea2)
        """