class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #hashmap to count num frequencies

        count = {}

        #iterate through the array and count the frequencies
        #key is num value count

        for n in nums:
 
            #if key exists we overwrite it plus one, otherwise we create the key with value 1
            
            count[n] = 1 + count.get(n,0)

        #create a list of lists to group numbers by frequency is index
        
        freq_buckets = [[] for _ in range (len(nums)+1)]

        #iterate through counts
        
        for num, f in count.items():

            #append the num as the index of the frequency
            
            freq_buckets[f].append(num)

        #results array
        
        most_frequent = []

        #iterate from the end of array for most frequent
        
        for i in range ((len(freq_buckets) - 1), 0, -1):

            for num in freq_buckets[i]:

                most_frequent.append(num)

            #when we have k amount of most frequent return the array
                
                if len(most_frequent) == k:

                    return most_frequent
