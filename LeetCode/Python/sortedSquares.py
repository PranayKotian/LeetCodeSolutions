#https://leetcode.com/problems/squares-of-a-sorted-array/
#Title: 977. Squares of a Sorted Array
#Difficulty: Easy
#Language: Python
#Author: Pranay Kotian

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #braindead solution
        #calculate all squares, array.sort()
        
#         for i in range(len(nums)):
#             nums[i] = nums[i] ** 2
#         return sorted(nums)
        
        #efficient solution?
        #GREATLY improved by simply creating points for the left and rightmost values in list and working inwards
        out = []
        i = 0
        
        while (i<len(nums)-1 and abs(nums[i+1]) <= abs(nums[i])):
            i+=1
        print(i)
        
        p1 = i
        p2 = i-1
        
        while p1>=0 and p2>=0 and p1<len(nums) and p2<len(nums):
            v1 = abs(nums[p1])
            v2 = abs(nums[p2])
            
            if (v1 < v2):
                out.append(v1**2)
                p1+=1
            else:
                out.append(v2**2)
                p2-=1
        while p1>=0 and p1<len(nums):
            out.append(nums[p1]**2)
            p1+=1
        while p2>=0 and p2<len(nums):
            out.append(nums[p2]**2)
            p2-=1
        return out