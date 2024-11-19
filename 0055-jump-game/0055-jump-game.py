class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        '''
        track max index you can reach
        iterate through array and update can_reach value as you go
        if cur index > can_reach: return False
        '''
        
        #DP Solution
        #Time: O(n) Space: O(1)
        
        can_reach = 0
        for i in range(len(nums)):
            if i <= can_reach:
                can_reach = max(can_reach, i+nums[i])
            else:
                return False
        return True