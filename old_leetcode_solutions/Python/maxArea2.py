#https://leetcode.com/problems/container-with-most-water/
#Title: Container With Most Water
#Difficulty: Medium
#Language: Python3
#Author: Pranay Kotian

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Volume = min height * width
        width = abs(index1 - index2) 
        """
        i = 0
        j = len(height) - 1
        maxVol = 0
        curVol = 0
        while (i < j):
            
            #Calculates current volume
            #Iterates/decrements the value of the min height
            # (in order to always try to increase the max height to maximize volume)
            width = j - i
            if (height[i] < height[j]):
                curVol = height[i] * width
                i += 1
            else:
                curVol = height[j] * width
                j -= 1
            
            #Checks if current volume is max volume
            if (curVol > maxVol):
                maxVol = curVol
        
        return maxVol
        
        """
        Runtime: 116 ms, faster than 98.56% of Python3 online submissions for Container With Most Water.
        Memory Usage: 14.3 MB, less than 86.32% of Python3 online submissions for Container With Most Water.
        """
            
            
                
                