#Python program to add three given list using Python map and lambda

num1 = [1,2,3]
num2 = [4,5,6]
num3 = [7,8,9]

print("Orginal list")
print(num1)
print(num2)
print(num3)

result = map(lambda x,y,z: x+y+z, num1,num2,num3)

print("after lambda ooperations")
print(list(result))