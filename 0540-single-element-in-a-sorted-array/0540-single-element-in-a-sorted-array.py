class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        #Binary Search Solution
        #Time: O(logn) Space: O(1)
        
        l = 0
        r = len(nums)-1
        m = (l+r)//2
        
        while l <= r:
            if m == 0 or m == len(nums)-1 or (nums[m-1] != nums[m] and nums[m+1] != nums[m]):
                return nums[m]
            elif nums[m-1] == nums[m]:
                if m%2 == 0:
                    r = m-2
                else:
                    l = m+1
            else: #nums[m+1] == nums[m]
                if m%2 == 0:
                    l = m+2
                else:
                    r = m-1
            m = (l+r)//2
        
        """
        #Bit Manipulation Solution
        #Time: O(n) Space: O(1)
        
        ans = 0
        for n in nums: 
            ans ^= n
        return ans
        """