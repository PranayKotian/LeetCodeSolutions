class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 1 <= k <= max(piles) 
        #binary search solution: O(nlog(max(n))) time

        l = 1
        r = max(piles) 
        res = r

        while l <= r: #change
            k = (l+r)//2
            if sum([(i-1)//k+1 for i in piles]) <= h:
                res = k
                r = k-1
            else: 
                l = k+1
        
        return res
        
