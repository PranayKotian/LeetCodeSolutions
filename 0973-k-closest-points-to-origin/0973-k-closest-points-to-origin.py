class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        minHeap = []
        heapq.heapify(minHeap)
        
        for x,y in points:
            heapq.heappush(minHeap, (-math.sqrt(x**2 + y**2), [x, y]))
        while len(minHeap) > k:
            heapq.heappop(minHeap)
        res = []
        for dist,coords in minHeap:
            res.append(coords)
        return res