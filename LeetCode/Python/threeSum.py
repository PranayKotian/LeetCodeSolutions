#https://leetcode.com/problems/3sum/
#Title: 3Sum
#Difficulty: Medium
#Language: Python3
#Author: Pranay Kotian

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
                
        nums.sort()
        n = len(nums)
        
        if (n < 3):
            return []
        triplets = []
        
        for i in range(n-2):
            if (i != 0 and nums[i] == nums[i-1]):
                continue
#            target = -nums[i]
            
            l = i + 1
            r = n - 1
            
            #EFFICIENT L R pointer solution (requires sorting nums array)
            while r > l:
                if (nums[i] + nums[l] + nums[r] > 0):
                    r -= 1
                elif (nums[i] + nums[l] + nums[r] < 0):
                    l += 1
                else: #(nums[i] + nums[l] + nums[r] == 0)
                    triplets.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while (nums[l] == nums[l-1] and r > l):
                        l += 1
                        
            #2SUM code and target determine by looping through list
            # worst case scenario is correct target is third last elemenet with next two elements working
#             for j in range(i + 1, n-1):
#                 comp = target - nums[j]
#                 if (j != 1 and comp == oldcomp):
#                     continue
                
#                 if (comp in nums[j+1:n]):
#                     triplets.append([nums[i], nums[j], comp])
#                 oldcomp = comp    
            
        return triplets