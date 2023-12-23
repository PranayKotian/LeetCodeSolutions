class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n == 1:
            return nums[0]
        
        v1 = [0] + nums[1:]
        v2 = [0] + nums[:n-1]
        
        for i in range(2,n):
            v1[i] = max(v1[i-1], v1[i-2]+v1[i])
            v2[i] = max(v2[i-1], v2[i-2]+v2[i])
        
        return max(v1[-1], v2[-1])