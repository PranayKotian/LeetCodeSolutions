class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        #MinHeap Solution
        #Time: O(n + klogn) Space: O(n)
        
        heap = [i for arr in matrix for i in arr]
        heapq.heapify(heap)
        for i in range(k-1):
            heapq.heappop(heap)
        return heapq.heappop(heap)