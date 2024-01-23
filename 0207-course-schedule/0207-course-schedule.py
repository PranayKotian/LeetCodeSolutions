class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        #BFS solution 
        reqs = {}
        for c,p in prerequisites:
            if c not in reqs:
                reqs[c] = set([p])
            else:
                reqs[c].add(p)
        
        taken = set()
        for c in range(numCourses):
            if c not in reqs: #course doesnt have any reqs
                taken.add(c)
        
        update = True
        while update:
            start = len(taken)
            for c in reqs.copy():
                if c not in reqs:
                    continue
                if taken >= reqs[c]:
                    del reqs[c]
                    taken.add(c)
            if start == len(taken):
                update = False
        
        return len(taken) == numCourses