class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #State machine solution
        #Time: O(n) Space: O(2)
        
        #s1: can buy
        #s2: can sell
        s1 = 0
        s2 = ~sys.maxsize
        
        for p in prices:
            s1, s2 = max(s1, s2+p), max(s2, s1-p)
        
        return s1