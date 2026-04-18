class Solution(object):
    def maxArea(self, height):

        #iterate using L and R pointer
        #create max area variable to track max area 

        R = (len(height))-1
        L = 0 

        maxArea = 0 

        #stop when our pointers cross

        while L < R:

            #get currentArea
            
            currentArea = (min(height[L],height[R])*(R-L))

            #compare with max area
            
            if currentArea > maxArea:
                maxArea = currentArea

            #increment pointers accordingly

            if height[L] > height[R]:
                R -= 1

            else:
                L += 1

        return maxArea
