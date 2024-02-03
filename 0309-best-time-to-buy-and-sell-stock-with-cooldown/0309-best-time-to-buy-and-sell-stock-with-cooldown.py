class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #State machine solution (linear DP) 
        #Time: O(n) Space: O(3)
        s1 = 0
        s2 = s3 = ~sys.maxsize
        
        for i in range(len(prices)):
            s1, s2, s3 = max(s1, s3), max(s2, s1-prices[i]), s2+prices[i]
        
        return max(s3,s1)