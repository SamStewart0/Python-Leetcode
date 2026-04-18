import heapq
from collections import Counter
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        max_value = []
        max_heap = []
        to_remove = Counter()

        for i in range(len(nums)):

            #first we add the values from the first k sized window

            heapq.heappush(max_heap, -nums[i])

            #if our window is too big, a value will be leaving the window so we need to prepare

            if i >= k:
                leaving_val = nums[i-k]
                to_remove[leaving_val] += 1

            #now our window is valid we get the value at the top of the heap and check is isnt stale, if it is we pop it

            while max_heap and to_remove[-max_heap[0]] > 0:
                removed = -heapq.heappop(max_heap)
                to_remove[removed] -= 1

            #this means all stale values are removed so append the top of the heap to our max_value array
            
            if i >= k-1:
                max_value.append(-max_heap[0])

        return max_value
