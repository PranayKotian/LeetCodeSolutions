

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        curminval = prices[0]
        curmax = 0
        for i, val in enumerate(prices):
            if (val - curminval) > curmax:
                curmax = val - curminval
            if val < curminval:
                curminval = val
        return curmax
        
        # Runtime: 1912 ms, faster than 8.83% of Python3 online submissions for Best Time to Buy and Sell Stock.
        # Memory Usage: 25.1 MB, less than 82.75% of Python3 online submissions for Best Time to Buy and Sell Stock.
        
        