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
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == -1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
                if tempNode == self.tail:
                    self.tail = newNode

    # traverse Singly Linked List
    def traverseSLL(self):
        if self.head is None:
            print("The Singly Linked List does not exist")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next
    
    def searchSLL(self, nodeValue):
        if self.head is None: #---------------------------------------------> O(1)
            return "The Linked List is not exist." #------------------------> O(1)
        else:
            node = self.head #----------------------------------------------> O(1)
            while node is not None: #---------------------------------------> O(n)
                if node.value == nodeValue: #-------------------------------> O(1)
                    return node.value #-------------------------------------> O(1)
                node = node.next
            return "The value does not exist in this Linked List." #--------> O(1)
        # Time Complexity: O(n)
        # Space Complexity: O(1)

singlyLinkedList = SLinkedList()
singlyLinkedList.insertSLL(1, -1)
singlyLinkedList.insertSLL(2, -1)
singlyLinkedList.insertSLL(3, -1)
singlyLinkedList.insertSLL(4, -1)

singlyLinkedList.insertSLL(0, 0)

singlyLinkedList.insertSLL(10, 3)

singlyLinkedList.insertSLL(20, 4)
print([node.value for node in singlyLinkedList])
# singlyLinkedList.traverseSLL()
print(singlyLinkedList.searchSLL(3))
print(singlyLinkedList.searchSLL(100))