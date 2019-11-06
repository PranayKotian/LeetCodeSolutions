//https://leetcode.com/problems/jewels-and-stones/
//Title: Jewels and Stones
//Difficulty: Easy
//Language: Python3
//Author: Pranay Kotian

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        counter = 0
        for i in S:
            for j in J:
                if i == j:
                    counter += 1
        return counter