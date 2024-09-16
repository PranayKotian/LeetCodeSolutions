class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0
        
        n = len(wordList)
        shortestpath = {word:n+1 for word in wordList}
                
        q = deque([beginWord])
        words = 1
        while q:
            words += 1
            for a in range(len(q)):
                w1 = q.popleft()
                for w2 in wordList:
                    diff = 0
                    for i in range(len(beginWord)):
                        if w1[i] != w2[i]:
                            diff += 1
                        if diff > 1:
                            break
                    if diff == 1:
                        if w2 == endWord:
                            return words
                        if shortestpath[w2] > words:
                            shortestpath[w2] = words
                            q.append(w2)
        
        return 0