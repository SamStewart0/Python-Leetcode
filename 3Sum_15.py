class Solution(object):
    def threeSum(self, nums):
        
        #sort the array
        #use a for i loop to iterate through the nums
        #use a while j < k loop to search the array for triplets that meet the criteria
        
        #sort arra
        nums.sort()

        results = []

        for i in range (len(nums)-2):

            #if duplicate then skip
            if i > 0 and nums[i] == nums[i-1]:
                continue

            #set our L and R pointers relative to the i pointers
            L = (i+1)
            R = (len(nums))-1

            #while L and R arent crossing over
            while L < R:
                
                #if our condition for triplet is true
                if nums[i] + nums[L] + nums[R] == 0:

                    #create the triplet and append
                    triplet = [nums[i], nums[L], nums[R]]

                    results.append(triplet)

                    #move pointers
                    L += 1
                    R -= 1

                    #if our new position is a duplicate, then keep moving them
                    while L < R and nums[L] == nums[L-1]:
                        L += 1

                    while L < R and nums[R] == nums[R+1]:
                        R -= 1  

                #if the sum is too small increment L pointer for larger value
                elif nums[i] + nums[L] + nums[R] < 0:

                    L += 1
                    
                #otherwise too big so decrement right pointer
                else:

                    R -= 1

        return results
