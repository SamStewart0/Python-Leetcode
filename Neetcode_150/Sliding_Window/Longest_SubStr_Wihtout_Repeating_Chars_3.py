        if not s:

            return 0

        #Define L and R pointers, longest_sub var and hashmap for seen values 

        L = 0
        R = 0

        longest_sub = 0

        seen = dict()

        while R < len(s):

            #Only update L if it is inside the sliding window and in seen
    
            if s[R] in seen and seen[s[R]] >= L:

                L = seen[s[R]] + 1

            seen[s[R]] = R

            R += 1

            #update longest sub var

            longest_sub = max(R - L, longest_sub) 

        #return longest sub var

        return longest_sub
