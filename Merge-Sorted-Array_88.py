class Solution(object):
    def merge(self, nums1, m, nums2, n):
       
        #3 pointers p1 end of valid nums in nums1, p2 end of nums2 and p at end of num1

        p1 = m - 1
        p2 = n - 1
        p = m + n - 1

        while p1 >= 0 and p2 >= 0:
            
            #if p1 value is bigger, move it to p pointer
            if nums1[p1] > nums2[p2]:

                nums1[p] = nums1[p1]

                p1 -= 1

            #else p2 value is bigger, move it to p
            else:

                nums1[p] = nums2[p2]

                p2 -= 1

            p -= 1

        #if nums1 runs out of values, fill nums1 with the remaining value in nums 2  
        while p2 >= 0:

            nums1[p] = nums2[p2]

            p2 -= 1
            p -= 1
          
    
        
