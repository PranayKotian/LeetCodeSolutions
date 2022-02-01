#https://leetcode.com/problems/maximum-subarray/submissions/
#Title: Maximum Subarray
#Difficulty: Easy
#Language: Python3
#Author: Pranay Kotian

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #brute force solution: test all subarrays and return the highest possible output O(n^2)
        
        #all subarrays will start and end with a positive value
        #unless all values are negative
        # --> then it will just be a subarray of the largest value
        
        #Too many edge cases for this to be an efficient solution
#         sum1 = 0
#         min1 = nums[0]
#         minpos = 0
#         max1 = nums[0]
#         maxpos = 0
        
#         if(len(nums) == 1):
#             return nums[0]
        
#         for i in range(len(nums)):
#             sum1+= nums[i]
#             if (min1 > sum1):
#                 min1 = sum1
#                 minpos = i
#             if (max1 < sum1):
#                 max1 = sum1
#                 maxpos = i
        
#         if(minpos == 0 and nums[minpos] > 0):
#             return sum(nums[minpos:maxpos+1])
        
#         return sum(nums[minpos+1:maxpos+1])
        
        #--------------------------------------------------------
        #KADANES ALGORITHM O(n) SOLUTION
        
#         prev = [nums[0]]
#         maxSub = nums[0]
        
#         for i in range(1, len(nums)):
#             if (nums[i] + sum(prev) > nums[i]):
#                 prev.append(nums[i])
#             else:
#                 prev = [nums[i]]
                
#             if (sum(prev) > maxSub):
#                 maxSub = sum(prev)
                
#         return maxSub
        
        #--------------------------------------------------------
        #MORE EFFICIENT KADANES SOLUTION
        
        prev = nums[0]
        maxSub = nums[0]
        
        for i in range(1, len(nums)):
            if (nums[i] + prev > nums[i]):
                prev += nums[i]
            else:
                prev = nums[i]
                
            if (prev > maxSub):
                maxSub = prev
                
        return maxSub
    
    