//https://leetcode.com/problems/container-with-most-water
//Title: Container With Most Water
//Difficulty: Medium
//Language: Java
//Author: Pranay Kotian

class Solution {
    public int maxArea(int[] height) {
        
        int i = 0;
        int j = height.length - 1;
        
        int maxVol = 0;
        int curVol = 0;
        
        while (i < j) {
            
            //Make sure to increment/decrement i/j AFTER calculation
            if (height[i] < height[j])
                curVol = (j - i) * height[i++];
            else
                curVol = (j - i) * height[j--];
            
            if (curVol > maxVol)
                maxVol = curVol;
        }
        
        return maxVol;    
    }
}