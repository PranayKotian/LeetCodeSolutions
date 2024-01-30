class Solution:
    def jump(self, nums: List[int]) -> int:
        
        #Greedy solution
        #Time: O(n) Space: O(1)
        jumps = 0
        cur = 0
        r = min(nums[0], len(nums)-1)
        
        while cur != len(nums)-1:
            jumps += 1
            temp = r
            for i in range(cur+1,r+1):
                r = max(r, i+nums[i])
            r = min(r, len(nums)-1)
            cur = temp
        
        return jumps