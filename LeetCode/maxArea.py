#https://leetcode.com/problems/container-with-most-water/
#Title: Container With Most Water
#Difficulty: Medium
#Language: Python3
#Author: Pranay Kotian

#Inefficient O(n^2) solution (too time consuming for LeetCode)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Volume = max height * width
        width = abs(index1 - index2) 
        """
        
        maxVol = 0
        
        for i in range (0, len(height)):
            for j in range (i + 1, len(height)):
                if (height[i] > height[j]):
                    minH = height[j]
                else:
                    minH = height[i] 
                if (minH * abs(i - j) > maxVol):
                    maxVol = minH * abs(i - j)
                    
        return maxVol
        