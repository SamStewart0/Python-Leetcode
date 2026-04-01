class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        #to store our results

        days = [0] * len(temperatures)

        #to store indexes of our temperatures

        tempIndexes = []

        #iterate through temps get index so we can work out difference in days

        for i, temp in enumerate(temperatures):

            #if the stack is not empty and if current temp is greater than temp at top of the stack

            while tempIndexes and temp > temperatures[tempIndexes[-1]]:

                #pop the index off and get the value

                index = tempIndexes.pop()

                #the difference between current index and index from the stack is the answer to next highest temp
                #we append this to days array at index of the day in temperatures

                days[index] = i - index

            #this adds our index to the tempIndex stack after all checks

            tempIndexes.append(i)


        #return the resulting array
        
        return days
