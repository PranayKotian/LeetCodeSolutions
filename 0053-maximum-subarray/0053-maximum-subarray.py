class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #Greedy solution
        #Time: O(n) Space: O(1)
        
        res = nums[0]
        cur = 0
        l = 0
        for r in range(len(nums)):
            cur += nums[r]
            res = max(res,cur)
            while cur < 0 and l <= r:
                cur -= nums[l]
                l += 1
        
        return res