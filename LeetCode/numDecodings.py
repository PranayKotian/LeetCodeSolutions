#https://leetcode.com/problems/decode-ways/
#Title: 91. Decode Ways
#Difficulty: Medium
#Language: Python3
#Author: Pranay Kotian

class Solution:
    def numDecodings(self, s: str) -> int:
        dict = {
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "11",
        "12",
        "13",
        "14",
        "15",
        "16",
        "17",
        "18",
        "19",
        "20",
        "21",
        "22",
        "23",
        "24",
        "25",
        "26"}

        n = len(s)
        arr = [0 for _ in range(n)]

        for i in range(1,27): #loop through the numbers 1 to 26