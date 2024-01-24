class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #Iterative BFS solution
        req = {i:set() for i in range(numCourses)}
        for crs,pre in prerequisites:
            req[crs].add(pre)
        
        res = []
        
        while True:
            start = len(res)
            for c in req.copy():
                if req[c] == set():
                    res.append(c)
                    del req[c]
                    for c1 in req:
                        if c in req[c1]:
                            req[c1].remove(c)
            if start == len(res):
                break
        
        if len(res) == numCourses:
            return res
        return []