#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
#Title: 167. Two Sum II - Input Array Is Sorted
#Difficulty: Medium
#Language: Python
#Author: Pranay Kotian

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        #solve question for zero indexed array
        #output +1 for each index
        
        #pseudocode
        l = 0
        r = len(numbers) - 1
       
         while r > l:
            if (numbers[l] + numbers[r] > target):
                r -= 1
            elif (numbers[l] + numbers[r] < target):
                l += 1
            else:
                return [l+1, r+1]