class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        smallest_letter = "{"
        for letter in letters:
            if ord(letter) > ord(target) and ord(letter) < ord(smallest_letter):
                smallest_letter = letter
        if smallest_letter == "{":
            return letters[0]
        return smallest_letter
    
    