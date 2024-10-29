class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        #Binary Search Solution
        #Time: O(logn + n) Space: O(1)
        
        if nums[0] >= 0 or len(nums)==1:
            return [n**2 for n in nums]
        
        l = 1
        r = len(nums)-1
        while l <= r:
            m = (l+r)//2
            if nums[m] >= 0 and nums[m-1] >= 0:
                r = m-1
            elif nums[m] < 0 and nums[m-1] < 0: 
                l = m+1
            else:
                break
        
        nums = [n**2 for n in nums]
        res = []
        l = m-1
        r = m
        while True:
            if l == -1:
                nums = nums[r:]
                return res + nums
            elif r == len(nums):
                nums = nums[:l+1][::-1]
                return res + nums
            elif nums[l] < nums[r]:
                res.append(nums[l])
                l -= 1
            else: 
                res.append(nums[r])
                r += 1