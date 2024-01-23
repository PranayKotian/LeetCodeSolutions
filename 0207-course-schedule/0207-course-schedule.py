class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        #BFS solution 
        prereqs = {i:set() for i in range(numCourses)}
        for course,pre in prerequisites:
            prereqs[course].add(pre)
        
        nottaken = set([i for i in range(numCourses)])
        taken = set()
        updated = True
        
        while updated:
            start = len(taken)
            for c in nottaken.copy():
                if prereqs[c] == set():
                    taken.add(c)
                    nottaken.remove(c)
                    for c1 in prereqs:
                        if c in prereqs[c1]:
                            prereqs[c1].remove(c)
            if start == len(taken):
                updated = False
        
        return len(taken) == numCourses