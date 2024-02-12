class Solution:
    def countBits(self, n: int) -> List[int]:
        
        #Solution 3: DP Solution
        #Time: O(n) Space: O(n) 
        
        ans = [0] * (n+1)
        offset = 1
        for i in range(1,n+1):
            if offset*2 == i:
                offset = i
            ans[i] = 1+ans[i-offset]
        return ans
        
        """
        #Solution 2: bin().count() List Comprehension Solution
        #Time: O(nlogn) Space: O(n)
        
        #bin() converts integer to binary representation (str) 
        return [bin(i).count('1') for i in range(n+1)]
        """
        
        """
        #Solution 1: Counting Bits Individually Solution
        #Time: O(nlogn) Space: O(n)
        
        ans = [0 for i in range(n+1)]
        for i in range(n+1):
            temp = i
            while temp:
                ans[i] += temp%2
                temp = temp >> 1
        return ans
        """