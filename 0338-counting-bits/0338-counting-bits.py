class Solution:
    def countBits(self, n: int) -> List[int]:
        
        #Solution 2: bin count solution
        #Time: O(32n) Space: O(n)
        
        #bin() converts integer to binary representation (str) 
        return [bin(i).count('1') for i in range(n+1)]
        
        """
        #Solution 1: Counting bits for each number
        #Time: O(32n) Space: O(n)
        
        ans = [0 for i in range(n+1)]
        for i in range(n+1):
            temp = i
            while temp:
                ans[i] += temp%2
                temp = temp >> 1
        return ans
        """