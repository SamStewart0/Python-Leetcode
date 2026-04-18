class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        sorted_words = {}
        
        #iterate through the strings and sort

        for word in strs:

            #sorted returns a list so use .join to return a string as list cannot be used as key for dict as they are mutable

            sorted_word = "".join(sorted(word))

            #now we have our key we use setdeafault to check whether the key already exists,
            #if the key does not exist we create it with an empty list and append word
            #if it does we just append word

            sorted_words.setdefault(sorted_word, []).append(word)

            #create new list of lists using the dictionary values 

        return(list(sorted_words.values()))
