'''
a = 4
b = 3

print(a,b)
temp = a
a = b
b = temp
print(a,b)
'''
#dictionaries

customer = {
    "name" : "Hridoy Alam",
    "age" : 25,
    "b_group": 'ab+'
}

print(customer['name'])
print(customer.get('age'))

#update
customer['name']='aron smith'
print(customer.get('name'))