class Solution:
    def jump(self, nums: List[int]) -> int:
        minJumps = [10**5 for i in range(len(nums))]
        minJumps[0] = 0
        
        for n in range(len(nums)):    
            for i in range(n+1,min(n+1+nums[n],len(nums))):
                minJumps[i] = min(minJumps[i], minJumps[n]+1)
        
        return minJumps[-1]
        