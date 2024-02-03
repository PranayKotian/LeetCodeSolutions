class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #One pass solution (track current minimum)
        #Time: O(n) Space: O(2)
        maxProfit = 0
        curmin = prices[0]
        
        for i in range(1,len(prices)):
            maxProfit = max(maxProfit, prices[i]-curmin)
            curmin = min(curmin, prices[i])
        
        return maxProfit