class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        We have a criteria which is window length - most_frequent <= K

        update most_freq everytime we increment R

        while this is true we can increment our R pointer

        while this is false we contract our L pointer until this is true again

        dictionary to keep track of key value pairs
        '''

        L = 0
        R = 0

        #use defaultdict so we can add keys without checking if they already exist or not

        counts = defaultdict(int)

        #max frequency to check k constraint

        max_frequency = 0

        #max length for final answer

        max_length = 0

        for R in range(len(s)):

            #add the value at R to the dict and update max_frequency

            counts[s[R]] += 1

            max_frequency = max(max_frequency, counts[s[R]])

            #if we have broken the k constraint we need to contract our window

            while ((R-L+1)-max_frequency > k):

                counts[s[L]] -= 1
            
                L += 1

            #update max length when we know we have a valid window

            max_length = max(max_length, R - L + 1)

        return max_length
