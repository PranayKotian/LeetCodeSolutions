class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        #Create prereqs adjacency list
        #Track unvisited courses set()
        #Instance where schedule is impossible: there is a loop in the prereqs adjacencny list
        #In this instance, return []
        #Else, build course ordering, once unvisited list in empty, return ordering
        
        prereqs = defaultdict(list)
        for crs,prereq in prerequisites:
            prereqs[crs].append(prereq)
            
        ordering = []
        visited = set()
        
        def dfs(crs: int) -> None:
            if crs in visited:
                return False
            if crs not in prereqs:
                if crs not in ordering: ordering.append(crs)
                return True
            
            visited.add(crs)
            for prereq in prereqs[crs]:
                if dfs(prereq) == False:
                    return False
            ordering.append(crs)
            del prereqs[crs]
            visited.remove(crs)
            return True
        
        for crs in range(numCourses):
            if dfs(crs) == False:
                return []
        return ordering