def min_max_time(date):
    lst = []
    min_lst = []
    max_lst =[]
    for i in range(len(date)):
        lst.append(date[i])
    for j in range(len(lst)):
        if lst[j] == " ":
            if j == 0 or j == 3 or j == 6:
                min_lst.append("0")
                max_lst.append("5")
            elif j == 1 or j == 4 or j == 7:
                min_lst.append("0")
                max_lst.append("9")
        else:
            min_lst.append(lst[j])
            max_lst.append(lst[j])
    min_time = "".join(min_lst)
    max_time = "".join(max_lst)
    return (min_time, max_time)

date = str(input())
print(min_max_time(date))