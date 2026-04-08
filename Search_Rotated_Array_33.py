class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        first we find our inflection point (point where nums[mid] < nums[left_val])

        then we identify which side of the inflection point we need 

        from here we perform a standaard binary search ont he correct part of the list
        '''

        #first we find our inflection point, so we can binary search the correct section of the list

        L = 0
        R = len(nums)-1

        inflection = None
        
        while L < R:

            mid = (L+R) // 2
            left_val = mid - 1

            if nums[mid] < nums[left_val]:

                #we have found the inflection so break out of the loop

                inflection = mid

                break

            #this means the min value(inflection point) is in the right side of the array

            elif nums[mid] > nums[R]:

                L = mid + 1

            else:

                R = mid - 1
        
        #if we go through the whole loop without finding the inflection, L is the index of the inflection

        if inflection is None:

            inflection = L

        
        R = len(nums)-1 


        #return inflection if it is the target

        if nums[inflection] == target:

            return inflection

        #if this is true our target is in the left side of the array

        elif target > nums[inflection] and target > nums[R]:

            R = inflection - 1
            L = 0

        #else the right

        else: 
            
            R = len(nums)- 1
            L = inflection - 1 

        #normal binary search to find the target

        while L <= R:

            mid = (L+R)//2

            if nums[mid] == target:

                return mid

            elif nums[mid] < target:

                L = mid + 1

            else:

                R = mid - 1

        return -1
