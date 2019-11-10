//https://leetcode.com/problems/squares-of-a-sorted-array/
//Title: Squares of a Sorted Array
//Difficulty: Easy
//Language: Python3
//Author: Pranay Kotian

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        for i in range(len(A)):
            A[i] = (A[i] * A[i])
        return sorted(A)a