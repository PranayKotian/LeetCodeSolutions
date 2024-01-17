class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        #Minheap solution
        #Time: O(klogn) Space: O(n)
        
        minHeap = []
        #Calculates all euclidean distances
        for x,y in points:
            minHeap.append((math.sqrt(x**2 + y**2), x, y))
        heapq.heapify(minHeap) #O(n) operation
        
        #Pops k coords from heap 
        #O(k logn) operation
        res = []
        for i in range(k):
            dist,x,y = heapq.heappop(minHeap)
            res.append([x,y])
        return res