def fibonacci(number):
    assert number >= 0 and int(number) == number, "Fibonacci number can not be negative number or non integer."
    if number in [0,1]:
        return number
    return fibonacci(number-1) + fibonacci(number-2)

print(fibonacci(7))