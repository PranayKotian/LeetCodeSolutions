class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        subsets = []
        
        def findSubsets(i, arr):
            if i == len(nums):
                subsets.append(arr)
                return
            
            findSubsets(i+1, arr+[nums[i]])
            cur = nums[i]
            while i != len(nums) and nums[i] == cur:
                i += 1
            findSubsets(i, arr)
        
        findSubsets(0, [])
        
        return subsets