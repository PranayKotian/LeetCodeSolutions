class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        #Binary Search Solution
        #Time: O(logn) Space: O(1)
        
        def binSearch(l,r):
            while l <= r:
                m = (l+r)//2
                if nums[m] == target:
                    return True
                elif nums[m] > target:
                    r = m-1
                else:
                    l = m+1
            return False
        
        if len(nums) == 0:
            return False
        if len(nums) == 1:
            return target == nums[0]
        if nums[0] < nums[-1]:
            return binSearch(0,len(nums)-1)
        
        l = 1
        r = len(nums)-1
        while l <= r:
            m = (l+r)//2
            if nums[m] < nums[m-1]:
                if nums[m] <= target <= nums[-1]: return binSearch(m, len(nums)-1)
                else: return binSearch(0, m-1)
            elif nums[m] > nums[0]:
                l = m+1
            elif nums[m] < nums[0]:
                r = m-1
            else:
                return self.search(nums[:m], target) or self.search(nums[m+1:], target)
        return False