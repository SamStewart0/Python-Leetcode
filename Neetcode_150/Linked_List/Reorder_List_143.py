# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        0(n) time and 0(1) space approach

        1. use slow and fast pointers to find the middle of the list 
        2. reverse the second part of the list, for merging
        3. merge the list using two pointers
        4. if there are any remaining nodes are one of the nodes is none, then add this as the last link of our list
        """
        
        #1. use slow and fast pointers to find the middle of the list 

        slow, fast = head, head

        while fast and fast.next:

            fast = fast.next.next
            slow = slow.next

        second_half = slow.next
        slow.next = None

        #2. reverse the second part of the list, for easier merging

        current,previous = second_half, None

        while current is not None:

            nextNode = current.next

            current.next = previous

            previous = current

            current = nextNode

        #reassign second half as we reversed pointers
        second_half = previous

        #3. merge the list using two pointers

        p1, p2 = head, second_half

        while p1 is not None and p2 is not None:

            #Save p1_next_node and p2_next_node
            p1_next_node = p1.next
            p2_next_node = p2.next

            #p1 points to p2 and p2 points to p1's next node
            p1.next = p2
            p2.next = p1_next_node

            #increment pointers
            p1 = p1_next_node
            p2 = p2_next_node

        return head
