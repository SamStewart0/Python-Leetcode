import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        '''
        k can be 0 -> 10,000
        lists[i].length can be 0 -> 500
        value in list can be negative
        '''

        #use a min heap to store all values in the list with the smallest being at the top of the heap
        #pop values off the top of the head, linking them together in the list

        #first flatten our list

        flat_list = []

        for head in lists:

            current = head

            while current is not None:

                flat_list.append(current.val)

                current = current.next

        heapq.heapify(flat_list)

        #create a dummy and return the sorted list

        dummy = ListNode(0)

        current = dummy

        while flat_list:

            #get the min value from our heap
            value = heapq.heappop(flat_list)

            nextNode = ListNode(value)
            
            current.next = nextNode

            current = nextNode

        return dummy.next
