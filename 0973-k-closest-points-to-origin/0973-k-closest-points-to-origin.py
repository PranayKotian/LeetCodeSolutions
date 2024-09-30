class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        #Min Heap Solution - Store distances with coordinates
        #Time: O(nlogn) Space: O(n)
        
        minHeap = []
        heapq.heapify(minHeap)
        
        for x,y in points:
            heapq.heappush(minHeap, [(x**2 + y**2)**0.5, [x,y]])
        
        res = []
        for i in range(k):
            res.append(minHeap[0][1])
            heapq.heappop(minHeap)
        return res