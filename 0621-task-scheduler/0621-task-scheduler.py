class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = Counter(tasks)
        maxHeap = []
        for t in count:
            maxHeap.append(-count[t])
        heapq.heapify(maxHeap)
        
        q = deque()
        time = 0
        
        while maxHeap or q:
            time += 1
            if maxHeap:
                task = heapq.heappop(maxHeap)
                if task != -1:
                    q.append((time+n, task+1))
            if q and q[0][0] == time:
                newtask = q.popleft()[1]
                heapq.heappush(maxHeap, newtask)
        
        return time