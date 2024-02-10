class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        #Solution 1: Constant Space Pointer Solution
        #Time: O(n+m) Space: O(1)
        
        p2 = len(nums2)-1
        p1 = len(nums1)-len(nums2)-1
        i = len(nums1)-1
        
        while p1 >= 0 and p2 >= 0:
            if nums2[p2] > nums1[p1]:
                nums1[i] = nums2[p2]
                p2 -= 1
                i -= 1
            else:
                nums1[i] = nums1[p1]
                p1 -= 1
                i -= 1
        while p1 >= 0:
            nums1[i] = nums1[p1]
            p1 -= 1
            i -= 1
        while p2 >= 0:
            nums1[i] = nums2[p2]
            p2 -= 1
            i -= 1