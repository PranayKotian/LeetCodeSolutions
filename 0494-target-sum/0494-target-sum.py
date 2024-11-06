class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        #Brute Force w/o Memoization
        #Time: O(2^n) Space: O(n)
        #TLE - 97/140
        
        cache = {}
        def dfs(i,tot):
            if i == len(nums):
                if tot == target:
                    return 1
                return 0
            
            if (i+1,tot+nums[i]) not in cache: cache[(i+1,tot+nums[i])] = dfs(i+1, tot+nums[i])
            if (i+1,tot-nums[i]) not in cache: cache[(i+1,tot-nums[i])] = dfs(i+1, tot-nums[i])
            return cache[(i+1,tot+nums[i])] + cache[(i+1,tot-nums[i])]
        
        return dfs(0,0)