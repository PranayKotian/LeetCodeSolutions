#https://leetcode.com/problems/employee-importance/
#Title: 690. Employee Importance
#Difficulty: Medium
#Language: Python
#Author: Pranay Kotian

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        empdict = {e.id: e for e in employees}
        
        #dfs iterative
        
        stack = [id]
        importance = 0
        
        while stack:
            e = stack.pop()
            
            importance += empdict[e].importance
            for sub in empdict[e].subordinates:
                stack.append(sub)
        
        return importance
        
        #dfs recursive
        '''
        def dfs(e):
            sub_imp = sum([dfs(sub) for sub in empdict[e].subordinates])
            return sub_imp + empdict[e].importance
        return dfs(id)
        '''