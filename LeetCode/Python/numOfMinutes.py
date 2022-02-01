#https://leetcode.com/problems/time-needed-to-inform-all-employees/
#Title: 1376. Time Needed to Inform All Employees
#Difficulty: Medium
#Language: Python
#Author: Pranay Kotian

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        #build graph
        #dfs to traverse graph
        #return maxtime
        
        #{man: emp1, emp2, emp3, etc...}
        adjlist = defaultdict(list)
        
        for emp,man in enumerate(manager):
            adjlist[man].append(emp)
        
        times = [0] * n
        stack = [headID]
        maxtime = 0
        
        while stack:
            boss = stack.pop()
            for emp in adjlist[boss]:
                times[emp] = times[boss] + informTime[boss]
                maxtime = max(maxtime, times[emp])
                stack.append(emp)
        return maxtime