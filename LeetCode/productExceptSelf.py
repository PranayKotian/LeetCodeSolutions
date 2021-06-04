#https://leetcode.com/problems/product-of-array-except-self/
#Title: Product of Array Except Self
#Difficulty: Medium
#Language: Java
#Author: Pranay Kotian

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = [1]
        prod = 1
        
        for i in range(1, len(nums)):
            prod*= nums[i-1]
            #output[i] = prod
            output.append(prod)
        
        #reset prod variable to 1 instead of creating new variable    
        #prod2 = 1
        prod = 1
        
        for i in range(len(nums)-2, -1, -1):
            prod*= nums[i+1]
            #output[i] = previous output value * new prod value
            #i starts at second last value - last value can remain untouched (multiplied by 1)
            output[i]*= prod
        
        return output
            