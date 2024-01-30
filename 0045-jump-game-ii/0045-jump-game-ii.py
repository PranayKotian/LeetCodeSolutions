class Solution:
    def jump(self, nums: List[int]) -> int:
        #Greedy solution
        #Time: O(n) Space: O(1)
        jumps = 0
        l = r = 0
        
        while r < len(nums)-1:
            jumps += 1
            newr = 0
            for i in range(l,r+1):
                newr = max(newr, i+nums[i])
            l = r+1
            r = newr
        
        return jumps