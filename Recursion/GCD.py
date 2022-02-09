from math import gcd


def gcd(num1, num2):
    assert int(num1) == num1 and int(num2) == num2, "The numbers must me integer"
    if num1<0:
        num1 = -1*num1
    if num2<0:
        num2 = -1*num2
    if num2 == 0:
        return num1
    return gcd(num2, num1%num2)

print(gcd(18,48))