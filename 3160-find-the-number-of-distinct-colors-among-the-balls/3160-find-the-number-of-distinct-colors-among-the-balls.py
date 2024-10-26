class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        
        #Colors Dictionary Solution
        #Time: O(n) Space: O(n)
        
        colors = defaultdict(set)
        res = []
        track = {}
        
        for idx,color in queries:
            if idx in track:
                colors[track[idx]].remove(idx)
                if colors[track[idx]] == set():
                    del colors[track[idx]]
            track[idx] = color
            colors[color].add(idx)
            res.append(len(colors))
        return res
        
        """
        #Brute Force Solution
        #Time: O(n*q) Space: O(n)
        #MLE - 547 / 551
        
        res = []
        balls = [0 for i in range(limit+2)]
        for i,c in queries:
            balls[i] = c
            print(balls)
            res.append(len(Counter(balls))-1)
        return res
        """