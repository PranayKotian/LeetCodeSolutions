class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        #Greedy DFS
        #Time: O(ElogE) Space: O(E)
        
        adj = defaultdict(list)
        for src,des in sorted(tickets, reverse=True):
            adj[src].append(des)
            
        res = []
        def dfs(src):
            while adj[src]:
                dfs(adj[src].pop())
            res.append(src)
        dfs("JFK")
        return res[::-1]
        
        """
        #Adjacency List + DFS w/ Backtracking Solution
        #Time: O(V+E)^2 Space: O(E)
        
        tickets.sort()
        adj = {src:[] for src,des in tickets}
        for src,des in tickets:
            adj[src].append(des)
        
        res = ["JFK"]
        
        def dfs(src):
            if len(res) == len(tickets)+1:
                return True
            if src not in adj:
                return False
            
            for i,des in enumerate(adj[src].copy()):
                res.append(des)
                adj[src].pop(i)
                if dfs(des): return True
                res.pop()
                adj[src].insert(i,des)
            return False
        
        dfs("JFK")
        return res
        """