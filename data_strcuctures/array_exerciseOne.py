expense = [2200,2350,2600,2130,2190]

print(expense[1]-expense[0])
sum =0
for i in range(3):
    sum +=expense[i]
print(sum)

for i in range(len(expense)):
    if expense[i] == 2000:
        print("yes")


expense.insert(5,1980)

print(expense)

expense[3] = expense[3] - 200
print(expense)