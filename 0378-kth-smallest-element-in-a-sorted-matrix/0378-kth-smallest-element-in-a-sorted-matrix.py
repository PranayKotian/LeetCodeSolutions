class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        #Heap Solution
        #Time: O(klogn) Space: O(n)
        
        minHeap = []
        for i in range(len(matrix)):
            heappush(minHeap, (matrix[i][0], i, 0))
        for i in range(k-1):
            val,r,c = heappop(minHeap)
            if c != len(matrix)-1:
                heappush(minHeap, (matrix[r][c+1], r, c+1))
        return minHeap[0][0]
        
        """
        #MaxHeap Solution
        #Time: O(n^2 * logk) Space: O(k)
        
        n = len(matrix)
        maxHeap = []
        for r in range(n):
            for c in range(n):
                heappush(maxHeap, -matrix[r][c])
                if len(maxHeap) > k:
                    heappop(maxHeap)
        return -heappop(maxHeap)
    
        
        #MinHeap Solution
        #Time: O(n^2 + klogn) Space: O(n^2)
        
        heap = [i for arr in matrix for i in arr]
        heapify(heap)
        for i in range(k-1):
            heappop(heap)
        return heappop(heap)
        """