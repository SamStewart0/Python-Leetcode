class Solution(object):
    def romanToInt(self, s):
        
        numerals = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
        }

        total = 0

        for i in range (len(s) -1):

            if numerals[s[i]] < numerals[s[i+1]]:

                #to account for if value needs to be subtracted
                total -= numerals[s[i]]

            else:

                total += numerals[s[i]]
        
        #return total + last value 
        return total + numerals[s[-1]]
        