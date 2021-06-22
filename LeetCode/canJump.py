#https://leetcode.com/problems/jump-game/
#Title: Jump Game
#Difficulty: Medium
#Language: Python3
#Author: Pranay Kotian

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        n = len(nums)
        #empty array of size nums
        arr = [False for _ in range(n)]
        arr[0] = True
        
        for i in range(1, n):
            for j in range(i-1, -1, -1): 
                #i - j represents the number of steps required to go from i to j
                if (arr[j] == True) and (nums[j] >= (i - j)):
                    arr[i] = True
                    break
        
        print(arr)
        if arr[n-1] == True:
            return True
        return False
    
        """
        Runtime: 3144 ms, faster than 6.76% of Python3 online submissions for Jump Game.
        Memory Usage: 15.5 MB, less than 46.70% of Python3 online submissions for Jump Game.
        
		SWITCHING the order of the conditions in the two if statements significantly improves the runtime: 

        Runtime: 2496 ms, faster than 7.86% of Python3 online submissions for Jump Game.
        Memory Usage: 15.5 MB, less than 44.37% of Python3 online submissions for Jump Game.
        """