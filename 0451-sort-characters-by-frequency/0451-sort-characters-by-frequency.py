class Solution:
    def frequencySort(self, s: str) -> str:
        
        #Counter + MinHeap Solution
        #Time: O(n+nlogn) Space: O(n)
        
        c = Counter(s)
        heap = []
        for k in c:
            heap.append([-c[k], k])
        heapq.heapify(heap)
        res = ""
        while heap:
            freq,ch = heapq.heappop(heap)
            res += ch*(freq*-1)
        return res