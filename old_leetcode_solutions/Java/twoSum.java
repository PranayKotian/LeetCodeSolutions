//https://leetcode.com/problems/two-sum/
//Title: Two Sum
//Difficulty: Easy
//Language: Java
//Author: Pranay Kotian

class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        int tempTar;
        int i = 0; 
        int j = 0;
        
        outer: for (i = 0; i < nums.length; i++) {
            tempTar = target - nums[i];
            for (j = i + 1; j < nums.length; j++) {
                if (nums[j] == tempTar)
                    break outer;
            }
        }
        return new int[] {i, j};

        /*
		Runtime: 43 ms, faster than 30.48% of Java online submissions for Two Sum.
		Memory Usage: 39.4 MB, less than 5.65% of Java online submissions for Two Sum.
        */
        
    }
}