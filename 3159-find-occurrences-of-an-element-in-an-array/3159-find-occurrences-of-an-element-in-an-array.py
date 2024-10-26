class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        
        
        """
        qtable = defaultdict(list)
        for i,v in enumerate(queries):
            qtable[v].append(i)
        
        queries = sorted(list(set(queries)))
        occurences = 0
        q = 0
        qth = queries[q]
        
        for n in nums:
            if n == x:
                occurences += 1
            if occurences == qth:
        """
                
                
        table = defaultdict(lambda:-1)
        count = 0
        for i,n in enumerate(nums):
            if n == x:
                count += 1
                table[count] = i
        res = [table[q] for q in queries]
        return res
        