firstNumber = 0
secondNumber = 1
number = [0,1]
for i in range(10):
    nextNumber = firstNumber + secondNumber
    number.append(nextNumber)
    firstNumber = secondNumber
    secondNumber = nextNumber
print(number)