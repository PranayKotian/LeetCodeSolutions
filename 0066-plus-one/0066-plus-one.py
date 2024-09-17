class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        #Simple Solution
        #Time: O(n) Space: O(1)
        
        idx = len(digits) - 1
        while idx >= 0 and digits[idx] == 9:
            digits[idx] = 0
            idx -= 1
        
        if idx == -1:
            digits = [1] + digits
        else:
            digits[idx] += 1
        return digits
        
        
        """
        #Convert To Int Solution
        #Time: O(n) Space: O(n)
        
        total = 0
        n = len(digits)
        for i in range(n-1,-1,-1):
            total += digits[i] * 10**(n-i-1)
        total += 1
        return [int(i) for i in str(total)]
        """