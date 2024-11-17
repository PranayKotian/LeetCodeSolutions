class Solution:
    def sortString(self, s: str) -> str:
        
        #Counter + Sorting Solution
        #Time: O(n) Space: O(n)
        
        res = []
        letter_count = Counter(s)
        while letter_count:
            for letter in sorted(letter_count):
                res.append(letter)
                letter_count[letter] -= 1
                if letter_count[letter] == 0:
                    del letter_count[letter]
            for letter in sorted(letter_count, reverse=True):
                res.append(letter)
                letter_count[letter] -= 1
                if letter_count[letter] == 0:
                    del letter_count[letter]
        return "".join(res)