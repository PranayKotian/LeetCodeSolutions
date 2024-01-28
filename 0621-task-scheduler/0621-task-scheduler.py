class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        #Max Heap Solution
        #Time: O(n)
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        
        q = deque()
        time = 0
        
        while maxHeap or q:
            time += 1
            if maxHeap:
                task = 1 + heapq.heappop(maxHeap)
                if task:
                    q.append([time+n, task])
            if q and q[0][0] == time:
                heapq.heappush(maxHeap, q.popleft()[1])
        
        return time