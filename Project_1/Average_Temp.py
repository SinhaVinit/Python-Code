# Find number of days above average temperature

numDays = int(input("How many day's temperature? : "))
total = 0
daysTemp = []
for i in range(numDays):
    nextDay = int(input("Day " + str(i+1) + "'s high temperature: "))
    daysTemp.append(nextDay)
    total += daysTemp[i]

avg = round(total/numDays, 2)
print("\nAverage = " + str(avg))

above = 0
for i in daysTemp:
    if i > avg:
        above += 1

print(str(above) + " day(s) above average")