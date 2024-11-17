class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        
        #Python Solution
        #Time: O(n) Space: O(n)
        return "".join(word1) == "".join(word2)