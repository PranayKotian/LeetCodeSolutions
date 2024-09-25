class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        """
        #DP Solution
        #Time: O(n) Space: O(n^2)
        
        tot = sum(nums)
        if tot%2 == 1:
            return False
        
        cache = set([0])
        for n in nums:
            for i in cache.copy():
                cache.add(i+n)
            
            if tot//2 in cache:
                return True
        return False
        """
        
        #Brute Force Solution
        #Time: O(2^n))
        
        tot = sum(nums)
        if tot%2 == 1:
            return False
        
        @lru_cache(None)
        def dfs(cur, i):
            if i == len(nums) or cur > tot//2:
                return False
            if cur == tot//2:
                return True
            
            return dfs(cur+nums[i], i+1) or dfs(cur, i+1)
        
        return dfs(0, 0)
        