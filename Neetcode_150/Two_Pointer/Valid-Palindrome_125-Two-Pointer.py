class Solution:
    def isPalindrome(self, s: str) -> bool:

        #two pointer solution

        #i pointer at index 0, j pointer at len(s)
        
        j = len(s) - 1 
        i = 0

        #while i>j as pointers do not need to cross

        while i < j:

            #if value is not a num or char move respective pointers

            if not s[i].isalnum():
                
                i += 1
                continue

            if not s[j].isalnum():
                
                j -= 1
                continue

            #convert chars to lower

            if s[i].lower() == s[j].lower():

                i += 1
                j -= 1

            #if chars are not equal, not palindrome so return false

            else:

                return False

        return True
