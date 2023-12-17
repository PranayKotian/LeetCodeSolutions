class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        subsets = []
        
        def findSubsets(i, arr):
            if i == len(nums):
                if arr not in subsets:
                    subsets.append(arr)
                return
            findSubsets(i+1, arr+[nums[i]])
            findSubsets(i+1, arr)
        
        findSubsets(0, [])
        
        return subsets