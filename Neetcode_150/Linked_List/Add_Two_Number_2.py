class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        #if either head is None, the sum is the other list
        if l1 or l2 is None:

            if l1 is None: return l2

            if l2 is None: return l1

        #create dummy node for return

        dummy = ListNode(0)

        #carry variable
        
        carry = 0

        current = dummy

        #while anything still has a value

        while l1 or l2 or carry:

            #define the next node and link

            nextNode = ListNode(0)

            current.next = nextNode

            #to allow for one loop, if the value does not exist we replace it with zero

            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            sum = val1 + val2 + carry

            #use floor division to calculate the carry

            carry = sum//10

            #use modulo to get value for result node (mod to ignore the carry)

            nextNode.val = sum%10

            #move our current pointer

            current = nextNode

            #increment l1 and l2 pointers if they exist

            if l1 is not None:
                l1 = l1.next

            if l2 is not None:
                l2 = l2.next

        #deal with final carry if it exists

        if carry>0:

            current.next = listNode(carry)

        return dummy.next
