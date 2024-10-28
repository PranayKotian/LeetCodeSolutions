class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        #Counter + Math Solution
        #Time: O(n) Space: O(n)
        
        c = Counter(tasks).values()
        a = max(c)
        b = list(c).count(a)
        return max(len(tasks), (n+1)*(a-1) + b)
        
        """
        #Max Heap Solution
        #Time O(n + m) where m = idle time, Space: O(n)
        
        minHeap = [[0,-v] for v in Counter(tasks).values()]
        heapq.heapify(minHeap)
        t = 0
        while minHeap:
            if minHeap[0][0] <= t:
                cur = heapq.heappop(minHeap)
                if cur[1] != -1:
                    cur = [cur[0]+n+1,cur[1]+1]
                    heapq.heappush(minHeap, cur)
            t += 1
        return t
        """