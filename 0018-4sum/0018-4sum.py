class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        #Sort + Two Pointer Solution
        #Time: O(n^3) Space: O(n)
        
        nums.sort()
        res = []
        
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)):
                if j != i+1 and nums[j] == nums[j-1]:
                    continue
                
                tar = target - nums[i] - nums[j]
                l = j+1
                r = len(nums)-1
                
                while l < r:
                    if nums[l] + nums[r] == tar:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        while l < len(nums) and nums[l] == nums[l-1]:
                            l += 1
                    elif nums[l] + nums[r] > tar:
                        r -= 1
                    else:
                        l += 1
        return res