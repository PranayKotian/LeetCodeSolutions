class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        #Multiple Pass Sliding Window Solution
        #Time: O(s) Space: O(w)
        
        res = []
        wordLen = len(words[0])
        concatLen = len(words)*wordLen
        
        for start in range(0,wordLen):
            l = start
            c = Counter(words)
            for r in range(start,len(s),wordLen):
                w = s[r:r+wordLen]
                if w not in c:
                    c = Counter(words)
                    l = r+wordLen
                    continue
                else:
                    c[w] -= 1
                    if r-l+1 > concatLen:
                        c[s[l:l+wordLen]] += 1
                        l += wordLen
                    if all(i==0 for i in c.values()): 
                        res.append(l)
        return res
        
        
        """
        #Optimized Brute Force Solution
        #Iterate through string in a window of size 3
        #If the window is a word in words: check if substring is permutation of words
        #Add index to result
        #TLE - 179 / 182
        
        c = Counter(words)
        def checkSubstring(i):
            if sum(c.values()) == 0:
                return True
            w = s[i:i+wordLen]
            if w in c and c[w] != 0:
                c[w] -= 1
                res = checkSubstring(i+wordLen)
                c[w] += 1
            else:
                res = False
            return res
        
        res = []
        wordLen = len(words[0])
        concatLength = len(words)*wordLen
        for idx in range(len(s)-concatLength+1):
            if checkSubstring(idx):
                res.append(idx)
        return res
        """