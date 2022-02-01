//https://leetcode.com/problems/two-sum/
//Title: Two Sum
//Difficulty: Easy
//Language: Java
//Author: Pranay Kotian

class Solution {
    public int[] twoSum(int[] nums, int target) {
        /*
        How I've solved in the past:
        - Sort array
        - Try combinations of numbers
        - If target > 0, and all nums > 0, eliminate any nums > target
            - Possibly use low high counters and work inwards?
            
        - Previous solution just tried all combinations of numbers (BRUTE FORCE) (O(N^2))
        - Python solution sorted array and did same thing
        */
        
        //Hash Tables in Java
        Map<Integer, Integer> map = new HashMap<>();
        
        //Adds all elements from array to hash table
        for (int i = 0; i < nums.length; i++) {
            map.put(nums[i], i);
        }
        
        //Checks if each numbers compliment exists in hash table
        for (int i=0; i < nums.length; i++) {
            int compliment = target - nums[i];
            if (map.containsKey(compliment) && map.get(compliment) != i) {
                return new int[] {i, map.get(compliment)};
            }
        }
        
        throw new IllegalArgumentException("No two sum solution"); 
    }
}