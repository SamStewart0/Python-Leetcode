class Solution:
    def isValid(self, s: str) -> bool:

        #dictionary to compare bracket types

        brackets = {
            '}' : '{',
            ']' : '[',
            ')' : '(',
        }

        #stack to keep track of the order in which we see the brackets

        stack = [] 

        #if length of s is not even return false

        if len(s) % 2 != 0:

            return False

        #iterate through the string 

        for bracket in s:
            
            #if opening bracket, add it to the stack

            if bracket == '(' or bracket == '[' or bracket == '{':

                stack.append(bracket)

                #skip rest of the code

                continue

            #if first bracket is closing and stack is empty, not valid return false

            if len(stack) == 0:

                return False

            #if the closing bracket is not the correct closing bracket, not valid return false

            if brackets[bracket] != stack[-1]:

                return False

            #if it is remove it from the stack
            stack.pop()

        #if items still left in the stack return false
        if len(stack) > 0:

            return False

        #if we made it this far it is valid so return true
        return True
