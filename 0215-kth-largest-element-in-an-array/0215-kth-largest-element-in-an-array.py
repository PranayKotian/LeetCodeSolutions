class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        #Time: O(n) Space: O(n)
        maxHeap = []
        heapq.heapify(maxHeap)
        for i in nums:
            if len(maxHeap) == k:
                heapq.heappushpop(maxHeap, i)
            else:
                heapq.heappush(maxHeap, i)
        
        return maxHeap[0]