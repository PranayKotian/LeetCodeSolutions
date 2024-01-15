class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #Maxheap solution
        #Time: O(nlogn) Space: O(n)
        stones = [-i for i in stones]
        heapq.heapify(stones) #O(nlogn)
        
        while len(stones) > 1:
            r1 = -heapq.heappop(stones) #O(1)
            r2 = -heapq.heappop(stones) #O(1)
            if r1 != r2:
                heapq.heappush(stones, -abs(r1-r2)) #O(logn)
        
        if stones:
            return -stones[0]
        return 0