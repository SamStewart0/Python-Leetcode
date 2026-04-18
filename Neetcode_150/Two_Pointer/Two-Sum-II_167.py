class Solution(object):
    def twoSum(self, numbers, target):

        #L and R pointers

        l = 0
        r = (len(numbers))-1
        
        #pointers should never cross
        while l < r:
            
            #get current sum for comparison
            current_sum = numbers[l] + numbers[r]
            
            #if current sum is target return the index
            if current_sum == target:
                return [l+1,r+1]

        #otherwise keep looking
            if target - numbers[l] < numbers[r]:
                r -= 1
            else:
                l += 1 
