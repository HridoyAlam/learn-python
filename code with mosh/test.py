'''
name = input("What's your name? ")
color = input("What's your favorite color? ")
print(name + " likes "+color)

year = input("What's your birth year? ")
age = 2021 - int(year)
print("You are "+ str(age)+ "'s old.")


name = input("Eneter your name: ")
si = len(name)

if 3> si:
    print("Name must be at least 3 chracters!")
elif si >= 50:
    print("name can't be maximum of 50 character")
else:
    print(f'{name} looks good')


wieght = int(input("Enter your Weight: "))
unit = input("(L)lbs or (k) kg: ")

if unit.upper() =='L':
    convert = wieght *0.45
    print(f'yor are {convert} kilos.')
else:
    convert = wieght/0.45
    print(f'you are {round(convert,2)} pounds')

'''
'''
i =1;
while i<=5:
    
    #print(i, end=' ')
    print('*' * i)
    i +=1

'''
secret_number = 9
count = 0
guess_lives = 3
while count < guess_lives:
    guess=int(input("guess: "))
    count +=1
    if guess == secret_number:
        print("you won")
        break
    else:
        #lives = guess_lives - count
        print(f"you have {guess_lives - count} lives left")
        
else:
    print("Sorry you are failed")