class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        #DP Solution
        #Time: O(n*sum(nums)) Space: O(sum(nums))
        
        tot = sum(nums)
        if tot%2 == 1:
            return False
        targetSum = tot//2
        
        sums = set([0])
        for n in nums:
            for s in sums.copy():
                sums.add(n+s)
            if targetSum in sums:
                return True
        return False