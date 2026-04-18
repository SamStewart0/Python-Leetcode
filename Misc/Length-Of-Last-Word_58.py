class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        #split each word by whitespace

        words = s.split()

        #get the word at the end of the array 

        lastWord = words[len(words)-1] 

        #return the length of last word

        return len(lastWord)
