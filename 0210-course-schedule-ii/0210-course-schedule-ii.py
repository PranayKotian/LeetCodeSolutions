class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        #Adjacency List Solution
        #Time: O(n) Space: O(n)
        
        prereqs = {i:[] for i in range(numCourses)}
        for crs,prereq in prerequisites:
            prereqs[crs].append(prereq)
            
        ordering = []
        visited = set()
        
        def dfs(crs: int) -> None:
            if crs in visited:
                return False
            if crs not in prereqs:
                return True
            if prereqs[crs] == []:
                ordering.append(crs)
                del prereqs[crs]
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