class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        #Prim's Algorithm Solution (Greedy DFS)
        #Time: O(v^2) Space: O(v^2)
        
        #Create adjacency matrix
        dist = {}
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                xi, yi = points[i]
                xj, yj = points[j]
                d = abs(xi-xj) + abs(yi-yj)
                
                dist[(i,j)] = d
                dist[(j,i)] = d
            
        #Inefficient Prim's algorithm
        minHeap = [[0,0]]
        unvisited = set([i for i in range(len(points))])
        res = 0
        
        while True: #len(unvisited) != 0
            d,p = heappop(minHeap)
            res += d
            
            unvisited.remove(p)
            if len(unvisited) == 0:
                return res
            
            for point in unvisited:
                heappush(minHeap, [dist[(p,point)], point])
            while minHeap and minHeap[0][1] not in unvisited:
                heappop(minHeap)