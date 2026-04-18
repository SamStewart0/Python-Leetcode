        # Get row and column values.

        r = len(matrix)
        c = len(matrix[0])
        
        # Init Left and Right pointers.

        L = 0
        R = (r*c)-1


        # While pointers are not overlapped.

        while L <= R:

            # Calculate mid point.

            mid = (L + R) // 2

            midRow = mid//c
            midCol = mid%c


            # If middle value is target return True.
            # Otherwise increment pointers accordingly.

            if matrix[midRow][midCol] == target:

                return True

            
            elif matrix[midRow][midCol] < target:

                L = mid + 1

            else:

                R = mid - 1

        # If we break out of the loop the value was not found so return False.
        
        return False
