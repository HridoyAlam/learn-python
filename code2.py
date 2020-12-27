# Python Program to convert a given list of integers and a tuple of integers into a list of strings

num_list = [1,2,3,4]
num_tuple = (0,1,2,3)

print("Orginal data set")
print(num_list)
print(num_tuple)

result_list = list(map(str,num_list))
result_tuple = list(map(str, num_tuple))
print("After type casting")
print(result_list)
print(result_tuple)