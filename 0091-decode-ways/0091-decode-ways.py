class Solution:
    @cache
    def numDecodings(self, s: str) -> int:
        if s == "":
            return 1
        if s[0] == "0":
            return 0
        if s[:2] in set([str(i) for i in range(10,27)]):
            return self.numDecodings(s[1:]) + self.numDecodings(s[2:])
        return self.numDecodings(s[1:])