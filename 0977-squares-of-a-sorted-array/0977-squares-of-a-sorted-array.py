class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        #Solution 2: Binary Search Solution
        #Time: O(n) Space: O(n)
        
        res = []
        l = 0
        r = len(nums)-1
        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                res.append(nums[l]**2)
                l+=1
            else:
                res.append(nums[r]**2)
                r-=1
        
        return res[::-1]
        
        """
        #Solution 1: .sort() solution
        #Time: O(nlogn) Space: O(n)
        
        nums = [i**2 for i in nums]
        nums.sort()
        return nums
        """