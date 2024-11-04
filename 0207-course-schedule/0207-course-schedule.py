class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        #Adjacency List DFS Solution
        #Time: O(n) Space: O(n)
        
        prereqs = defaultdict(list)
        for crs,pre in prerequisites:
            prereqs[crs].append(pre)
        
        visited = set()
        def dfs(crs):
            if crs in visited:
                return False
            if crs not in prereqs:
                return True
            
            visited.add(crs)
            res = True
            for req in prereqs[crs]:
                res = res and dfs(req)
            del prereqs[crs]
            visited.remove(crs)
            return res
        
        for crs in prereqs.copy():
            if not dfs(crs):
                return False
        return True
            