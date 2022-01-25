#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
#Title: Best Time to Buy and Sell Stock
#Difficulty: Medium
#Language: Python
#Author: Pranay Kotian

class Solution:
    def maxProfit2(self, prices: List[int]) -> int:
        
        pastval = prices[0]
        profit = 0
        
        for i, val in enumerate(prices):
            if (val > pastval):
                profit += val - pastval
            pastval = val
        
        return profit