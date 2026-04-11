class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        

        #First define Array A and Array B

        A, B = (nums1, nums2) if len(nums1) <= len(nums2) else (nums2, nums1)

        #Define our L and R pointers to binary search the smaller array

        L = 0 
        R = len(A) 

        #Define our half_length as to find the median we need the left and right side of our arrays to be exactly half to find the median

        half_len = ((len(A) + len(B))+1)//2

        while L <= R:
            
            #Define I as the midpoint of Array A

            I = (L+R)//2

            #Define J as the remainder of the amount of values we need on the left side of the partition

            J = half_len - I

            #Define values for A
           
            a_left = A[I - 1] if I > 0 else float('-inf')
            a_right = A[I] if I < len(A) else float('inf')

            #Define values for B
           
            b_left = B[J - 1] if J > 0 else float('-inf')
            b_right = B[J] if J < len(B) else float('inf')

            #If this is correct we break the loop and find the median
            
            if a_left <= b_right and b_left <= a_right:

                break
            
            #If the largest value in our A left side is bigger than the smallest in our B right then our partition is incorrect
            #and we need less values from Array A
            
            elif a_left > b_right:

                R = I - 1

            #Else means our partition is still incorrect but the opposite way so we take more values from Array A

            else: 
            
                L = I + 1

        #Return the median accordingly

        total_len = len(A) + len(B)

        if total_len % 2 == 0:

            return (max(a_left, b_left) + min(a_right, b_right)) / 2
        
        else:

            return max(a_left, b_left)



        '''
        We place our L and R pointers in the smaller array and find the midpoint (I pointer)

        To find our J pointer for the larger array 
        1. we take the length of both arrays,add 1 and divide by 2 as we need the left and right side to be exactly half (median)
        2. we subtract this from the amount of elements in the left half of our smaller array to get the position for our J pointer 
        J = half_len - I

        Once we have our pointers set up we need to check if we have partitioned correctly
        
        lets call the smaller array A and bigger B

        To check the partition we need to check if A[I-1] <= B[J] and B[J-1] <= A[I]
            1. if this is the correct then we have partitioned correctly
            2. if A[I-1] > B[J] the value in A is too big so we decrement our R pointer
            3. if B[J-1] > A[I] the value in B is too big so we increment our L pointer
        '''
