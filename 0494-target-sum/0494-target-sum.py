class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        #Brute Force w/ Memoization
        #Time: O(n*sum(nums)) Space: O(n*sum(nums))
        
        # cache = {}
        @cache
        def dfs(i,tot):
            if i == len(nums):
                if tot == target:
                    return 1
                return 0
            return dfs(i+1, tot+nums[i]) + dfs(i+1, tot-nums[i])
            
            # if (i+1,tot+nums[i]) not in cache: cache[(i+1,tot+nums[i])] = dfs(i+1, tot+nums[i])
            # if (i+1,tot-nums[i]) not in cache: cache[(i+1,tot-nums[i])] = dfs(i+1, tot-nums[i])
            # return cache[(i+1,tot+nums[i])] + cache[(i+1,tot-nums[i])]
        
        return dfs(0,0)
        
        """
        #Brute Force w/o Memoization
        #Time: O(n^2) Space: O(n)
        #TLE - 97/140
        
        self.res = 0
        def dfs(i,tot):
            if i == len(nums):
                if tot == target:
                    self.res += 1
                return
            dfs(i+1, tot+nums[i])
            dfs(i+1, tot-nums[i])
        
        dfs(0,0)
        return self.res
        """