class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        #Solution 1: Adjacency List Solution
        #Time: O(n + p) Space: O(1)
        
        prereq = {i:[] for i in range(numCourses)}
        for p in prerequisites:
            prereq[p[0]] += [p[1]]
        
        visited = set()
        
        def dfs(n):
            if prereq[n] == []:
                return True
            if n in visited:
                return False
            
            visited.add(n)
            for p in prereq[n]:
                if not dfs(p):
                    return False
            prereq[n] = []
            visited.remove(n)
            return True
        
        for crs in range(numCourses):
            if dfs(crs) == False: return False
        return True