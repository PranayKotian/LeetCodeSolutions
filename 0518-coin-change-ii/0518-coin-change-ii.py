class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        #Most efficient DP solution
        #Time: O(c*n) Space: O(n)
        
        arr = [0 for i in range(amount+1)]
        arr[0] = 1
        
        #Potential combinations are found coin by coin
        # to avoid repeated permutations
        for c in coins: 
            for i in range(1,amount+1):
                if i-c >= 0:
                    arr[i] += arr[i-c]
        
        return arr[-1]