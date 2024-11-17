class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        
        def word_to_int(word: str) -> int:
            idx = 0
            while idx != len(word) and word[idx] == "a":
                idx += 1
            
            nums = []
            for letter in word[idx:]:
                nums.append(str(ord(letter)-ord("a")))
            
            if nums == []:
                return 0
            return int("".join(nums))
            
        return word_to_int(firstWord) + word_to_int(secondWord) == word_to_int(targetWord)