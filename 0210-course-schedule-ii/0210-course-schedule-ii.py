class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        #Topological Sort
        #Time: O(n+p) Space: O(n)
        
        #Create adjacency list
        prereqs = {i:[] for i in range(numCourses)}
        for crs,prereq in prerequisites:
            prereqs[crs].append(prereq)
        
        ordering = []
        
        visited = set()
        completed = set()
        
        def dfs(course):
            if course in visited:
                return False
            if course in completed:
                return True
            
            visited.add(course)
            for req in prereqs[course]:
                if dfs(req) == False:
                    return False
            visited.remove(course)
            completed.add(course)
            ordering.append(course)
            prereqs[course] = []
            return True
        
        for crs in prereqs:
            if dfs(crs) == False:
                return []
        
        return ordering
        
        """
        #Adjacency List + Inefficient BFS
        #Time: O(?) Space: O(n)
        
        #Create adjacency list
        adjacent = {}
        for crs,prereq in prerequisites:
            if crs not in adjacent:
                adjacent[crs] = set()
            adjacent[crs].add(prereq)
        
        courses = set([i for i in range(numCourses)])
        ordering = []
        change = True
        
        while courses and change:
            change = False
            
            #Add to ordering
            for i in courses.copy():
                if i not in adjacent:
                    courses.remove(i)
                    ordering.append(i)
                    change = True
            
            #Remove from adjacency list
            for k in adjacent:
                for i in adjacent[k].copy():
                    if i not in courses:
                        adjacent[k].remove(i)
            
            #Remove empty lists
            for k in adjacent.copy():
                if adjacent[k] == set():
                    del adjacent[k]
        
        if change == False:
            return []
        return ordering
        """