class Solution(object):
    def searchInsert(self, nums, target):

        #binary search

        #low and high pointers
        
        low = 0 
        high = len(nums)-1

        #find mid point
        while low <= high:
            
            mid = (low + high) // 2

            if nums[mid] == target:

                return mid
            
            #if element is less than target increment low pointer
        
            elif nums[mid] < target:
                
                low = mid + 1

            else:
                
                #otherwise deincrement high pointer
                
                high = mid - 1

        #if not found low is correct insertion
       
        return low