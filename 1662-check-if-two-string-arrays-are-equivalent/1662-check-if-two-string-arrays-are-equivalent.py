class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        
        #Generators and Yield Solution
        #Time: O(n) Space: O(1)
        
        def generator(wordList: List[str]):
            for segment in wordList:
                for char in segment: 
                    yield char
            yield None
        
        return all(c1 == c2 for c1,c2 in zip(generator(word1), generator(word2)))
        
        """
        #Naive Python Solution
        #Time: O(n) Space: O(n)
        return "".join(word1) == "".join(word2)
        """