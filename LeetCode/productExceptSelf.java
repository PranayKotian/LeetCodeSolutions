//https://leetcode.com/problems/product-of-array-except-self/
//Title: Product of Array Except Self
//Difficulty: Medium
//Language: Java
//Author: Pranay Kotian

class Solution {
    public int[] productExceptSelf(int[] nums) {
        
        //CHEATY SOLUTION WHICH BASICALLY STILL USES DIVISION
        //EXPONENT WORKAROUND DOESN'T WORK FOR 1/0 
        //Create new empty array
//         int[] output = new int[nums.length];
        
//         double prod = nums[0];
//         boolean containsZero = false; 
        
//         for (int i = 1; i < nums.length; i++) {
//             if (nums[i] == 0 && containsZero) { //Output if array contains two zeroes
//                 return output;
//             }
//             if (nums[i] == 0) {
//                 containsZero = true;
//                 continue;
//             }
//             prod *= nums[i];
//         }
        
//         if (containsZero) { //Output if array contains one zero
//             for (int i = 0; i < nums.length; i++) {
//                 if (nums[i] == 0) {
//                     output[i] = (int)prod;
//                 }    
//             }
//         }
//         else { //Output if array contains no zeroes
//             for (int i = 0; i < nums.length; i++) {
//                 output[i] = (int)(prod * Math.pow(nums[i], -1));
//             }
//         }
//         return output;
        
        
        //CORRECT SOLUTION
        //Two arrays:
        // Product of all elms to left of current element 
        // Product of all elems to the right of the current element
        //Multiply corresponding elms of both = product of all elms except current elm
        
        int LENGTH = nums.length;
        
        int[] temp1 = new int[LENGTH];
        temp1[0] = 1;
        int[] temp2 = new int[LENGTH];
        temp2[LENGTH-1] = 1;
        
        int prod1 = 1;
        int prod2 = 1;
        
        for (int i = 1; i < LENGTH; i++) {
            prod1*= nums[i-1];
            temp1[i] = prod1;
        }
        for (int i = LENGTH - 2; i >= 0; i--) {
            prod2*= nums[i+1];
            temp2[i] = prod2;
        }
        
        int[] output = new int[LENGTH];
        
        for (int i = 0; i < LENGTH; i++){
            output[i] = temp1[i] * temp2[i];
        }
            
        return output;
    }
}