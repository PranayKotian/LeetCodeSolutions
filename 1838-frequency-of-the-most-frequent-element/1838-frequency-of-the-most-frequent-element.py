class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        #Solution 1: Sliding Window Solution
        #Time: O(nlogn) Space: O(n)
        
        nums.sort()
        l = r = len(nums)-1
        cur = k
        res = 1
        
        while l >= 0:
            while cur >= 0 and l >= 0:
                res = max(res, r-l+1)
                l -= 1
                cur -= nums[r]-nums[l]
            if l == -1: 
                return res
            while cur < 0:
                prev = nums[r]
                r -= 1
                cur += (r-l+1)*(prev-nums[r])
        
        return -1