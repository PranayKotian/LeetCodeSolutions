//https://leetcode.com/problems/remove-element/
//Title: Remove Element
//Difficulty: Easy
//Language: Java
//Author: Pranay Kotian

class Solution {
    public int removeElement(int[] nums, int val) {
        /*
        int length = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == val) {
                i -= 1;
                for (int j = i + 1; j < nums.length; j++) {
                    nums[j - 1] = nums[j];
                }
            }
            else
                length += 1;
        }
        return length + 1; 

        //Solution exceeds time limit when i is decremented by 1
        */
        
        /*
        int i = 0;
        int len = nums.length; 
        while (i < len) {
            if (nums[i] == val) {
                for (int j = i + 1; j < len; j++)
                    nums[j - 1] = nums[j];
            }
            else
                i += 1; 
        }
        return i + 1;

        //Solution exceeds tie limit
        */
    }
}