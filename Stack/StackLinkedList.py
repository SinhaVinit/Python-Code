class Node:
    def __init__(self, value = None) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def __iter__(self) -> None:
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

class Stack:
    def __init__(self) -> None:
        self.LinkedList = LinkedList()
    
    def __str__(self) -> str:
        values = [str(x.value) for x in self.LinkedList]
        return '\n'.join(values)
    
    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False
    
    def push(self, value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node
    
    def pop(self):
        if self.isEmpty():
            return "There is not any element in the stack."
        else:
            nodeValue = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return nodeValue
    
    def peek(self):
        if self.isEmpty():
            return "There is not any element in the stack."
        else:
            nodeValue = self.LinkedList.head.value
            return nodeValue
    
    def delete(self):
        self.LinkedList.head = None
        return "Stack is completely deleted."


myObj = Stack()
print("-----------")
print(myObj.isEmpty())
print("-----------")
myObj.push(1)
myObj.push(2)
myObj.push(3)
myObj.push(4)
print("-----------")
print(myObj)
print("-----------")
print(myObj.pop())
print("-----------")
print(myObj)
print("-----------")
print(myObj.peek())
print("-----------")
print(myObj.delete())
print("-----------")
print(myObj)