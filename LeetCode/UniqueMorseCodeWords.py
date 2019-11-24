#https://leetcode.com/problems/unique-morse-code-words/
#Title: Unique Morse Code Words
#Difficulty: Easy
#Language: Python3
#Author: Pranay Kotian

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        morseWords = []
        
        #Converts all words into morsecode and adds them to list morseWords
        blankStr = ""
        addWord = 1
        for i in range(len(words)):
            for j in words[i]:
                blankStr += morse[ord(j) - 97]
                
            #Checks if morse word is already in list (adds if not)
            for k in range(len(morseWords)):
                if (morseWords[k] == blankStr):
                    addWord = 0
                    break
            if addWord:
                morseWords.append(blankStr)
            addWord = 1
            blankStr = ""
            
        #Returns the len of the list of morse words (which only contains unique words)
        return len(morseWords)
        