class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        #Max Heap Solution
        #Time: O(n) Space: O(n)
        
        maxHeap = [-i for i in stones]
        heapq.heapify(maxHeap)
        
        while len(maxHeap) > 1:
            s1 = heapq.heappop(maxHeap)
            s2 = heapq.heappop(maxHeap)
            
            if s1 == s2:
                continue
            heapq.heappush(maxHeap, -1*abs(s1-s2))
        
        if maxHeap:
            return -1*maxHeap[0]
        return 0
        