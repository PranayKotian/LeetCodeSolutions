class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        #Two Pass Solution
        #Time: O(n) Space: O(1)

        res = nums[0]
        prod = 0
        for i in range(len(nums)):
            if prod == 0: prod = nums[i]
            else: prod *= nums[i]
            res = max(res,prod)
        prod = 0
        for i in range(len(nums)-1,-1,-1):
            if prod == 0: prod = nums[i]
            else: prod *= nums[i]
            res = max(res,prod)
        return res