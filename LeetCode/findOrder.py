#https://leetcode.com/problems/course-schedule-ii/
#210. Course Schedule II
#Difficulty: Medium
#Language: Python
#Author: Pranay Kotian

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        def dfs(c):
            if c in cycle:
                return False
            if c in visit:
                return True
            
            cycle.add(c)
            for pre in prereq[c]:
                if not dfs(pre):
                    return False
            cycle.remove(c)
            visit.add(c)
            res.append(c)
            return True
        
        prereq = {i: [] for i in range(numCourses)}
        for crs,pre in prerequisites:
            prereq[crs].append(pre)
            
        cycle = set()
        visit = set()
        res = []
        
        for i in range(numCourses):
            if i not in visit:
                if not dfs(i):
                    return []

        return res