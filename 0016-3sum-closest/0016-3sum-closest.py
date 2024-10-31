class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        #Sorting + 2 Pointer
        #Time: O(nlogn + n^2) Space: O(1)
        
        res = 0
        dist = sys.maxsize
        nums.sort()
        for i in range(len(nums)-2):
            tar = target-nums[i]
            l = i+1
            r = len(nums)-1
            while l < r:
                if abs(target-(nums[i]+nums[l]+nums[r])) < dist:
                    dist = abs(target-(nums[i]+nums[l]+nums[r]))
                    res = nums[i]+nums[l]+nums[r]
                if nums[l]+nums[r] < tar:
                    l += 1
                else:
                    r -= 1 
        return res