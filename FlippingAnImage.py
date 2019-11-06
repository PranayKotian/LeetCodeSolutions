//https://leetcode.com/problems/flipping-an-image/
//Title: Flipping an Image
//Difficulty: Easy
//Language: Python3
//Author: Pranay Kotian

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        rows = len(A)
        cols = len(A[0])
        B = [[0 for x in range(cols)] for y in range(rows)] 
        for i in range(rows):
            for j in range(cols):
                B[i][-j -1] = A[i][j]
        for i in range(rows):
            for j in range(cols):
                if B[i][j] == 1:
                    B[i][j] = 0
                else:
                    B[i][j] = 1
        return B
            