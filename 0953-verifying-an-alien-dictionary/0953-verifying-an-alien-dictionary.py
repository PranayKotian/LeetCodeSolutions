class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        ordering = {c:i for i,c in enumerate(order)}
        
        for i in range(len(words)-1):
            w1,w2 = words[i],words[i+1]
            
            for w in range(len(w1)):
                if w >= len(w2) or ordering[w2[w]] < ordering[w1[w]]:
                    return False
                if ordering[w2[w]] == ordering[w1[w]]:
                    continue
                break
        
        return True