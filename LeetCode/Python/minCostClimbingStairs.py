#https://leetcode.com/problems/min-cost-climbing-stairs/
#Title: 746. Min Cost Climbing Stairs
#Difficulty: Easy
#Language: Python3
#Author: Pranay Kotian

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        length = len(cost)
        
        arr = [0 for i in range(length)]
        arr[0] = cost[0]
        arr[1] = cost[1]
        
        for i in range(2,length):
            arr[i] = min(arr[i-1],arr[i-2]) + cost[i]
        
        return min(arr[length-1], arr[length-2])