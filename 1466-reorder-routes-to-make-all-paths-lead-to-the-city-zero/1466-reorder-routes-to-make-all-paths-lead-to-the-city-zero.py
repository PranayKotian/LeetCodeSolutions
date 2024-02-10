class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        #Solution 1: BFS Solution (likely inefficient)
        #Time: O(n) Space: O(n)
        
        #BFS from node 0 determines node priority
        #Count connections that don't follow node priority
        
        #Dict will all node neighbours
        nei = {i:[] for i in range(n)}
        for i,j in connections:
            nei[i].append(j)
            nei[j].append(i)
                
        #Create node priorities using BFS
        prio = {}
        q = deque([0])
        curprio = 0 #lower num = higher priority
        while q:
            for i in range(len(q)):
                node = q.popleft()
                prio[node] = curprio
                for n in nei[node]:
                    if n not in prio: q.append(n)
            curprio += 1
        
        #Count wrong connections
        res = 0
        for c1,c2 in connections:
            if prio[c1] < prio[c2]:
                res += 1
        return res