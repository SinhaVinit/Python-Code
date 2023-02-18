def abc(s, t):
    lst1 = list(s)
    lst2 = list(t)
    count = 0
    ans = 0
    num = 0
    while num == 0:
        for i in lst2:
            count += 1
            for j in range(len(lst1)):
                if i == lst1[j]:
                    lst1[j] = 0
                    break
                if i not in lst1:
                    return ans
            if count == len(lst2):
                ans += 1
        count = 0
        for i in lst1:
            if i == 0:
                num = 0
            else:
                if i in lst2:
                    num = 0
                else:
                    num = 1
    return ans

print(abc("abacbc", "bca"))