from platform import node


class Node:
    def __init__(self, value=None):
        self.value = value 
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    # insert in Linked List
    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head is None: #------------------------------------------> O(1)
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0: #------------------------------------------> O(1)
                newNode.next = self.head
                self.head = newNode
            elif location == -1: # elif location == 1: #-----------------> O(1)
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1: #----------------------------> O(n)
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next #-------------------------------> O(1)
                tempNode.next = newNode #--------------------------------> O(1)
                newNode.next = nextNode #--------------------------------> O(1)
                if tempNode == self.tail: #------------------------------> O(1)
                    self.tail = newNode

# Time Complexity: O(n)
# Space Complexity: O(1) , Because here we are just creating 2 nodes. The 1st node is newNode and 2nd node is tempNode. Thats why the spaxe complexity is O(1).

singlyLinkedList = SLinkedList()
singlyLinkedList.insertSLL(1, -1)
singlyLinkedList.insertSLL(2, -1)
singlyLinkedList.insertSLL(3, -1)
singlyLinkedList.insertSLL(4, -1)

singlyLinkedList.insertSLL(0, 0)

singlyLinkedList.insertSLL(10, 3)

singlyLinkedList.insertSLL(20, 4)
print([node.value for node in singlyLinkedList])