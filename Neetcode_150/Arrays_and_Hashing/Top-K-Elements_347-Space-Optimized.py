import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #count nums and frequency
        counts = Counter(nums)

        #create an array of freq,num tuples
        #freq is negative as heap pushes min to top by default so have to trick it
        max_heap = [(-freq, num) for num, freq in counts.items()]

        #creates the heap, organises everything into order with smallest at index zero
        heapq.heapify(max_heap)

        #results array
        max_frequency = []

        #iterate k times
        for _ in range(k):

            #append most frequent number to the array also pops the tuple off the heap 
            max_frequency.append(heapq.heappop(max_heap)[1])

        return max_frequency
