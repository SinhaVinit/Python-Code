def sumOfDigits(number):
    assert number >= 0 and int(number) == number, "The number has to be a positive only"
    if number < 1:
        return 0
    return (int(number%10) + sumOfDigits(int(number/10)))

print(sumOfDigits(1234321))