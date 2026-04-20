# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        '''
        we need to merge the list, without creating a new list - change the direction of the pointers

        we need 2 pointers, one for each list

        we need to save the head of the list initially 
        '''

        #define our pointers as p1 and p2 

        p1 = list1
        p2 = list2

        #create a dummy node (head) that we can return as the start of our linked list

        dummy = ListNode(0)

        current = dummy

        #while both nodes are not null

        while p1 is not None and p2 is not None:

            if p1.val <= p2.val:
                
                #set our current pointers next node to p1

                current.next = p1

                #move our p1 pointer

                p1 = p1.next

                #move our current pointer to the next node in the list (p1 node we just added)

                current = current.next 

            #else we do the same but with p2

            else:

                current.next = p2

                p2 = p2.next

                current = current.next 
        
        #if p1 still has nodes, attach them. otherwise, attach p2.

        current.next = p1 if p1 is not None else p2

        return dummy.next
