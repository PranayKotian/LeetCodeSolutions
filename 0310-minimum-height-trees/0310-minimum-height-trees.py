class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        #Eliminate Leaf Nodes Solution
        #Time: O() Space: O(n+e) 
        
        edgesDict = defaultdict(set)
        for n1,n2 in edges:
            edgesDict[n1].add(n2)
            edgesDict[n2].add(n1)
        
        nodes = set([i for i in range(n)])
        while len(nodes) > 2:
            remove = []
            for n1 in nodes:
                if len(edgesDict[n1]) == 1:
                    remove.append(n1)
            for n1 in remove:
                nodes.remove(n1)
                edgesDict[next(iter((edgesDict[n1])))].remove(n1)
        return list(nodes)
        
        '''        
        edgesDict
        0: 1
        1: 0,2,3
        2: 1
        3: 1
        '''
        
        #Middle of Longest Path Solution
        
        
        
        
        """
        #Brute Force Solution
        #Given all nodes + all edges, dfs on each node to find MHT
        #Time: O(n^2) Space: O(e)
        #TLE - 65 / 71
        
        edgesTable = defaultdict(list)
        for n1,n2 in edges:
            edgesTable[n1].append(n2)
            edgesTable[n2].append(n1)
        
        visited = set()
        def treeHeight(n1):
            height = 0
            visited.add(n1)
            for n2 in edgesTable[n1]:
                if n2 not in visited:
                    height = max(height, 1 + treeHeight(n2))
            visited.remove(n1)
            return height
        
        curMin = sys.maxsize
        validNodes = []
        for i in range(n):
            h = treeHeight(i)
            if h < curMin:
                curMin = h
                validNodes = [i]
            elif h == curMin:
                validNodes.append(i)
        return validNodes
        """