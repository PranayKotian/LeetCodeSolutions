class Solution:
    def countBits(self, n: int) -> List[int]:
        
        #Pattern Solution
        #Time: O(n) Space: O(1)
        
        arr = [0]
        while len(arr) <= n+1:
            arr += [1+i for i in arr]
        return arr[:n+1]
        
        """
        #Brute Force Solution
        #Time: O(nlogn) Space: O(1)
        
        res = []
        for i in range(n+1):
            ones = 0
            while i!=0:
                ones += i%2
                i = i//2
            res.append(ones)
        return res 
        """