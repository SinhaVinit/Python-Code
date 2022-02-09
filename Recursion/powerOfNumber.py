def powerOfNumber(number, power):
    assert power >= 0 and int(power) ==  power, "The power must be positive integer only"
    if power == 1:
        return number
    elif power == 0:
        return 1
    return number * powerOfNumber(number, power-1)

print(powerOfNumber(2,2))