"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head: return None

        original = head 

        while original is not None:
        #1. create a copy of each node 

            copy = Node(original.val)

        # copy points to original.next

            copy.next = original.next

        # original.next points to copy

            original.next = copy

        # go to the next original node

            original = copy.next 


        #2. iterate through each node again and initialise copy.random to original_node.random.next - this points to our copy node

        original = head

        while original is not None:

            copy = original.next

            if original.random is None:

                copy.random = None 

                original = copy.next

                continue

            copy.random = original.random.next

            original = copy.next


        #3. we now point each copy node to the next copy node and return the head 

        original = head
       

        #save the head

        copyHead = head.next        

        current_copy = copyHead

        
        while original is not None:

            #skip the copy

            original.next = original.next.next

            #move original pointer
            
            original = original.next

            if original is not None:

                #if not end of the list good, point the copy to the next copy

                current_copy.next = original.next

            else:
                
                #end of the list

                current_copy.next = None

            current_copy = current_copy.next

        return copyHead
