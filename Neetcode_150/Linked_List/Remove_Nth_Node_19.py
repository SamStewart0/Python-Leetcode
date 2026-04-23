class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        size = 0
        get_size_pointer = head

        #get the size of our list

        while sizePointer is not None:

            get_size_pointer = get_size_pointer.next
            size += 1

        #if n is the size of the list this means we need to remove the head

        if size == n:

            return head.next

        #set our p1 pointer to the node before the one we are removing

        p1 = head 

        for i in range((size-n-1)):

            p1 = p1.next

        #point this node to the node after the one we are removing 
            
        p1.next = p1.next.next

        return head
        
        
