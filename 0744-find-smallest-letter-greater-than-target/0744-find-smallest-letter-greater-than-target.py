class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        #Binary Search Solution
        #Time: O(logn) Space: O(1)
        
        if ord(letters[-1]) <= ord(target) or ord(letters[0]) > ord(target):
            return letters[0]
        
        l = 1
        r = len(letters)-1
        
        letter_vals = [ord(letter) for letter in letters]
        target_val = ord(target)
        
        while l <= r:
            m = (l+r)//2
            if letter_vals[m] <= target_val:
                l = m+1
            elif letter_vals[m] > target_val and letter_vals[m-1] > target_val:
                r = m-1
            else:
                return letters[m]
        