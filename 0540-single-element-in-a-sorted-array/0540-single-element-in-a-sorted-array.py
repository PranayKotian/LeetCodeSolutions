class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        #Bit Manipulation Solution
        #Time: O(n) Space: O(1)
        
        ans = 0
        for n in nums: 
            ans ^= n
        return ans