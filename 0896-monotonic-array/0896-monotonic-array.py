class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        #One Pass Solution
        #Time: O(n) Space: O(2)
        
        inc = True
        dec = True
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                dec = False
            elif nums[i] < nums[i-1]:
                inc = False
        return inc or dec
        
        """
        #Three Cases Solution
        #Time: O(n) Space: O(1)
        
        if nums[0] > nums[-1]: #decreasing
            for i in range(1,len(nums)):
                if nums[i] > nums[i-1]:
                    return False
        elif nums[0] < nums[-1]: #increasing
            for i in range(1,len(nums)):
                if nums[i] < nums[i-1]:
                    return False
        else: #nums[0] == nums[-1]
            for n in nums:
                if n != nums[0]:
                    return False
        return True
        """