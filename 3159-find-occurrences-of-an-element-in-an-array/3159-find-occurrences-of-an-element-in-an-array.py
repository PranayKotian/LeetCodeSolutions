class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        
        #Track All Occurences Solution w/ Arrays
        #Time: O(n+q) Space: O(n)
        
        occur = [0]
        for i,n in enumerate(nums):
            if n == x:
                occur.append(i)
        res = []
        oLen = len(occur)
        for q in queries:
            if q < oLen: res.append(occur[q])
            else: res.append(-1)
        return res
        
        """
        #Track All Occurences Solution w/ Dict
        #Time: O(n+q) Space: O(n)
        
        table = defaultdict(lambda:-1)
        count = 0
        for i,n in enumerate(nums):
            if n == x:
                count += 1
                table[count] = i
        res = [table[q] for q in queries]
        return res
        """