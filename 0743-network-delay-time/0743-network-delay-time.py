class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        #BFS Solution
        #Time: O(n^2) Space: O(e)
        
        paths = {i:[] for i in range(1,n+1)}
        for n1,n2,t in times:
            paths[n1].append([n2, t])
        
        minTimes = [sys.maxsize for i in range(n+1)]
        minTimes[0] = 0
        minTimes[k] = 0
        q = deque([(0,k)])
        
        while q:
            for i in range(len(q)):
                curTime,node = q.popleft()
                for n2,t in paths[node]:
                    if minTimes[n2] > curTime+t:
                        minTimes[n2] = curTime+t
                        q.append((curTime+t, n2))
        
        res = max(minTimes)
        if res == sys.maxsize:
            return -1
        return res