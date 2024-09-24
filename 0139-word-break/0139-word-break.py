class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        #DP Solution
        #Time: O(s*w) Space: O(s)
        
        arr = [0 for i in range(len(s)+1)]
        arr[0] = 1
        
        for i in range(len(arr)):
            if arr[i]:
                for word in wordDict:
                    if s[i:i+len(word)] == word:
                        arr[i+len(word)] = 1
        
        return arr[-1] == 1