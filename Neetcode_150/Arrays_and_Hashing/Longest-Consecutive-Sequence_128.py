class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        #init a max length counter
        
        maxLength = 0

        #turn nums to a set for instant lookup

        nums = set(nums)

        #iterate through nums

        for num in nums:

            if (num-1) not in nums:

                currentLength = 1
            
                #nums + 1 = next

                next = num + 1

                #while next in nums

                while next in nums:

                    #currentLength += 1

                    currentLength += 1

                    next += 1
        
                #if currentLength>maxLength

                if currentLength>maxLength:

                    maxLength = currentLength
                        

        return maxLength
