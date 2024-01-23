class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #Recursive DFS
        reqs = {i:[] for i in range(numCourses)}
        for c,p in prerequisites:
            reqs[c].append(p)
        
        visited = set()
        def dfs(crs):
            if crs in visited:
                return False
            if reqs[crs] == []:
                return True
            
            visited.add(crs)
            for pre in reqs[crs]:
                if dfs(pre) == False: return False
            visited.remove(crs)
            reqs[crs] = []
            
            return True
        
        for crs in reqs:
            if dfs(crs) == False: return False
        return True