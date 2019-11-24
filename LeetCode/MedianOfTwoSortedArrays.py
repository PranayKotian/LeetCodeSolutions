#https://leetcode.com/problems/median-of-two-sorted-arrays/
#Title: Median of Two Sorted Arrays
#Difficulty: Hard
#Language: Python3
#Author: Pranay Kotian

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Calculating median value based on length:
        Odd length:
        [num/2]
            3/2 = [1]
            5/2 = [2]
        
        Even length:
        ([num/2] + [num/2 - 1])/2
            (4/2 + 4/2 - 1)/2  == ([2] + [1])/2 
        """
        
        """
        Psuedocode:
            Merge lists
            Sort merged list
            Find median of list
        """
        
        newList = (nums1 + nums2)
        newList.sort()
        len1 = len(newList)
        
        if len(newList)%2 == 0:
            return((newList[len1//2] + newList[len1//2 - 1]) / 2.0)
        else:
            return(newList[len1//2])
        
        #SIDE NOTE: Complete problem without use of sorting algorithms
            