class Solution:

    def encode(self, strs: List[str]) -> str:

        #define string encoded to add our strings to 

        encoded = ''

        #to encode we iterate through each word in the array

        for word in strs:

            #for each in the array we encode as [length][delimiter][string]

            length = len(word)

            encoded_word = str(length) + '#' + word

            encoded += encoded_word

        return encoded 

    def decode(self, s: str) -> List[str]:

        #pointer for encoded string
        encoded_p = 0

        #define an array as 'decoded'
        decoded = [] 

        #while our pointer is not at the end of the string
        while encoded_p < len(s):

            #initialise j pointer to find length
            j = encoded_p

            while s[j] != '#':
                j += 1

            length = int(s[encoded_p:j])

            #move our p pointer past the delimiter
            encoded_p = j+1

            #get our decoded word
            decoded_word = s[encoded_p : encoded_p + length]

            #add to decoded array
            decoded.append(decoded_word)

            #move encoded string pointer to end of word
            encoded_p += length

        return decoded
