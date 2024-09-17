class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        #Convert To Int Solution
        #Time: O(n) Space: O(n)
        
        total = 0
        n = len(digits)
        for i in range(n-1,-1,-1):
            total += digits[i] * 10**(n-i-1)
        total += 1
        return [int(i) for i in str(total)]