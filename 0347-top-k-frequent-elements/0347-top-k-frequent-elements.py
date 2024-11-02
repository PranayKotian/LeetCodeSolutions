class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #Counter + Heap Solution
        #Time: O(n+klogn) Space: O(n)
        
        c = Counter(nums)
        heap = []
        for i in c:
            heap.append([-c[i], i])
        heapq.heapify(heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res