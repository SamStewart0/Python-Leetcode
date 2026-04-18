class MinStack:

    #this function needs to create the stack and the min stack

    def __init__(self):

        self.stack = []
        self.minStack = []
        
    #this function needs to push the value to the stack
    #this function also needs to check if the value is smaller than the current min value in the min stack, if yes then append this value to the min stack

    def push(self, val: int) -> None:

        self.stack.append(val)

        if not self.minStack or val <= self.minStack[-1]:
            
            self.minStack.append(val)

    #this function needs to remove the value at the top of the stack
    #this function also needs to check if the value we are removing is the current min and if it is remove this from the min stack

    def pop(self) -> None:

        if not self.stack:

            return

        if self.stack[-1] == self.minStack[-1]:

            self.minStack.pop()

        self.stack.pop()

        
    #this function needs to get the value from the top of the stack without removal

    def top(self) -> int:
        
        if not self.stack:

            return -1

        return self.stack[-1]
        
    #this function needs to get the current min value from the min stack
    
    def getMin(self) -> int:

        if not self.minStack:

            return -1 

        return self.minStack[-1]
