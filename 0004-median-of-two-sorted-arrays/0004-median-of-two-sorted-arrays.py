class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #Solution 1: cheat using python libraries
        import numpy
        return numpy.median(nums1 + nums2)