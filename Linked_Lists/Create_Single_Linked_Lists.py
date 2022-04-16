class Node:
    def __init__(self, value=None):
        self.value = value #----------------------------------> O(1)
        self.next = None #------------------------------------> O(1)

class SLinkedList:
    def __init__(self):
        self.head = None #------------------------------------> O(1)
        self.tail = None #------------------------------------> O(1) 

singlyLinkedList = SLinkedList()
node1 = Node(1)
node2 = Node(2)

singlyLinkedList.head = node1 #-------------------------------> O(1)
singlyLinkedList.head.next = node2 #--------------------------> O(1)
singlyLinkedList.tail = node2 #-------------------------------> O(1)

# Time Complexity: O(1)
# Space Complexity: O(1) --> Because all we are doing here is just creating head and tail pointers and creating a blank node. If we create more than one node then the space complexity will be O(n), because it depends on the number of elements of the Singly Linked Lists.