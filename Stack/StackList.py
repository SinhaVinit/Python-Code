class Stack:
    def __init__(self) -> None:
        self.list = [] #----------------------------------------------- Time Complexity: O(1)
    
    def __str__(self) -> str:
        values = reversed(self.list)
        values = [str(x) for x in values]
        return '\n'.join(values)
    
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
    
    def push(self, value): 
        self.list.append(value)
        return "This element has been successfully inserted."
    
    def pop(self):
        if self.isEmpty():
            return "There is not any element in the stack."
        else:
            return self.list.pop()
    
    def peek(self):
        if self.isEmpty():
            return "There is not any element in the stack."
        else:
            return self.list[-1]
    
    def delete(self):
        self.list = None
        return "Stack is completely deleted."


myObj = Stack()
print("-----------")
print(myObj.isEmpty())
print("-----------")
myObj.push(1)
myObj.push(2)
myObj.push(3)
myObj.push(4)
print(myObj)
print("-----------")
myObj.pop()
print(myObj)
print("-----------")
print(myObj.peek())
print("-----------")
print(myObj)
print("-----------")
print(myObj.delete())
print("-----------")
# print(myObj)