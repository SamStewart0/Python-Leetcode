class Solution(object):
    def search(self, nums, target):
        

        if not nums:

            return -1


        L = 0
        R = len(nums)-1 

        while L <= R:

            #find midpoint
            mid = (L+R)/2

            #if target return index 

            if nums[mid] == target:

                return mid

            #otherwise increment pointers according

            if nums[mid] < target:

                L = mid+1 

            else:

                R = mid-1

        #return -1 if we finish the algo and do not find target

        return -1
