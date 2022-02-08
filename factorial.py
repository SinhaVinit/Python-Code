import re
from struct import pack_into


def factorial(number):
    assert number > 0 and int(number) == number, "The number must be positive integer only!"
    if number == 0 or number == 1: # if number in [0,1]:
        result = 1
    else:
        result = number*factorial(number-1)
    return result
print(factorial(5))