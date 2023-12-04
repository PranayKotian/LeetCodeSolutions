#https://leetcode.com/problems/two-sum/
#Title: Two Sum
#Difficulty: Easy
#Language: Python3
#Author: Pranay Kotian

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #BRUTE FORCE SOLUTION (very slow 6400ms)
        # length = len(nums)
        # for i in range(length):
        #     j = i + 1
        #     while j < length:
        #         if target == (nums[i] + nums[j]):
        #             return [i, j];
        #         j += 1
        
        #NOT A HASH TABLE SOLUTION (find better code for duplicate num/compliment case)
        # n = len(nums)
        # for i in range(n):
        #     comp = target - nums[i]
        #     if (comp == nums[i]):
        #         if (comp in nums[i+1:n]):
        #             return [i, nums[i+1:n].index(comp) + i + 1]
        #     elif (comp in nums):
        #         return [i, nums.index(comp)]
        
        #HASH TABLE SOLUTION
        #copy values into hash map
        hashmap = {}
        for i, val in enumerate(nums):
            temp = target - val
            if temp in hashmap:
                return [hashmap[temp], i]
            hashmap[val] = i