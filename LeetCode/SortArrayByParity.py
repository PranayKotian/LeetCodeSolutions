//https://leetcode.com/problems/sort-array-by-parity/
//Title: Sort Array By Parity
//Difficulty: Easy
//Language: Python3
//Author: Pranay Kotian

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        B = []
        for i in A:
            if (i % 2) == 0:
                B.insert(0, i)
            else:
                B.append(i)
        return B