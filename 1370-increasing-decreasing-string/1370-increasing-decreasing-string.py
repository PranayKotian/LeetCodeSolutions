class Solution:
    def sortString(self, s: str) -> str:
        
        #Counter + Sorting Solution
        #Time: O(n) Space: O(n)
        
        res = []
        letter_count = Counter(s)
        while True:
            for letter in sorted(letter_count.keys()):
                res.append(letter)
                letter_count[letter] -= 1
                if letter_count[letter] == 0:
                    del letter_count[letter]
                if len(res) == len(s):
                    return "".join(res)
            for letter in sorted(letter_count.keys(), reverse=True):
                res.append(letter)
                letter_count[letter] -= 1
                if letter_count[letter] == 0:
                    del letter_count[letter]
                if len(res) == len(s):
                    return "".join(res)