class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        total = 1
        count_zero = 0

        #find total product for array and get zero count

        for num in nums:

            if num == 0:

                count_zero += 1

                continue

            total = total * num

        #if more than one zero return array of zeros

        if count_zero > 1:

            return [0] * len(nums)

        #if one zero, each index in the array apart from value zero is zero

        if count_zero == 1:

            return [0 if i != 0 else total for i in nums]

        #if no zeros, each position is total//i

        return [total // i for i in nums]

            
