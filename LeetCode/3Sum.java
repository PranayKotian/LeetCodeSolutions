//https://leetcode.com/problems/3sum/
//Title: 3Sum
//Difficulty: Medium
//Language: Java
//Author: Pranay Kotian

import java.util.*;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        
        Arrays.sort(nums);
        
        List<List<Integer>> listB = new LinkedList<>();
        
        int n = nums.length; 
        int[] lastA = {10, 10, 10};
        for (int i = 0; i < n; i++){
            for (int j = i + 1; j < n; j++){
                for (int k = j + 1; k < n; k++) {
                    if ((nums[i] + nums[j] + nums[k] == 0) && ((lastA[0]!=nums[i]) || (lastA[1]!=nums[j]))) {
                        listB.add(Arrays.asList(nums[i], nums[j], nums[k]));
                        lastA[0]=nums[i];
                        lastA[1]=nums[j];
                    }
                }
            }
        }
        //Only compared current triplet to previous triplet
        //Need to find solution where duplicate triplets are avoided completely
        
        return listB;
    }
}