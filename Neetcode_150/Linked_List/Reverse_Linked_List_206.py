class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        current = head 
        prev = none 

        nextNode = current.next
        current.next = prev

        prev = current 
        current = nextNode 
        '''

        #set our current and previous pointers
        current = head
        prev = None

        #while current is not null (end of the list)
        while current is not None:

            #get the next node
            nextNode = current.next
            #reverse the pointers
            current.next = prev

            #move our pointers up
            prev = current
            current = nextNode

        #return the head of the new list
        return prev
