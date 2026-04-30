class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        current = head
        length = 0

        #get the length of the LL so we know how many iterations
        
        while current is not None:

            current = current.next 

            length += 1

        #early exit

        if k > length:

            return head

        #calcuate iterations

        iterations = length//k

        #init dummy node for return and link it to head 

        dummy = ListNode(0)

        dummy.next = head

        prev = dummy

        current = head

        prev_tail = dummy

        for i in range (0, iterations):

            #current_tail is the first value in our k sub section

            current_tail = current

            for i in range(0,k):
                
                #standard reversing of linked list
                
                nextNode = current.next 

                current.next = prev

                prev = current

                current = nextNode

            #set our tail pointers, prev tail points to the start of the current k section
            #current_tail points to the start of the next k nodes, unless we iterate again

            prev_tail.next = prev
            current_tail.next = current

            #move tail pointers

            prev_tail = current_tail

        return dummy.next
