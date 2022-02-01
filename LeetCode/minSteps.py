#https://leetcode.com/problems/2-keys-keyboard/
#Title: 650. 2 Keys Keyboard
#Difficulty: Medium
#Language: Python3
#Author: Pranay Kotian

class Solution:
    def minSteps(self, n: int) -> int:
        steps = [10*1000] * (n+1)
        steps[0] = 0
        steps[1] = 0  
        
        for i in range(2,n+1):
            for d in range(1,i+1):
                if i%d == 0:
                    steps[i] = min(steps[i], steps[d] + i//d)
        return steps[n]
        
        '''
        e.g. 6
        
        can be divide by
        1 2 3 6
        
        possible number of operations =
        1 * 6 (paste A 5 times)     6 operations 
        2 * 3 (paste AA 2 times)    3 operations
        3 * 2 (paste AAA 1 times)   2 operations
        
        operations = 1 copy + X pastes
        total operations = past operations to get to divisor, + current operations to get to current n
        '''