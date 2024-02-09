class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        ordering = {c:i for i,c in enumerate(order)}
        
        for i in range(len(words)-1):
            w1,w2 = words[i],words[i+1]
            
            for w in range(len(w1)):
                if w >= len(w2):
                    return False
                if w2[w] != w1[w]:
                    if ordering[w2[w]] < ordering[w1[w]]:
                        return False
                    else:
                        break
        
        return True