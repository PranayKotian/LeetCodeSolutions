class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        #Counters Solution
        #Time: O(n) Space: O(n)
        
        res = 0
        c = Counter(chars)
        for w in words:
            if Counter(w) <= c:
                res += len(w)
        return res