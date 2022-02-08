def sumOfDigits(number):
    number = int(number)
    if number < 1:
        return 0
    return (number%10 + sumOfDigits(number/10))

print(sumOfDigits(121))