class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        '''
        Two pointers one slow and one fast
        Floyd’s Cycle-Finding Algorithm
        If there is a cycle in the list - the pointers will meet
        '''

        fast = head
        slow = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            if fast == slow:
                return True
    
        return False
