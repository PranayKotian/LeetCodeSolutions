class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #Greedy solution
        #Time: O(n) Space: O(1)
        
        res = nums[0]
        cur = 0
        for r in range(len(nums)):
            if cur < 0:
                cur = 0
            cur += nums[r]
            res = max(res,cur)
        
        return res