#https://leetcode.com/problems/decompress-run-length-encoded-list/
#Title: Decompress Run-Length Encoded List
#Difficulty: Easy
#Language: Python3
#Author: Pranay Kotian

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        list1 = [] 
        c = 0
        j = 0
        for i in nums:
            if (c%2 == 0):
                j = i
            else:
                for k in range(j):
                    list1.append(i)
            c += 1 

        return list1