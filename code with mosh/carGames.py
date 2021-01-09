'''
while True:
    ins = input()
    if ins.upper() == "START":
        print("Car started... Ready to go")
    elif ins.upper() == "STOP":
        print("Car stopped...")
    elif ins.upper() == "QUIT":
        break
    else:
        print("I don't understand that...")

command =''
started = False
while True:
    command = input("> ").lower()


    if command == "start":
        if started:
            print("Car already started... man what are doing")
        else:
            started = True
            print("Car started... Ready to go")
    elif command == "stop":
        if not started:
            print("Car already stoped... man what are doing")
        else:
            started = False
            print("Car stopped...")
    elif command =="quit":
        break
    elif command == "help":
        print("""
                start -> to start the car
                stop -> to stop the car
                quit -> quit the program
        """)
    else:
        print("I don't understand that...")

list = [5,2,5,2,2,1,1,4,5,9]
for i in list:
    for j in range(i):
        print('x',end='')
    print()
print("another easy way\n")
for x_count in list:
    print('x' * x_count)
duplicate=[]
for i in list:
    if i not in duplicate:
        duplicate.append(i)
print(duplicate)


'''
# tuples are immutable

numbers = (1,2,3,4)
print(numbers)
n = len(numbers)
print(n)

# unpacking

coordinates = (1,2,3)
x,y,z = coordinates
print(x)
print(y)