class Stack:
    def __init__(self, maxSize) -> None:
        self.maxSize = maxSize
        self.list = []
    
    def __str__(self) -> str:
        values = reversed(self.list)
        values = [str(x) for x in values]
        return '\n'.join(values)
    
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
    
    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False
    
    def push(self, value):
        if self.isFull():
            return "The stack is full."
        else:
            self.list.append(value)
            return "The element has been successfully inserted."
    
    def pop(self):
        return self.list.pop()
    
    def peek(self):
        if self.isEmpty():
            return "There is not any element in the stack."
        else:
            return self.list[-1]
    
    def delete(self):
        self.list = None
        return "Stack is completely deleted."


myObj = Stack(4)
print("-----------")
print(myObj.isEmpty())
print("-----------")
print(myObj.isFull())
print("-----------")
print(myObj.push(1))
print(myObj.push(2))
print(myObj.push(3))
print(myObj.push(4))
print("-----------")
print(myObj)
print("-----------")
print(myObj.isEmpty())
print("-----------")
print(myObj.isFull())
print("-----------")
print(myObj.push(5))
print("-----------")
myObj.pop()
print("-----------")
print(myObj)
print("-----------")
print(myObj.peek())
print("-----------")
print(myObj)
print("-----------")
print(myObj.delete())
print("-----------")
# print(myObj)