class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        #Solution 3: DP solution
        #Time: O(n^2) Space: O(n)
        
        LIS = [1 for i in range(len(nums))]
        
        for i in range(len(nums)-2,-1,-1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1+LIS[j])

        return max(LIS)
        
        """
        #Solution 2: Brute force w/ caching
        #Time: O(n^2) Space: O(n*1e8)
        #(Memory Limit Exceeded)
        
        cache = {}
        def dfs(prev, i):
            if i == len(nums):
                return 0
            if (prev, i) not in cache:
                if nums[i] > prev:
                    cache[(prev,i)] = max(1 + dfs(nums[i], i+1), dfs(prev, i+1))
                else:
                    cache[(prev,i)] = dfs(prev, i+1)
            return cache[(prev,i)]
        
        return dfs(-10**5, 0)
        """
        
        """
        #Solution 1: Brute force
        #Time: O(2^n) Space: O(n) (max recursive stack depth)
        
        def dfs(prev, i):
            if i == len(nums):
                return 0
            if nums[i] > prev:
                return max(1 + dfs(nums[i], i+1), dfs(prev, i+1))
            else:
                return dfs(prev, i+1)
                    
        return dfs(-10**5, 0)
        """