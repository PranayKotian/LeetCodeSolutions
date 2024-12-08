class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        #Three Pointer Solution
        #Time: O(n) Space: O(1)
        
        res = 0
        odds = 0
        l = m = 0
        
        for r in range(len(nums)):
            if nums[r]%2 == 1:
                odds += 1
            
            while odds > k:
                if nums[l]%2 == 1:
                    odds -= 1
                l += 1
            m = l
            
            if odds == k:
                while nums[m]%2 == 0:
                    m += 1
                res += m-l+1
        return res
        
        """
        #Two Pointer Solution
        #Time: O(n) Space: O(1)
        
        l = r = 0
        odds = 0
        res = 0
        
        while r < len(nums): 
            lcount = 1
            while r < len(nums) and odds < k:
                if nums[r]%2 == 1:
                    odds += 1
                r += 1

            while l < len(nums) and nums[l]%2 == 0:
                l += 1
                lcount += 1
            
            rcount = 1
            while r < len(nums) and nums[r]%2 == 0:
                rcount += 1
                r += 1

            if odds == k: res += lcount*rcount
            l += 1
            odds -= 1
        
        return res
        """