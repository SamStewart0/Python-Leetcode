class Solution(object):
    def plusOne(self, digits):

        #starting from end of array
        for i in range (len(digits) -1, -1, -1):
            
            #if digit is a 9 we make it zero
            if digits[i] == 9:

                digits [i] = 0
            
            #this handles the carry for if digit is 9, or just simple incrementation
            else:

                digits[i] += 1
                #returns digits
                return digits

        #if all 9s we return digits array with 1 at front of array
        return [1] + digits
     
