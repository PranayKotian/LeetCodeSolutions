class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = [10**5 for i in range(amount+1)]
        res[0] = 0

        for c in coins:
            if c <= amount:
                res[c] = 1

        for i in range(amount+1):
            for c in coins:
                if i-c >= 0:
                    res[i] = min(res[i], 1+res[i-c])

        if res[-1] == 10**5:
            return -1
        return res[-1]