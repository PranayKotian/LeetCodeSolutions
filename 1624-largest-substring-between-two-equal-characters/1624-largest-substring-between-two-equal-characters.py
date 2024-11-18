class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        
        if len(set(s)) == len(s):
            return -1
        
        first_occurence = {}
        res = 0
        for i,char in enumerate(s):
            if char not in first_occurence:
                first_occurence[char] = i
            else:
                res = max(res, i-first_occurence[char]-1)
        return res