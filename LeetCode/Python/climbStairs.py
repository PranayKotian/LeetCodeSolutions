#https://leetcode.com/problems/climbing-stairs/
#Title: Climbing Stairs
#Difficulty: Easy
#Language: Python3
#Author: Pranay Kotian

class Solution:
    def climbStairs(self, n: int) -> int:
        if (n == 1 or n == 2):
             return n
        
        stairs = [1, 1]
        
        for i in range(2, n+1):
            stairs.append(stairs[i-1] + stairs[i-2])
        
        return stairs[n]