class Node:
    def __init__(self, value=None):
        self.value = value 
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

    def createCSLL(self, nodeValue):
        node = Node(nodeValue)
        node.next = node
        self.head = node
        self.tail = node
        return "The CSLL has been created."

    def insertCSLL(self, value, location):
        if self.head is None:
            return "The head reference is None." # -----------------------------> O(1)
        else:
            newNode = Node(value) # --------------------------------------------> O(1)
            if location == 0:
                newNode.next = self.head #
                self.head = newNode      # -------------------------------------> O(1)
                self.tail.next = newNode #
            elif location == -1:
                newNode.next = self.tail.next #
                self.tail.next = newNode      # --------------------------------> O(1)
                self.tail = newNode           #
            else:
                tempNode = self.head # -----------------------------------------> O(1)
                index = 0 # ----------------------------------------------------> O(1)
                while index < location - 1: #
                    tempNode =tempNode.next # ----------------------------------> O(n)
                    index += 1              #
                nextNode = tempNode.next #
                tempNode.next = newNode  # -------------------------------------> O(1)
                newNode.next = nextNode  #
            return "The node has been successfully inserted." # ----------------> O(1)
        # Time Complexity: O(n)
        # Space Complexity: O(1)



circularSLL = CircularSinglyLinkedList()
print(circularSLL.createCSLL(1))
# print(circularSLL.createCSLL(2))

circularSLL.insertCSLL(0,0)
circularSLL.insertCSLL(2,-1)
circularSLL.insertCSLL(3,-1)
circularSLL.insertCSLL(2,2)
circularSLL.insertCSLL(1,2)

print([node.value for node in circularSLL])