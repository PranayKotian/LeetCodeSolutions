#https://leetcode.com/problems/merge-sorted-array/
#Title: 88. Merge Sorted Array
#Difficulty: Easy
#Language: Python
#Author: Pranay Kotian

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        for i in range(m, m+n):
            nums1[i] = nums2[i-m]
        
        nums1.sort()