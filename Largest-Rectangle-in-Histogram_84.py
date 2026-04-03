class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        #use stack to store seen bars

        stack = []

        maxArea = 0 

      

        for i, height in enumerate(heights):

            #while the current height is smaller than the top of the stack: this is the right boundary of the top of the stack and potentitally more
            while stack and height < stack[-1][0]:

                #calculate max aree

                currentHeight, currentIndex = stack.pop()

                rightBound = i

                #left boundary is the index value at the top of the stack (value before the current) as we used an increasing monotonic stack (each value behind the current values on the stack should be smaller)

                leftBound = stack[-1][1] if stack else -1

                maxArea = max(maxArea, (currentHeight * (rightBound - leftBound - 1)))

            #append to the stack after boundary checks

            stack.append([height,i])

        #if we have still have values left in the stack

        if stack:

            #right bound is the end of the histogram/array
        
            rightBound = len(heights)

            #same area calculations
        
            while stack:

                currentHeight, currentIndex = stack.pop()

                leftBound = stack[-1][1] if stack else -1

                maxArea = max(maxArea, (currentHeight * (rightBound - leftBound - 1)))

        return maxArea

       
       #stack.pop() = current
       #right boundary = i
       #left boundary = stack[-1][1] if stack else -1 
       #currentHeight = current[0]

       #maxArea = max(maxArea, (currentHeight * (rightBound - leftBound - 1))

       #stack.append([height , i])

       #right bound = len(heights)
       
       #while stack 

       #stack.pop() = current
       #left boundary = stack[-1][1] if stack else -1 
       #currentHeight = current[0]

       #maxArea = max(maxArea, (currentHeight * (rightBound - leftBound - 1))

       #return maxArea

       

            
