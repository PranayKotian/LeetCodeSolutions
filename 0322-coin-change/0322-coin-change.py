class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        #Iterative DP Solution
        #Time: O(n) Space: O(n) where n: amount
        
        min_coins = [sys.maxsize for i in range(amount+1)]
        min_coins[0] = 0
        
        for i in range(1, len(min_coins)):
            for c in coins:
                if i-c >= 0:
                    min_coins[i] = min(min_coins[i], min_coins[i-c]+1)
        if min_coins[-1] == sys.maxsize:
            return -1
        return min_coins[-1]
        
        
        '''
        #Recursive Solution
        #Time: O(amount*c) Space: O(amount) 
        
        @cache
        def min_coins(amt):
            if amt == 0:
                return 0
            if amt in coins:
                return 1

            res = sys.maxsize
            for c in coins:
                if amt-c >= 0:
                    res = min(res, min_coins(amt-c)+1)
            return res
        
        if min_coins(amount) == sys.maxsize:
            return -1
        return min_coins(amount)
        '''