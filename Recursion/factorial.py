def factorial(number):
    assert number > 0 and int(number) == number, "The number must be positive integer only!"
    if number == 0 or number == 1: # if number in [0,1]:
        return 1
    return number*factorial(number-1)

print(factorial(4))