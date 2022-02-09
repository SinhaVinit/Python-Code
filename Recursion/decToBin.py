def decimalTOBinary(num):
    assert int(num) == num, "The parameter must be an integer only!"
    if num == 0:
        return 0
    return num%2 + 10*decimalTOBinary(int(num/2))

print(decimalTOBinary(15))