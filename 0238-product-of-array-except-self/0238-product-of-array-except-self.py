class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #Two Pass Constant Space Solution
        #Time: O(n) Space: O(1)
        
        res = [1] * len(nums)
        prod = 1
        for i in range(0, len(nums)-1):
            prod *= nums[i]
            res[i+1] *= prod
        prod = 1
        for i in range(len(nums)-1,0,-1):
            prod *= nums[i]
            res[i-1] *= prod
        return res
            