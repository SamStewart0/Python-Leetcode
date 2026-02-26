# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):

            #start at head
            curr = head
            prev = None

            while curr is not None:
                #get the next node in the list before link is broked
                nextNode = curr.next
                #switch direction of pointer
                curr.next = prev
                #shift previous pointer current is now previous
                prev = curr
                #shift current pointer current is now next node 
                curr = nextNode
            
            #return pointer for previous as this is now first pointer of the linked list
            return prev