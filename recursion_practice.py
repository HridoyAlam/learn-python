
'''
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)
    
print(factorial(5));
'''
'''
def sum_to(x):
    if x == 0:
        return 0
    else:
        return x+ sum_to(x-1)
print(sum_to(5))
'''
'''
def is_even(x):
    if x==0:
        return True
    else:
        return is_odd(x-1)
def is_odd(x):
    return not is_even(x)

print(is_even(23))
print(is_odd(17))
'''
def fib(x):
    if x==0 or x==1:
        return 1
    else:
        return fib(x-1)+fib(x-2)
print(fib(4))