max_val = int(input("taking max value from users : "))
odd_list = []
for i in range(1, max_val+1):
    if (i%2) == 1:
        odd_list.append(i)

print('print odd list',odd_list)

