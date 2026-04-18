#Define L and R pointers

        L = 1
        R = max(piles)

        #Define minK for case when we have a K that matches H but is not the min 

        min_k = R

        while L <= R:

            #find midK

            mid_k = (L + R) // 2

            current_hours = 0

            #find currentHours using midK 

            for pile in piles:

                    #this lines forces python to round up the floor division instead of down, aligning with constraint if pile[i] < k he finishes the pile and no more 

                current_hours += -(-pile // mid_k)

            #if current_hours is less than or equal to H this is a new min

            if current_hours <= h:

                min_k = mid_k

                R = mid_k - 1

            #else Koko needs to eat more bananas

            else:

                L = mid_k + 1

        return min_k
