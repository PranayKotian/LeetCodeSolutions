class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxindex = 0
        for i in range(len(nums)):
            if i <= maxindex:
                maxindex = max(maxindex, i+nums[i])
            else:
                return False
        return True