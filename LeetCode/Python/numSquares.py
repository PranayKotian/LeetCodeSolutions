#https://leetcode.com/problems/perfect-squares/
#Title: 279. Perfect Squares
#Difficulty: Medium
#Language: Python3
#Author: Pranay Kotian

class Solution:
    mincost = [0 ,1]
    
    def numSquares(self, n: int) -> int:
        mincost = self.mincost
        lenarr = len(mincost)
        
        for i in range(lenarr,n+1):
            s = 1
            mincost.append(5)
            for s in range(1,int(len(mincost)**0.5) + 1):
                mincost[i] = min(mincost[i], mincost[i - s**2] + 1)
        
        return mincost[n]

    # _dp = [0]
    # def numSquares(self, n):
    #     dp = self._dp
    #     while len(dp) <= n:
    #         dp += min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1,
    #     return dp[n]