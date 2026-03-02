class Solution(object):
    def isAnagram(self, s, t):

        #impossible to be anagram if different lengths 
        
        if len(s) != len(t):

            return False

        #create dictionary to keep count of chars
        
        count = {}
      
        #add each char in s to dict
        
        for char in s:

            if char not in count:

                count[char] = 1
            
            else:

                count[char] += 1

        #decrement count for each char in t
        
        for char in t:
           
            #if char not in count impossible to be anagram
           
            if char not in count:

                return False

            count[char] -= 1

        #for each char in count, if count !=0, it appeared too many or too little times so false
        
        for value in count.values():

            if value != 0:

                return False
        
        return True



        
