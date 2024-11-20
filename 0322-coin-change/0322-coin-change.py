class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

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