class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #Recursive solution with caching
        #Time: Space:
        
        @lru_cache(None)
        def explore(i, curTar):
            if i == len(nums)-1:
                if nums[i] == 0 and curTar == 0:
                    return 2
                if nums[i] == curTar or nums[i] == -curTar:
                    return 1
                else:
                    return 0
            
            p1 = explore(i+1, curTar+nums[i])
            p2 = explore(i+1, curTar-nums[i])

            return p1 + p2
        
        return explore(0, target)
        
        """
        #Recursive brute force solution w/o caching
        #Try every possible combination of +/- on each number in num
        #Check if resulting expression equates to target
        #Time: O(2^n) Space: O(1)
        #(Time Limited Exceeded)
        
        if len(nums) == 1:
            if nums[0] == 0 and target == 0:
                return 2
            if nums[0] == target or nums[0] == -target:
                return 1
            else:
                return 0
        
        p1 = self.findTargetSumWays(nums[1:], target+nums[0])
        p2 = self.findTargetSumWays(nums[1:], target-nums[0])
        
        return p1 + p2
        """