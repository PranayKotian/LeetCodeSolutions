#https://leetcode.com/problems/fizz-buzz/
#Title: FizzBuzz
#Difficulty: Easy
#Language: Python3
#Author: Pranay Kotian

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        '''
        FIRST SOLUTION: Using if statements
        arr = []
        for i in range(1, n + 1):
            if (i%3 == 0) and (i%5 == 0):
                arr.append("FizzBuzz")
            elif(i%3 == 0):
                arr.append("Fizz")
            elif(i%5 == 0):
                arr.append("Buzz")
            else:
                arr.append(str(i))
        return arr
        '''

        #SECOND SOLUTION: Using for loops
        arr = [0] * n
        for i in range(n):
            arr[i] = str(i+1)
        for i in range(2, n, 3):
            arr[i] = "Fizz"
        for i in range(4, n, 5):
            arr[i] = "Buzz"
        for i in range(14, n, 15):
            arr[i] = "FizzBuzz"
        return arr


		'''
		FIRST SOLUTION
		Runtime: 44 ms, faster than 47.90% of Python3 online submissions for Fizz Buzz.
		Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Fizz Buzz.

		SECOND SOLUTION
		Runtime: 36 ms, faster than 94.07% of Python3 online submissions for Fizz Buzz.
		Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Fizz Buzz.
		'''