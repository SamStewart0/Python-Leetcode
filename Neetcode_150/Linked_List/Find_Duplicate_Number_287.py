class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        '''
        Find duplicate using Floyds algo

        use index values as pointers

        1. use slow and fast to find cycle
        2. once cycle found, reset slow pointer to zero
        3. increment by one until they meet again
        4. return index pointed to as this is duplicate (cycle)

        '''
        
        #init slow and fast from zero

        slow, fast = nums[0], nums[nums[0]]

        #when the cycle occurs we break out of the loop

        while slow != fast:

            slow = nums[slow]

            fast = nums[nums[fast]]

        #reset slow to beggining

        slow = 0

        #when they meet again, the index is the duplicate

        while slow != fast:

            slow = nums[slow]
            fast = nums[fast]

        return slow
