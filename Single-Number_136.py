class Solution(object):
    def singleNumber(self, nums):

        result = 0 

        for num in nums:

            #XOR num with result
            result ^= num

        return result 
        