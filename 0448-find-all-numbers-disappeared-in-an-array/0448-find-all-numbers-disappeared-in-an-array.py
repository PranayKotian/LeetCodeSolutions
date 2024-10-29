class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        #Mark Numbers Solution
        #Time: O(n) Space: O(1)
        
        res = []
        for n in nums:
            nums[abs(n)-1] = abs(nums[abs(n)-1])*-1
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i+1)
        return res