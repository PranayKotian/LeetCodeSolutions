//https://leetcode.com/problems/contains-duplicate/
//Title: Contains Duplicate
//Difficulty: Easy
//Language: Java
//Author: Pranay Kotian

class Solution {
    public boolean containsDuplicate(int[] nums) {
        
        //Hashtable<Integer, Integer> ht1 = new Hashtable<>();
//         Hashtable ht1 = new Hashtable();
        
        // for (int i = 0; i < nums.length; i++) {
        //     if (ht1.contains(nums[i])) {
        //         return false;
        //     }
        //     ht1.put(i, nums[i]);
        // }
        
//         //If no duplicates are found
//         return true; 
        
        Set<Integer> set = new HashSet<Integer>();
        
        for (int i = 0; i < nums.length; i++) {
            if (set.contains(nums[i])) {
                return true;
            }
            set.add(nums[i]);
        }
        
        return false; 
    }
}