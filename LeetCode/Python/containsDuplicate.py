#https://leetcode.com/problems/contains-duplicate/
#Title: 217. Contains Duplicate
#Difficulty: Easy
#Language: Python
#Author: Pranay Kotian

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        group = {}
        
        for i in nums:
            if i not in group:
                group[i] = i
            else:
                return True
        
        return False