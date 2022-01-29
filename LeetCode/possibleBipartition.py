#https://leetcode.com/problems/possible-bipartition/
#Title: 886. Possible Bipartition
#Difficulty: Medium
#Language: Python
#Author: Pranay Kotian

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        #build graph
        #check if all connected components are bipartite
        #if not, return False
        #else return True
        
        adjlist = defaultdict(set)
        
        for a,b in dislikes:
            adjlist[a].add(b)
            adjlist[b].add(a)
        
        color = {i: -1 for i in range(1,n+1)}
        
        for i in adjlist:
            queue = []
            if color[i] == -1:
                queue.append(i)
                c = True
                
                while queue:
                    for j in range(len(queue)):
                        x = queue.pop(0)
                        if color[x] == (not c):
                            return False
                        if color[x] == c:
                            continue
                        for k in adjlist[x]:
                            queue.append(k)
                        color[x] = c
                    c = not c
        
        return True
        