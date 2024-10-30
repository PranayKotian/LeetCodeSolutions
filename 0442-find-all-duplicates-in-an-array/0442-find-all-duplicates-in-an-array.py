class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        #Modify Input Array Solution
        #Time: O(n) Space: O(1)
        
        res = []
        for n in nums:
            if nums[abs(n)-1] < 0:
                res.append(abs(n))
            nums[abs(n)-1] *= -1
        return res