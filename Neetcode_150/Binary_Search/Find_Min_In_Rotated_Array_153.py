class Solution:
    def findMin(self, nums: List[int]) -> int:

        # L and R pointers
        L = 0 
        R = len(nums) - 1
        
        while L < R:

            mid = (L+R) // 2
            left_val = mid - 1

            #if mid value is smaller than the value to the left this is the inflection point (min value) so return mid 

            if nums[mid] < nums[left_val]:

                return nums[mid]

            #if mid value is greater than the value at the end of the array, then we know the min value is in the right side so we move the L pointer up

            elif nums[mid] > nums[R]:

                L = mid + 1

            #else we move the R pointer down

            else: 

                R = mid - 1

        return nums[L]
