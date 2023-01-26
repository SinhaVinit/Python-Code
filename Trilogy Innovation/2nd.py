a = [1,4,6,2]
b = 2
sum1 = 0
if b>1 and b<16:
    a.sort()
    for i in range(b):
        if (i == b-1):
            s = (sum(a))**2
        else:
            c = -1
            sum1 = sum1 + (a[c])**2
            a.pop(c)
    print(sum1+s)
else:
    print(sum(a)**2)