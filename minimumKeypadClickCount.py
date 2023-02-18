def minimumKeypadClickCount(text):
    # Write your code here
    dct = {}
    count = 0
    sum = 0
    for i in text:
        if i in dct:
            sum = sum + dct[i]
        else:
            if count < 9:
                dct[i] = 1
                print(dct)
                count += 1
            elif count >= 9 and count < 18:
                dct[i] = 2
                print(dct)
                count += 1
            else:
                dct[i] = 3
                print(dct)
    for j in dct:
        sum = sum + dct[j]
    return sum

print(minimumKeypadClickCount("abacdefghijklmnopqrstuvwxyz"))