class Queue:
    def __init__(self) -> None:
        self.items = []
    
    def __str__(self) -> str:
        values = [str(x) for x in self.items]
        return " ".join(values)
    
    def isEmpty(self):
        if self.items == []:
            return True
        return False
    
    def enqueue(self, value):
        self.items.append(value) #----------------- if memory alocation is used for large inputs then, O(n) and maybe O(n^2) too.
        return "The element {} is inserted at the end of Queue.".format(value)
    
    def dequeue(self):
        if self.isEmpty():
            return "The queue is empty." #-------------------- O(1)
        else:
            return self.items.pop(0) #---------------- O(n)
    
    def peek(self):
        if self.isEmpty():
            return "The queue is empty." #-------------------- O(1)
        else:
            return self.items[0] #--------------------- O(1)
    
    def delete(self):
        self.items = None #---------------------- O(1)
        return "Queue is deleted."

customQueue = Queue()
print("--------------------")
print(customQueue.isEmpty())
print("--------------------")
print(customQueue.enqueue(1))
print(customQueue.enqueue(2))
print(customQueue.enqueue(3))
print(customQueue.enqueue(4))
print("--------------------")
print(customQueue)
print("--------------------")
print(customQueue.dequeue())
print("--------------------")
print(customQueue)
print("--------------------")
print(customQueue.peek())
print("--------------------")
print(customQueue)
print("--------------------")
print(customQueue.delete())
print("--------------------")
# print(customQueue)
# print("--------------------")