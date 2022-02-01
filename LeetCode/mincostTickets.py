#https://leetcode.com/problems/minimum-cost-for-tickets/
#Title: 983. Minimum Cost For Tickets
#Difficulty: Medium
#Language: Python3
#Author: Pranay Kotian

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        mincost = [10*1000] * (len(days) + 1)
        mincost[0] = 0
        #mincost= [0, 1, 2, 3]
        costdur = [1,7,30]
        
        for i in range(1,len(mincost)):
            day = days[i-1]
            
            for c in range(len(costs)):
                oldday = day - costdur[c]
                ni = i 
                while ni > 0 and days[ni-1] > oldday:
                    ni -= 1
                mincost[i] = min(mincost[i], mincost[ni] + costs[c])
        
        return mincost[len(mincost)-1]
        
        
        '''
        mincost to travel today = minimum of 
            cost[2] + mincost(today-30)
            cost[1] + mincost(today-7)
            cost[0] + mincost(today-1)
            
        go backwards until days[index] < today - X or index<0
            find mincost for that day
            or if index<0 mincost = 0
        
        '''