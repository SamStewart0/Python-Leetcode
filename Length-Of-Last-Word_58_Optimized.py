class Solution:
    def lengthOfLastWord(self, s: str) -> int:
class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        length = 0

        #iterate from end of array
        
        for i in range( len(s) - 1 , - 1, - 1):

            #if s[i] is not space, increment length

            if s[i] != ' ':

                length += 1

            #when s[i] is a space again, break

            elif length > 0:

                break

        return length
