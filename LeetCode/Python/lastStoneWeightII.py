#https://leetcode.com/problems/last-stone-weight-ii/
#Title: 1049. Last Stone Weight II
#Difficulty: Medium
#Language: Python3
#Author: Pranay Kotian

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
            
            '''
            divide the array into two groups such that the difference between the groups is minimized
            
            0/1 knapsack problem where we try to maximize the sack with a limit of sum(stones)/2
            '''
            
            S = sum(stones)//2
            arr = [False] * (S + 1)
            arr[0] = True
            maxval = 0
            
            for s in stones:
                clone = arr.copy()
                for i in range(s, S+1):
                    if clone[i - s] == True:
                        arr[i] = True
                        maxval = max(maxval, i)
                if arr[S] == True:
                        break
            
            return sum(stones) - maxval*2