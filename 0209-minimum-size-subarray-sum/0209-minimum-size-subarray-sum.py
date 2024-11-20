class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        '''
        Sliding window
        while sum(subarray) < target: shift right pointer
        while sum(subarray) > target: shift left pointer (make size smaller)
        track minimum size in res
        '''
        
        #Sliding Window Solution
        #Time: O(n) Space: O(1)
        
        l = 0
        cur_sum = 0
        min_len = sys.maxsize
        for r in range(len(nums)):
            cur_sum += nums[r]
            
            while cur_sum >= target and l <= r:
                min_len = min(min_len, r-l+1)
                cur_sum -= nums[l]
                l += 1
                
        if min_len == sys.maxsize:
            return 0
        return min_len