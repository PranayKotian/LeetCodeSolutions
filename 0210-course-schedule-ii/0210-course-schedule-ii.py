class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
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