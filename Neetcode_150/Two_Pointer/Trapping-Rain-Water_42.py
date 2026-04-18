class Solution:
    def trap(self, height: List[int]) -> int:
        
        #L R Pointers
        L = 0
        R = len(height)-1

        #total water count
        totalWater = 0 
        
        #track tallest wall on each side
        maxL = 0
        maxR = 0
       

        while L < R:

            #if value at left poionter is smaller, this is our bottleneck(water cannot go higher than this point) so we calculate the water we can trap based on this side
            if height[L] < height[R]:

                #get max L value
                
                maxL = max(height[L], maxL)
                
                #calculate water at this position and add to totalwater tally

                totalWater += maxL - height[L]

                #increment pointer

                L += 1

            #otherwise do this but on the right side
            else:

                maxR = max(height[R], maxR)
                
                totalWater += maxR - height[R]

                R -= 1

        return totalWater 

            
