class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        
        #Brute Force Solution
        #Time: O(2^n) Space: O(n)
        
        '''
        at each letter, choose to split at the end or skip
        if substring in set, iteration is invalid
        if index == len(s)-1, we split (including the final letter)
        if index == len(s) return length of set
        '''
        
        self.res = 1
        
        bag = set()
        def backtrack(start,end):
            if start == len(s):
                self.res = max(self.res, len(bag))
                return
            
            sub = s[start:end]
            if sub not in bag:
                bag.add(sub)
                backtrack(end, end+1)
                bag.remove(sub)
            if end != len(s): 
                backtrack(start, end+1)
            
        backtrack(0,1)
        return self.res