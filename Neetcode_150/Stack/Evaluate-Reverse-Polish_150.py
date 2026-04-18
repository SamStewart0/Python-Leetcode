class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        #function to perform operations
        
        def operations(operator,x,y):
            
            if operator == "+":
                return x+y

            elif operator == "-":
                return x-y

            elif operator == "/":
                return int(x/y)

            else:
                return x*y



        #list to check for operator
        
        operators = ["+", "-", "*", "/"]
        
        #result stack for calculations
        
        result = []
        
        
        for token in tokens:

            #if token is not an operator append to right side of stack
            
            if token not in operators:
                #change data type from str to int
                result.append(int(token))

            #if the token is an operator we perform the operation by popping off the stack

            else:

                x = result.pop()
                y = result.pop()
                result.append(operations(token,y,x))

        #return the result 

        return result.pop()

            
