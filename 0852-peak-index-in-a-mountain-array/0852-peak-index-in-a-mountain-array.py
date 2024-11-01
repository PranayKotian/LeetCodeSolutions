class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        #Binary Search Solution
        #Time: O(logn) Space: O(1)
        
        # if arr[0] > arr[1]:
        #     return 0
        # if arr[-1] > arr[-2]:
        #     return len(arr)-1
        
        l = 1
        r = len(arr)-2
        while l <= r:
            m = (l+r)//2
            if arr[m-1] > arr[m] > arr[m+1]:
                r = m-1
            elif arr[m-1] < arr[m] < arr[m+1]:
                l = m+1
            else:
                return m
        return -1