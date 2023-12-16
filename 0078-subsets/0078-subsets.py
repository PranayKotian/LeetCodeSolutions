class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:        
        res = []
        
        def backtrack(i, arr):
            if i == len(nums):
                res.append(arr)
            else:
                backtrack(i+1, arr+[nums[i]])
                backtrack(i+1, arr)
        backtrack(0, [])
        
        return res