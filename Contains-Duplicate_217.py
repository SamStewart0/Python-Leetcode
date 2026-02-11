class Solution(object):
    def containsDuplicate(self, nums):
        
        #empty set to store and check for value  
        seen = set()   

        #loop through nums
        for num in nums:

            #if seen return true
            if num in seen:

                return True
            
            #else add value to seen
            seen.add(num)

        #return false if no match
        return False