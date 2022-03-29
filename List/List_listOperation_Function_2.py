# total = 0
# count = 0
# while (True):
#     inp = input("Enter a number: ")
#     if inp == "done":
#         break
#     value = float(inp)
#     total = total + value
#     count = count + 1
#     average = total / count

# print("Average: ", average)

# By ushing list and list functions
myList = []
while (True):
    inp = input("Enter a number: ")
    if inp == "done":
        break
    value = float(inp)
    myList.append(value)
average = sum(myList) / len(myList)

print("Average: ", average)