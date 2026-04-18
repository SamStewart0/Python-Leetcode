class Solution(object):
    def wordPattern(self, pattern, s):

        #create an array of the words in s 
        
        words = s.split()

        #edge case, if lengths do not match, bijection impossible
        
        if len(words) != len(pattern):

            return False

        #dict for pattern(char) to word mapping
        
        char_word = {}

        #set of seen words instantly lookup if a word has already been assigned to a char in the pattern

        seen_words = set()

        for i, letter in enumerate(pattern):

            #get each word from array

            current_word = words[i]

            #if we have seen the letter but the word does not match, bijection impossible

            if letter in char_word:
                   
                if char_word[letter] != current_word:
                        
                    return False
                
                #if it is a brand new letter but we have seen the word before, bijection impossible
                
            else:

                if current_word in seen_words:
                        
                    return False

                #if we get to here the char to word mapping is safe so we save it 
                char_word[letter] = current_word
                    
                seen_words.add(current_word)

            #if we get to here, its a bijection so return true
            
        return True


        
