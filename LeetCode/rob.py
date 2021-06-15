#https://leetcode.com/problems/house-robber/
#Title: House Robber
#Difficulty: Medium
#Language: Python3
#Author: Pranay Kotian

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return nums[0]
        
        arr = [0 for i in range(n)]
        arr[0] = nums[0]
        arr[1] = max(nums[0], nums[1])
        
        for i in range(2, n):
            arr[i] = max(arr[i-1], arr[i-2] + nums[i])
        
        return arr[n-1]
    
        """
        Runtime: 32 ms, faster than 65.46% of Python3 online submissions for House Robber.
        Memory Usage: 14.5 MB, less than 17.94% of Python3 online submissions for House Robber.
        """

        # n = len(nums)
        # if n < 2:
        #     return nums[0]
        
        # arr = [0 for _ in range(3)]
        # arr[0] = nums[0]
        # if nums[0] > nums[1]:
        #     arr[1] = nums[0]
        # else:
        #     arr[1] = nums[1]
        
        # if n == 2:
        #     return arr[1]
        
        # for i in range(2, n):
        #     if (arr[1] > arr[0] + nums[i]):
        #         arr[2] = arr[1]
        #     else:
        #         arr[2] = arr[0] + nums[i]
            
        #     arr[0], arr[1] = arr[1], arr[2]
            
        # return arr[2]

        """
        (Above solution uses an array of size 3 instead of an arry of size len(nums))
        """