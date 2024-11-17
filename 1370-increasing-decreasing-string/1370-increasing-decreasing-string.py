class Solution:
    def sortString(self, s: str) -> str:
        
        
        sorted_letters = sorted(list(set(s)))
        res = []
        count_letters = Counter(s)
        while True:
            for letter in sorted_letters:
                if count_letters[letter] >= 1:
                    res.append(letter)
                    count_letters[letter] -= 1
                if len(res) == len(s):
                    return "".join(res)
            for letter in sorted_letters[::-1]:
                if count_letters[letter] >= 1:
                    res.append(letter)
                    count_letters[letter] -= 1
                if len(res) == len(s):
                    return "".join(res)