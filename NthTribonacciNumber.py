//https://leetcode.com/problems/n-th-tribonacci-number/submissions/
//Title: N-th Tribonacci Number
//Difficulty: Easy
//Language: Python3
//Author: Pranay Kotian

class Solution:
    def tribonacci(self, n: int) -> int:
        tn0 = 0
        tn1 = 1
        tn2 = 1
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        for i in range(n-2):
            tn = tn0 + tn1 + tn2
            tn0 = tn1
            tn1 = tn2
            tn2 = tn
        return tn
            