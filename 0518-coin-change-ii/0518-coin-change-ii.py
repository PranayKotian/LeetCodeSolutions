class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        #DP Solution
        #Time: O(n*c) Space: O(n)
        
        amounts_array = [0 for i in range(amount+1)]
        amounts_array[0] = 1
        
        for c in coins:
            for i in range(c, len(amounts_array)):
                amounts_array[i] += amounts_array[i-c]
        return amounts_array[-1]
    
        
        """
        #Brute Force All Combinations
        #Time: O(2^n) Space: O(n)
        #TLE - 14/29
        
        self.res = 0
        def backtrack(i: int, cur: int):
            if cur == amount:
                self.res += 1
                return
            if cur > amount or i == len(coins):
                return
            backtrack(i, cur+coins[i])
            backtrack(i+1, cur)
        backtrack(0, 0)
        return self.res
        """