class Solution(object):
    def removeElement(self, nums, val):

        #k pointer to move nums that arent val to beginning of array
        k = 0

        for i in range (len(nums)):

            if nums[i] != val:
                
                #place num in correct position
                nums[k] = nums[i]
                
                #move k pointer forward
                k += 1
        
        #return k
        return k
        
