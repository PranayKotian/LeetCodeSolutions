class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        #Two Pointer Solution
        #Time: O(n^2) Space: O(1)
        
        nums.sort()
        res = []
        
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < len(nums) and nums[l] == nums[l-1]:
                        l += 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                    while r >= 0 and nums[r] == nums[r+1]:
                        r -= 1
                else: 
                    l += 1
                    while l < len(nums) and nums[l] == nums[l-1]:
                        l += 1
        return res
        
        
        """
        #Binary Search Solution
        #Time: O(n^2 * logn) Space: O(1)
        #TLE
        
        #Sort list (nlogn)
        nums.sort()
        res = set()
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                target = -nums[i] - nums[j]
                
                #Binary search (logn operation n^2 times)
                l = j+1
                r = len(nums)-1
                while l <= r:
                    m = (l+r)//2
                    if nums[m] == target:
                        res.add((nums[i], nums[j], nums[m]))
                        break
                    elif nums[m] > target:
                        r = m-1
                    else:
                        l = m+1
        return list(res)
        """