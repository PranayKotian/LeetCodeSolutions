class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #One pass solution (track current minimum)
        #Time: O(n) Space: O(2)
        maxProfit = 0
        curmin = prices[0]
        
        for p in prices[1:]:
            maxProfit = max(maxProfit, p-curmin)
            curmin = min(curmin, p)
        
        return maxProfit