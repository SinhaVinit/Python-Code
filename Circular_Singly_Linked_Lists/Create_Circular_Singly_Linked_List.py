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
            if node.next == self.head:
                break
            node = node.next

    # Creation of circular singly linked list
    def createCSLL(self, nodeValue):
        # -----------------------------------------> O(1)
        node = Node(nodeValue)
        # -----------------------------------------------> O(1)
        node.next = node
        # -----------------------------------------------> O(1)
        self.head = node
        # -----------------------------------------------> O(1)
        self.tail = node
        # ----------------------------> O(1)
        return "The CSLL has been created."

        # Time Complexity: O(1)
        # Space Complexity: O(1)


circularSLL = CircularSinglyLinkedList()
circularSLL.createCSLL(1)
circularSLL.createCSLL(2)

print([node.value for node in circularSLL])
