class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #Topological sort solution (BFS)
        req = {i:set() for i in range(numCourses)} #prereq: list of next courses
        indegree = numCourses*[0]
        
        for crs,pre in prerequisites:
            req[pre].add(crs)
            indegree[crs] += 1
        
        q = deque()
        for c in range(numCourses):
            if indegree[c] == 0:
                q.append(c)
        
        res = []
        while q:
            cur = q.pop()
            res.append(cur)
            for nextCrs in req[cur]:
                indegree[nextCrs] -= 1
                if indegree[nextCrs] == 0:
                    q.append(nextCrs)
        
        if len(res) == numCourses:
            return res
        return []