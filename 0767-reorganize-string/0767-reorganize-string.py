class Solution:
    def reorganizeString(self, s: str) -> str:
        
        #MaxHeap Solution
        #Time: O(nlogn) Space: O(n)
        
        '''
        1 a 
        1 ab
        2 aba
        2 abab
        3 ababa
        3 ababab
        
        len(s)+1//2
        
        '''
        
        count = Counter(s)
        if max(count.values()) > (len(s)+1)//2:
            return ""
        
        maxHeap = []
        for c in count:
            heappush(maxHeap, (-count[c], c))
        
        res = ""
        toAdd = None
        while maxHeap:
            cur = heappop(maxHeap)
            res += cur[1]
            if toAdd:
                heappush(maxHeap, toAdd)
            toAdd = (cur[0]+1, cur[1]) if cur[0] != -1 else None
        return res 
            
            