numlist = list()

while True:
    inp = input("Enter a number: ")
    if inp =="Done" or inp =="done":
        break
    value = float(inp)
    numlist.append(value)

average = sum(numlist)/len(numlist)
print(f"Average value of given list is: {average}")