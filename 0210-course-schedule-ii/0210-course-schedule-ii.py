class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        #from collections import defaultdict
        
        #Adjacency List Solution
        #Time: O(n) Space: O(n)
        
        #Create adjacencny list
        prereq = {i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            prereq[crs].append(pre)
        
        #Perform DFS that works backwards through prereqs and adds them first
        visited = set()
        res = []
        
        def dfs(crs):
            if crs in visited: #indicates loop in array
                return False
            if crs not in prereq:
                return True
            if prereq[crs] == []:
                res.append(crs)
                del prereq[crs]
                return True
            
            out = True
            visited.add(crs)
            for pre in prereq[crs]:
                out = out and dfs(pre)
            res.append(crs)
            del prereq[crs]
            visited.remove(crs)
            return out
        
        for i in range(numCourses):
            if not dfs(i):
                return []
            
        if len(res) != numCourses:
            return []
        return res