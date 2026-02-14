class Solution(object):
    def climbStairs(self, n):

        if n<=2:
            
            return n
        #first steps
        step1 = 1
        step2 = 2

        #for each step between current and n
        for i in range(3, n+1):
        
            #find current
            current = step1+step2
            #slide variables
            step1 = step2
            step2 = current 