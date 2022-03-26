l1 = [2,4,3]
l2 = [5,6,4]
def addTwoNumbers(l1, l2):
    lst = []
    rem = 0
    if len(l1) >= len(l2):
        for i in range(len(l1)):
            if len(l2) > i:
                num = l1[i]+l2[i]+rem
                rem = 0
                lst.append(num%10)
                if num >= 10:
                    rem = int(num/10)         
            else:
                num = l1[i] + rem
                rem = 0
                lst.append(num%10)
                if num >= 10:
                    rem = int(num/10)
        if rem > 0:
            lst.append(rem)
        return lst

    else:
        for i in range(len(l2)):
            if len(l1) > i:
                num = l1[i]+l2[i]+rem
                rem = 0
                lst.append(num%10)
                if num >= 10:
                    rem = int(num/10)         
            else:
                num = l2[i] + rem
                rem = 0
                lst.append(num%10)
                if num >= 10:
                    rem = int(num/10)
        if rem > 0:
            lst.append(rem)
        return lst

print(addTwoNumbers(l1,l2))