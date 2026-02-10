class Solution(object):
    def twoSum(self, nums, target):
        
        #define the dictionary

        seen = {}

        #enumerate through nums

        for i,num in enumerate(nums):

            #calculate the target     
            needed = target - num
            
            #if needed is in seen (dictionary)
            if needed in seen:

                #return the index from seen and i
                
                return[seen[needed], i]
           
            #otherwise add the value to seen at index of the i and loop
            seen[num] = i