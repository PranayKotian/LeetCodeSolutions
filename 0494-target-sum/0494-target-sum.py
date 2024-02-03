class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #Recursive solution with caching
        #Time: O(n*t) Space: O(n*t)
        #(where t = all possible expression sums from the nums array)
        
        cache = {}
        def explore(i, curTar):
            if i == len(nums):
                if curTar == 0:
                    return 1
                else:
                    return 0
            if (i,curTar) in cache:
                return cache[(i,curTar)]

            cache[(i,curTar)] = explore(i+1, curTar+nums[i]) + explore(i+1, curTar-nums[i])
            return cache[(i,curTar)]
        
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