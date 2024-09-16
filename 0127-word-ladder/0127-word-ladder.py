class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0
        
        n = len(wordList)
        wordLen = len(beginWord)
        visited = set([beginWord])
                
        q = deque([beginWord])
        words = 1
        while q:
            words += 1
            for a in range(len(q)):
                w1 = q.popleft()
                for w2 in wordList:
                    diff = 0
                    for i in range(wordLen):
                        if w1[i] != w2[i]:
                            diff += 1
                        if diff > 1:
                            break
                    if diff == 1:
                        if w2 == endWord:
                            return words
                        if w2 not in visited:
                            q.append(w2)
                            visited.add(w2)
        
        return 0