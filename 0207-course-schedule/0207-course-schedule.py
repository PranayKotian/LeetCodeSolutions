class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        #Adjacency List + DFS Solution
        #Time: O(n+p)  Space: O(n)
        
        #Create adjacency list
        prereqs = {}
        for crs,prereq in prerequisites:
            if crs not in prereqs:
                prereqs[crs] = []
            prereqs[crs].append(prereq)
        
        def dfs(course):
            if course in visited:
                return False
            if course not in prereqs:
                return True
            
            visited.add(course)
            res = True
            for req in prereqs[course].copy():
                res = res and dfs(req)
            visited.remove(course)
            del prereqs[course]
            return res
        
        visited = set()
        for crs in prereqs.copy():
            if dfs(crs) == False:
                return False
        
        return True