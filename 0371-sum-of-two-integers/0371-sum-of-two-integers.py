class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        #Solution 0: Python Hack
        #Time: O(1) Space: O(1)
        return sum([a, b])
        
        """
        #Solution 1: Bit Manipulation
        #Time: O(1) Space: O(1)
        #INVALID SOLUTION IN PYTHON due to lack of 32-bit integer
        
        res = a ^ b
        leftover = (a & b) << 1
        while leftover:
            res, leftover = res^leftover, (res&leftover) << 1
        return res
        """