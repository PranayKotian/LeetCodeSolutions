class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #maxheap solution
        stones = [-i for i in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            r1 = -heapq.heappop(stones)
            r2 = -heapq.heappop(stones)
            if r1 != r2:
                heapq.heappush(stones, -abs(r1-r2))
        
        if stones:
            return -stones[0]
        return 0
        