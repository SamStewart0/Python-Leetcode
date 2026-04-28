'''
Keeps track of age discards the last recently used item when put is used

How to keep track of age? 

combine a hashmap and a linked list

linked list used to find LRU - the tail of the list is the last recently used 

hashmap to store the pointers to the nodes in the linked list - if the value exists in the hashamp we jump to it and return the value 


'''

#class for the Node
class Node:

    def __init__(self, key: int, val: int):
        
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        
        #init current capacity

        self.current_capacity = 0
        self.capacity = capacity

        #head and tail for easy remove/push

        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)

        #link them up

        self.head.next = self.tail
        self.tail.prev = self.head

        #hashmap to store key:pointer pairs

        self.key_to_node = dict()


    def get(self, key: int) -> int:

        #if we dont have anything to return or key doesnt exist return -1

        if key not in self.key_to_node:
            return -1

        #else we get the value from the node and update position if nesscary

        else:

            node = self.key_to_node[key]

            #if the node is already head.next we dont need to move it

            if node == self.head.next:

                return node.val

            #First disconnect the node from its current position

            nextNode = node.next
            prevNode = node.prev
            
            prevNode.next = nextNode
            nextNode.prev = prevNode

            #Second we insert it next to head 

            #get node next to head 
            headNext = self.head.next

            #insert the MRU

            #set head.next to the MRU
            #set the old head.next previous pointer to the MRU 

            self.head.next = node
            headNext.prev = node

            #Update our MRU pointers so everything links up 

            node.next = headNext
            node.prev = self.head
            
            #return the value of the key from the node

            return node.val


    def put(self, key: int, value: int) -> None:

        #if the key exists, update the value of the node and do nothing

        if key in self.key_to_node:

            #get the node pointer from the dict

            node = self.key_to_node[key]

            #disconnect the node from current position while ensuring list still valid

            nextNode = node.next
            prevNode = node.prev

            nextNode.prev = prevNode
            prevNode.next = nextNode

            #place the new MRU while ensuring list still valid

            current_MRU = self.head.next

            self.head.next = node
            current_MRU.prev = node

            node.next = current_MRU
            node.prev = self.head

            #update the value 

            node.val = value

            return

        #if the key does not exist

        if self.current_capacity == self.capacity:

            #if we dont have any room remove the LRU

            LRU = self.tail.prev

            new_LRU = LRU.prev

            new_LRU.next = self.tail
            self.tail.prev = new_LRU

            del self.key_to_node[LRU.key] 

            self.current_capacity -= 1

        #add the new node

        newNode = Node(key, value)

        self.key_to_node[key] = newNode

        current_MRU = self.head.next

        self.head.next = newNode
        current_MRU.prev = newNode

        newNode.prev = self.head
        newNode.next = current_MRU

        self.current_capacity += 1 
