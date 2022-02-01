#https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/
#Title: 947. Most Stones Removed with Same Row or Column
#Difficulty: Medium
#Language: Python
#Author: Pranay Kotian

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
        c = defaultdict(list)
        
        for i, j in stones:
            c[i].append([i,j])
            c[~j].append([i,j])
        
        visited = set()
        groups = 0
        
        for i, j in stones:
            if (i, j) not in visited:
                visited.add((i,j))
                groups += 1
                stack = [(i,j)]
                
                while stack:
                    curi, curj = stack.pop()
                    
                    for newi, newj in c[curi]:
                        if (newi, newj) not in visited: 
                            visited.add((newi,newj))
                            stack.append((newi,newj))
                            
                    for newi, newj in c[~curj]:
                        if (newi, newj) not in visited: 
                            visited.add((newi,newj))
                            stack.append((newi,newj))
        
        return len(stones) - groups
