class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        #Min Heap Solution - Store distances with coordinates
        #Time: O(klogn) Space: O(n)
        
        minHeap = []
        for x,y in points:
            minHeap.append([(x**2 + y**2)**0.5, [x,y]])
        heapq.heapify(minHeap)
        
        res = []
        for i in range(k):
            res.append(minHeap[0][1])
            heapq.heappop(minHeap)
        return res