//https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
//Title: Best Time to Buy and Sell Stock
//Difficulty: Easy
//Language: Java
//Author: Pranay Kotian

class Solution {
    public int maxProfit(int[] prices) {
        //work backwards, compare all subtractions, return the max
        //TIME LIMIT EXCEEDED
        
//         int max = 0;
        
//         for (int i = prices.length - 1; i >= 0; i--) {
//             for (int j = i - 1; j >= 0; j--) {
//                 if (prices[i] - prices[j] > max) {
//                     max = prices[i] - prices[j];
//                 }
//             }
//         }
        
//         return max;
        
        //work forwards, track highest spikes, return max
        
        int max = 0;
        int curLow = prices[0];
        
        for (int i = 1; i < prices.length; i++) {
            if (prices[i] - curLow > max) {
                max = prices[i] - curLow;
            }
            if (prices[i] < curLow) {
                curLow = prices[i]; 
            }
        }
        
        return max; 
    }
}