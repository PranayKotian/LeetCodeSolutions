#https://leetcode.com/problems/course-schedule/
#Title: 207. Course Schedule
#Difficulty: Medium
#Language: Python
#Author: Pranay Kotian

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        prereq = {i:[] for i in range(numCourses)}
        
        for crs,prq in prerequisites:
            prereq[crs].append(prq)
        
        visited = set()
        
        def dfs(crs):
            if crs in visited:
                return False
            if prereq[crs] == []:
                return True
            
            visited.add(crs)
            for i in prereq[crs]:
                if dfs(i) == False:
                    return False
            visited.remove(crs)
            prereq[crs] = []
            return True
                
        for a in range(numCourses):
            if dfs(a) == False:
                print(a)
                return False
        
        return True