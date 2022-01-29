#https://leetcode.com/problems/find-the-town-judge/
#Title: 997. Find the Town Judge
#Difficulty: Easy
#Language: Python
#Author: Pranay Kotian

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        ppl = dict.fromkeys([a for a in range(1,n+1)],0)
        
        for a,b in trust:
            if a in ppl:
                ppl.remove(a)
            
        if len(ppl) == 0:
            return -1
         
        for a,b in trust:
            ppl[b] += 1

        for i in ppl:
            if ppl[i] == n-1:
                return i
        return -1