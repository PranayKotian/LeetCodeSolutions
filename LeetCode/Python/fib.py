#https://leetcode.com/problems/fibonacci-number/
#Title: Fibonacci
#Difficulty: Easy
#Language: Python3
#Author: Pranay Kotian

class Solution:
    def fib(self, n: int) -> int:
        if (n <= 1): return n
        return self.fib(n - 1) + self.fib(n - 2)