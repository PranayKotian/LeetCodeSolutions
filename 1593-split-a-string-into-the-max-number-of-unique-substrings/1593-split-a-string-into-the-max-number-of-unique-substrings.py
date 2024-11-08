class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        
        #Backtracking Solution
        #Time: Space:
        
        def backtrack(bag, left):
            if left == "":
                return len(bag)
            res = len(bag)
            for i in range(1,len(left)+1):
                if left[:i] not in bag:
                    bag.add(left[:i])
                    res = max(res, backtrack(bag, left[i:]))
                    bag.remove(left[:i])
            return res
            
        return backtrack(set(), s)