class Solution(object):
    def removeDuplicates(self, nums):

        if not nums:
            return 0

        l = 1

        for r in range (1, (len(nums))):
            
            #if current value is unique place r at left pointer

            if nums[r] != nums[r-1]:

                nums[l] = nums[r]

                #increment left pointer
                l += 1
        
        return l