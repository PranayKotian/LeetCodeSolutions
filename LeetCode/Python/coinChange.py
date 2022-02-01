#https://leetcode.com/problems/coin-change/
#Title: Coin Change
#Difficulty: Medium
#Language: Python3
#Author: Pranay Kotian

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        arr = [sys.maxsize for _ in range(amount+1)]
        arr[0] = 0
        
        for i in range(1, amount + 1):
            for c in coins:
                back = i - c
                if (back < 0):
                    continue
                if(arr[back] != -1):
                    arr[i] = min(arr[i], 1 + arr[back])
            if arr[i] == sys.maxsize:
                arr[i] = -1
        return arr[amount]