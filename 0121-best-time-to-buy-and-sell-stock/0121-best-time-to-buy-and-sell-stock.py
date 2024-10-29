class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #One Pass Solution
        #Time: O(n) Space: O(1)
        
        res = 0
        curMin = prices[0]
        for p in prices[1:]:
            res = max(res, p-curMin)
            curMin = min(curMin, p)
        return res