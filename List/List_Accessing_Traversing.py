shoppingList = ["Milk", "Cheese", "Butter"]

print("---------------------------------")
print(shoppingList[0])
print(shoppingList[1])
print(shoppingList[2])

print("---------------------------------")
print("Milk" in shoppingList)
print("Bread" in shoppingList)

print("---------------------------------")
print(shoppingList[-1])
print(shoppingList[-2])
print(shoppingList[-3])

print("---------------------------------")
for i in shoppingList:
    print(i)

print("---------------------------------")
for i in range(len(shoppingList)):
    shoppingList[i] = shoppingList[i] + " Food"
    print(shoppingList[i])

print("---------------------------------")
emptyList = []
for i in emptyList:
    print("I an empty")