#https://leetcode.com/problems/3sum/
#Title: 3Sum
#Difficulty: Medium
#Language: Python3
#Author: Pranay Kotian

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
		PSEUDOCODE
		1. Sort array
		2. Create empty arr for answers and initialize length of arr into variable to save time on repeated len calls
		3. Iterate through list of nums using for loop
		4. Set condition to skip repeated targets (if cur elm = last elm)
		5. Set target
		6. Initialize start and end variables
		7. While loop through elms in front of target to find triplets
		8. If triplet is found iterate start to avoid repeat triplets being added to arr
		9. Else, if start + end > target decrement end to get closer to target
		10. Else if start + end < target increment start to get closer to target
		11. Stop while loop once start > end
		12. Return arr with triplets for 3Sum
        '''

        #Sort array
        nums.sort()
        arr = []
        N = len(nums)
        
        for i in range(N):
            #Skips over checking for the same target twice
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            #Looks for two numbers that equals target
            target = nums[i] * -1
            
            #Checks numbers from opposite ends that equal the target
            start = i + 1
            end = N - 1
            while start < end:
                if (nums[start] + nums[end] == target):
                    arr.append([nums[i], nums[start], nums[end]])
                    
                    #avoids duplicate triplets 
                    start = start + 1
                    while start < end and (nums[start] == nums[start-1]):
                        start = start + 1
                    
                elif (nums[start] + nums[end] > target):
                    end = end - 1
                else:
                    start = start + 1
                
        return arr
        

        
        """
        MY OLD SOLUTION:
        arr = []
        
        i = 0
        N = len(nums)
        while (i < N):
            j = 1 + 1
            while (j < N):
                k = j + 1
                while (k < N):
                    if (nums[i] + nums[j] + nums[k] == 0):
                        arr.append([nums[i], nums[j], nums[k]])
            i += 1
        
        return arr

        #EXCEEDS TIME LIMIT
        """
        
        
        """
        #nums = complete list of nums
        
        1 2 3 4
          2 3 4 5 
            3 4 5 6
            
        
        listList = []
        
        nums1 = nums.copy()
        nums1.pop(-1)
        nums1.pop(-2)
        nums2 = nums.copy()
        nums2.pop(0)
        nums2.pop(-1)
        nums3 = nums.copy()
        nums3.pop(0)
        nums3.pop(1)
        
        for i in nums1:
            for j in nums2:
                for k in nums3:
                    if (i + j + k == 0):
                        listList.append([i, j, k])
        return listList
        
        """
        
                        
        