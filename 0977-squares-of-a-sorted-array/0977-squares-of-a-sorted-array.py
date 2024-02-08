class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        
        
        #Solution 1: .sort() solution
        #Time: O(nlogn) Space: O(n)
        
        nums = [i**2 for i in nums]
        nums.sort()
        return nums