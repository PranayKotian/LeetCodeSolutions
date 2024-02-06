class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        #Solution 3: Dynamic Programming
        #Time: O(n*sum(nums)) Space: O(sum(nums))
        if sum(nums)%2 == 1:
            return False
        
        target = sum(nums)//2
        sums = set([0])
        
        for n in nums:
            for s in sums.copy():
                sums.add(s+n)
            if target in sums:
                return True
        
        return False
        
        #Solution 2: Backtrack w/ Cache
        #Time: O(n*sum(nums)) Space:
        #where sum(nums) is (max) 200*100 = 20000
        
        
        """
        #Solution 1: Brute force DFS
        #Time: O(2^n) Space: O(n)
        #(Time Limited Exceeded w/ 36/141 passed) 
        
        if sum(nums)%2 == 1:
            return False
        
        def dfs(cur, arr):
            if sum(arr) == cur:
                return True
            if cur > sum(arr):
                return False
            
            for i in range(len(arr)):
                elm = arr.pop(0)
                if dfs(cur+elm, arr):
                    return True
                arr.append(elm)
            
            return False
        
        return dfs(0, nums)
        """