class Solution:
    def rob(self, nums: List[int]) -> int:
        
        p1 = 0
        p2 = nums[0]
        for i in range(1, len(nums)):
            p2, p1 = max(p1 + nums[i], p2), p2        
        return p2