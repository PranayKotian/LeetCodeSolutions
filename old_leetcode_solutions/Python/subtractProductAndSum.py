#https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
#Title: Subtract the Product and Sum of Digits of an Integer
#Difficulty: Easy
#Language: Python3
#Author: Pranay Kotian

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        sum1 = 0
        
        while (n != 0):
            prod = prod * (n % 10)
            sum1 = sum1 + (n % 10)
            n = n // 10
        
        return prod - sum1